"""Regression tests for the corrected portfolio analyses, with independent expectations."""
from pathlib import Path
from collections import Counter
import copy
import csv
import datetime as dt
import importlib.util
import json
import subprocess
import shutil
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
P = ROOT/"projects"

def load(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

H=P/"01-nist-csf-risk-assessment"
K=P/"02-cisa-kev-vulnerability-prioritization"
A=P/"04-aws-cloud-security-log-investigation"
T=P/"03-mitre-attack-cti-brief"
h=load("hhs",H/"scripts/analyze_hhs_breaches.py")
k=load("kev",K/"scripts/analyze_kev.py")
a=load("cloud",A/"scripts/analyze_cloudtrail.py")
repro=load("repro",ROOT/"tools/reproduce.py")

def event(name, params=None, **extra):
    result={"eventTime":"2026-09-01T00:00:00Z","eventName":name,
            "eventSource":a.EXPECTED.get(name,"example.amazonaws.com"),
            "userIdentity":{"type":"AssumedRole","arn":"arn:aws:sts::111122223333:assumed-role/test/session-a"},
            "requestParameters":params or {}}
    result.update(extra)
    return result

def permission(cidr="0.0.0.0/0",lo=22,hi=22,proto="tcp",ipv6=False):
    return {"ipProtocol":proto,"fromPort":lo,"toPort":hi,
            "ipv6Ranges" if ipv6 else "ipRanges":{"items":[{"cidrIpv6" if ipv6 else "cidrIp":cidr}]}}

class Healthcare(unittest.TestCase):
    def test_sample_arithmetic_and_categories(self):
        rows=h.read_rows(H/"data/hhs-ocr-breach-sample-2026-05-16.csv")
        self.assertEqual(len(rows),100)
        self.assertEqual(sum(h.parse_int(r["individuals_affected"]) for r in rows),6692288)
        summary=h.build_summary(rows,dt.date(2026,5,16))
        self.assertIn("5,140.5",summary)
        self.assertEqual(len(h.counter_by(rows,"location_of_breached_information")),11)
        self.assertEqual(h.counter_by(rows,"location_of_breached_information")["Network Server"],60)
        self.assertEqual(sum("Network Server" in r["location_of_breached_information"] for r in rows),67)
        self.assertEqual(sum(not r["state"].strip() for r in rows),2)

    def test_invalid_count_is_not_silently_zero(self):
        for value in ["","-1","2.5","bad"]:
            with self.subTest(value=value),self.assertRaises(ValueError):
                h.parse_int(value)
        self.assertEqual(h.parse_int("1,234"),1234)

    def test_input_rejection(self):
        sample=h.read_rows(H/"data/hhs-ocr-breach-sample-2026-05-16.csv")[0]
        bad_date=dict(sample,breach_submission_date="not-a-date")
        missing_value=dict(sample,covered_entity="")
        for rows in [[],[sample,sample],[bad_date],[missing_value]]:
            with self.subTest(rows=len(rows)),tempfile.TemporaryDirectory() as tmp:
                path=Path(tmp)/"bad.csv"
                with path.open("w",newline="",encoding="utf-8") as out:
                    writer=csv.DictWriter(out,fieldnames=list(sample))
                    writer.writeheader();writer.writerows(rows)
                with self.assertRaises(ValueError):h.read_rows(path)

class Kev(unittest.TestCase):
    def setUp(self):
        self.rows=k.read_rows(K/"data/known_exploited_vulnerabilities-2026-05-16.csv")
        self.base=dict(self.rows[0],dateAdded="2020-01-01",dueDate="2026-05-01")
    def test_worked_example(self):
        row=next(r for r in self.rows if r["cveID"]=="CVE-2024-1708")
        scored=k.score_row(row,dt.date(2026,5,16))
        self.assertEqual((scored["score"],scored["priority"]),(116,"First review"))
    def test_old_overdue_bonus_does_not_decay(self):
        scores=[k.score_row(self.base,dt.date(2026,5,1)+dt.timedelta(days=n))["score"] for n in [1,31,91,366]]
        self.assertEqual(len(set(scores)),1)
    def test_future_addition_rejected(self):
        with self.assertRaises(ValueError):k.score_row(dict(self.base,dateAdded="2026-05-17"),dt.date(2026,5,16))
    def test_due_boundary(self):
        day=dt.date(2026,5,16)
        far=k.score_row(dict(self.base,dueDate=(day+dt.timedelta(days=31)).isoformat()),day)["score"]
        for delta,bonus in [(-400,15),(-1,15),(0,15),(7,15),(8,10),(30,10),(31,0)]:
            with self.subTest(delta=delta):
                self.assertEqual(k.score_row(dict(self.base,dueDate=(day+dt.timedelta(days=delta)).isoformat()),day)["score"]-far,bonus)
    def test_quoted_cwe(self):
        self.assertEqual(k.cwe_counter([{"cwes":'["CWE-20", "CWE-78"]'}]),Counter({"CWE-20":1,"CWE-78":1}))
    def test_unique_source_and_full_ranking(self):
        ranking=list(csv.DictReader((K/"outputs/kev-full-ranking-2026-05-16.csv").read_text(encoding="utf-8").splitlines()))
        self.assertEqual(len(ranking),1592)
        self.assertEqual(len({r["cveID"] for r in ranking}),1592)
        self.assertEqual({r["cveID"] for r in ranking},{r["cveID"] for r in self.rows})
    def test_duplicate_invalid_and_empty_csv(self):
        for rows in [[],[self.base,self.base],[dict(self.base,cveID="bad")],[dict(self.base,knownRansomwareCampaignUse="No")]]:
            with self.subTest(rows=len(rows)),tempfile.TemporaryDirectory() as tmp:
                path=Path(tmp)/"bad.csv"
                with path.open("w",newline="",encoding="utf-8") as out:
                    writer=csv.DictWriter(out,fieldnames=list(self.base));writer.writeheader();writer.writerows(rows)
                with self.assertRaises(ValueError):k.read_rows(path)

class Cloud(unittest.TestCase):
    def test_supplied_fixture(self):
        events=a.load_events(A/"data/sample-cloudtrail-events.json")
        findings=[f for e in events for f in a.analyze_event(e)]
        self.assertEqual(len(events),12)
        self.assertEqual(Counter(f["severity"] for f in findings),{"High":5,"Medium":3,"Informational":2})
    def test_denied_action_does_not_become_success(self):
        for name in ["StopLogging","AuthorizeSecurityGroupIngress","PutBucketPolicy","CreateAccessKey"]:
            with self.subTest(name=name):
                findings=a.analyze_event(event(name,errorCode="AccessDenied"))
                self.assertEqual(len(findings),1)
                self.assertEqual(findings[0]["outcome"],"Denied/error")
                self.assertEqual(findings[0]["severity"],"Medium")
    def test_service_name_guard(self):
        self.assertEqual(a.analyze_event(event("StopLogging",eventSource="s3.amazonaws.com")),[])
    def test_successful_stop_requires_review(self):
        self.assertEqual(a.analyze_event(event("StopLogging"))[0]["severity"],"High")
    def test_failed_signin(self):
        f=a.analyze_event(event("ConsoleLogin",responseElements={"ConsoleLogin":"Failure"}))[0]
        self.assertEqual(f["outcome"],"Sign-in failure")
    def test_root_identity(self):
        f=a.analyze_event(event("ConsoleLogin",userIdentity={"type":"Root"},responseElements={"ConsoleLogin":"Success"}))
        self.assertEqual(f[0]["signal"],"Root identity activity")
    def test_admin_ports_ranges_ipv6_and_protocols(self):
        cases=[permission(),permission("::/0",3389,3389,ipv6=True),permission(lo=1,hi=65535),permission(proto="-1")]
        for rule in cases:
            with self.subTest(rule=rule):
                f=a.analyze_event(event("AuthorizeSecurityGroupIngress",{"ipPermissions":{"items":[rule]}}))
                self.assertEqual(f[0]["severity"],"High")
    def test_unrelated_rules_are_not_combined(self):
        rules=[permission("10.0.0.0/8"),permission(lo=443,hi=443)]
        f=a.analyze_event(event("AuthorizeSecurityGroupIngress",{"ipPermissions":{"items":rules}}))
        self.assertEqual(len(f),1);self.assertEqual(f[0]["severity"],"Medium")
    def test_private_only_ingress(self):
        self.assertEqual(a.analyze_event(event("AuthorizeSecurityGroupIngress",{"ipPermissions":{"items":[permission("10.0.0.0/8")]}})),[])
    def test_bucket_deny_and_allow(self):
        for field in ["policy","bucketPolicy"]:
            for effect,expected in [("Deny",0),("Allow",1)]:
                with self.subTest(field=field,effect=effect):
                    p={field:{"Statement":[{"Effect":effect,"Principal":"*","Action":"s3:GetObject","Condition":{"StringEquals":{"aws:PrincipalOrgID":"o-example"}}}]}}
                    f=a.analyze_event(event("PutBucketPolicy",p))
                    self.assertEqual(len(f),expected)
                    if f:self.assertEqual(f[0]["severity"],"Medium")
    def test_bpa_requires_all_four_true(self):
        config={key:True for key in ["BlockPublicAcls","IgnorePublicAcls","BlockPublicPolicy","RestrictPublicBuckets"]}
        self.assertEqual(a.analyze_event(event("PutPublicAccessBlock",{"PublicAccessBlockConfiguration":config}))[0]["severity"],"Informational")
        config["BlockPublicPolicy"]=False
        self.assertEqual(a.analyze_event(event("PutPublicAccessBlock",{"PublicAccessBlockConfiguration":config}))[0]["severity"],"Medium")
    def test_guardduty_enabled_is_not_disabled(self):
        self.assertEqual(a.analyze_event(event("CreateDetector",{"enable":True}))[0]["severity"],"Informational")
        self.assertEqual(a.analyze_event(event("UpdateDetector",{"enable":False}))[0]["severity"],"High")
    def test_removal_does_not_establish_closure(self):
        f=a.analyze_event(event("RevokeSecurityGroupIngress"))[0]
        self.assertEqual(f["severity"],"Informational");self.assertIn("not proof",f["why_it_matters"])
    def test_duplicate_and_distinct_sessions(self):
        first=event("StartLogging",eventID="same",recipientAccountId="111122223333",awsRegion="us-west-2")
        different=copy.deepcopy(first);different["eventID"]="second"
        different["userIdentity"]["arn"]=different["userIdentity"]["arn"].replace("session-a","session-b")
        unique,count=a.deduplicate([first,copy.deepcopy(first),different])
        self.assertEqual((len(unique),count),(2,1))
        self.assertNotEqual(a.actor(first),a.actor(different))
        self.assertEqual(a.deduplicate([event("StartLogging"),event("StartLogging")])[1],1)
    def test_event_history_and_rejected_formats(self):
        e=event("StartLogging")
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"events.json"
            for data in [{"Records":[e]},{"Events":[{"CloudTrailEvent":json.dumps(e)}]},[e],e]:
                p.write_text(json.dumps(data),encoding="utf-8")
                self.assertEqual(a.load_events(p),[e])
            for data in [[],[{}],[dict(e,requestParameters="wrong")]]:
                p.write_text(json.dumps(data),encoding="utf-8")
                with self.assertRaises(ValueError):a.load_events(p)
            with self.assertRaises(ValueError):a.load_events(Path(tmp)/"events.csv")
    def test_legacy_sanitizer_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"out.json"
            result=subprocess.run([sys.executable,str(A/"scripts/sanitize_cloudtrail.py"),"input.json","--output",str(p)],capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0);self.assertFalse(p.exists())

class ProvenanceAndArtifacts(unittest.TestCase):
    def test_layer_matches_supported_evidence(self):
        layer=json.loads((T/"attack-navigator-layer.json").read_text(encoding="utf-8"))
        index=json.loads((T/"evidence/selected-relationships.json").read_text(encoding="utf-8"))
        self.assertEqual(len(layer["techniques"]),11)
        self.assertEqual({(t["techniqueID"],t["tactic"]) for t in layer["techniques"]},{(t["technique_id"],t["tactic"]) for t in index["relationships"]})
        self.assertEqual(next(t["tactic"] for t in layer["techniques"] if t["techniqueID"]=="T1213.003"),"collection")
    def test_rule_index_is_current(self):
        stored=json.loads((A/"detections/cloudtrail-detection-rules.json").read_text(encoding="utf-8"))
        self.assertEqual(stored,repro.cloud_index())
    def test_template_source_arn_and_scope(self):
        text=(A/"cloudformation/aws-cloud-security-lab.yaml").read_text(encoding="utf-8")
        self.assertEqual(text.count("aws:SourceArn:"),2)
        self.assertIn("IsMultiRegionTrail: false",text)
        self.assertNotIn("AWS::EC2::Instance",text)
    def test_healthcare_visual_uses_independent_expected_counts(self):
        svg=ET.parse(H/"visuals/information-location-records.svg").getroot()
        values=[n.text for n in svg.findall(".//{http://www.w3.org/2000/svg}text") if (n.text or "").isdigit()]
        self.assertEqual(values,["60","67","21","24"])

    def test_generated_visuals_are_reproducible(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)/"repo"
            shutil.copytree(ROOT,target,ignore=shutil.ignore_patterns(".git","__pycache__"))
            subprocess.run([sys.executable,str(target/"tools/generate_portfolio_visuals.py")],check=True,capture_output=True)
            for source in ROOT.glob("projects/**/*.svg"):
                self.assertEqual(source.read_text(encoding="utf-8"),(target/source.relative_to(ROOT)).read_text(encoding="utf-8"))

    def test_generated_outputs_are_reproducible(self):
        cases=[
            (H,"analyze_hhs_breaches.py","hhs-ocr-breach-sample-2026-05-16.csv",["--as-of","2026-05-16"]),
            (K,"analyze_kev.py","known_exploited_vulnerabilities-2026-05-16.csv",["--as-of","2026-05-16"]),
            (A,"analyze_cloudtrail.py","sample-cloudtrail-events.json",[])]
        for project,script,source,extra in cases:
            with self.subTest(project=project.name),tempfile.TemporaryDirectory() as tmp:
                subprocess.run([sys.executable,str(project/"scripts"/script),str(project/"data"/source),*extra,"--output-dir",tmp],check=True,capture_output=True)
                for path in Path(tmp).iterdir():
                    self.assertEqual(path.read_text(encoding="utf-8"),(project/"outputs"/path.name).read_text(encoding="utf-8"))

if __name__=="__main__":
    unittest.main()
