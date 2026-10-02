"""Generate repository-native SVGs from retained data and explicit design notes.

Run from any directory: python tools/generate_portfolio_visuals.py
No third-party packages or network calls.
"""
from pathlib import Path
from collections import Counter
import csv
import html
import importlib.util
import json
import statistics
import textwrap

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
NAVY, TEAL, GRAY = "#142b43", "#147d83", "#46576a"

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

def text(x, y, value, size=22, color=NAVY, weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}">{html.escape(str(value))}</text>'

def start(title, description, height):
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{height}" viewBox="0 0 760 {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{html.escape(title)}</title>',
        f'<desc id="desc">{html.escape(description)}</desc>',
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#147d83"/></marker></defs>',
        '<rect width="760" height="100%" rx="8" fill="#ffffff"/>',
        '<g font-family="Arial, Helvetica, sans-serif">',
        '<rect x="30" y="28" width="42" height="5" fill="#147d83"/>',
    ]
    for i, line in enumerate(textwrap.wrap(title, 42)):
        out.append(text(30, 70+i*34, line, 29, weight=700))
    return out

def save(path, parts):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts+["</g></svg>"])+"\n", encoding="utf-8")

def flow(path, title, note, steps, connected=True):
    """Vertical cards keep the reading order clear at narrow widths."""
    card_h = 142
    top = 154
    height = top + len(steps)*(card_h+30)+40
    parts = start(title, note+" "+" ".join(a+": "+b for a,b in steps), height)
    parts.append(text(30, 126, note, 18, GRAY))
    for i,(label,body) in enumerate(steps):
        y=top+i*(card_h+30)
        parts.append(f'<rect x="30" y="{y}" width="700" height="{card_h}" rx="8" fill="#f4f8fa" stroke="#c7d3df"/>')
        parts.append(text(50,y+34,f"{i+1}. {label}",24,weight=700))
        for j,line in enumerate(textwrap.wrap(body,57)):
            parts.append(text(50,y+68+j*27,line,21,GRAY))
        if connected and i<len(steps)-1:
            parts.append(f'<path d="M 380 {y+card_h+3} V {y+card_h+25}" stroke="{TEAL}" stroke-width="2" fill="none" marker-end="url(#arrow)"/>')
    save(path,parts)

def bars(path,title,note,rows):
    height=174+len(rows)*96
    parts=start(title,note+" "+"; ".join(f"{k}: {v:,}" for k,v in rows),height)
    parts.append(text(30,126,note,18,GRAY))
    maxv=max([v for _,v in rows]+[1])
    for i,(label,value) in enumerate(rows):
        y=160+i*96
        parts.append(text(30,y,label,21,weight=700))
        parts.append(f'<rect x="30" y="{y+16}" width="540" height="22" rx="3" fill="#e6edf2"/>')
        parts.append(f'<rect x="30" y="{y+16}" width="{540*value/maxv:.2f}" height="22" rx="3" fill="{TEAL}"/>')
        parts.append(text(595,y+36,f"{value:,}",23,weight=700))
    save(path,parts)

def main():
    h = PROJECTS/"01-nist-csf-risk-assessment"
    hm=module("hhs",h/"scripts/analyze_hhs_breaches.py")
    rows=hm.read_rows(h/"data/hhs-ocr-breach-sample-2026-05-16.csv")
    loc=Counter(r["location_of_breached_information"] for r in rows)
    vals=[hm.parse_int(r["individuals_affected"]) for r in rows]
    # Strip whitespace in tokenized multi-value fields.
    mentions=lambda s:sum(s in [p.strip() for p in r["location_of_breached_information"].split(",")] for r in rows)
    bars(h/"visuals/information-location-records.svg","Exact labels and mentions differ","100 reports; mention counts overlap.",[
        ("Network Server only",loc["Network Server"]),("Any Network Server mention",mentions("Network Server")),
        ("Email only",loc["Email"]),("Any Email mention",mentions("Email"))])
    flow(h/"visuals/healthcare-breach-dashboard.svg","Read the denominator first","Retained HHS sample; not an industry estimate.",[
        ("100 reported breaches","A convenience sample; original portal capture is missing."),
        (f"{sum(vals):,} reported affected individuals","A sum across reports, not a count of unique people."),
        (f"{max(vals)/sum(vals):.1%} from one report",f"The median is {statistics.median(vals):,.1f}. Large reports strongly affect the total.")],False)
    bars(h/"visuals/breach-type-distribution.svg","Breach labels in the retained sample","100 reports; labels do not establish the cause.",hm.counter_by(rows,"type_of_breach").most_common())
    bars(h/"visuals/entity-type-distribution.svg","Reporting entity types","100 reports; not a market-share or risk measure.",hm.counter_by(rows,"covered_entity_type").most_common())
    bars(h/"visuals/affected-individuals-by-breach-type.svg","Reported affected counts by label","Sums across reports; individuals may overlap.",sorted(hm.affected_by(rows,"type_of_breach").items(),key=lambda x:x[1],reverse=True))

    k=PROJECTS/"02-cisa-kev-vulnerability-prioritization"
    km=module("kev",k/"scripts/analyze_kev.py")
    kr=km.read_rows(k/"data/known_exploited_vulnerabilities-2026-05-16.csv")
    ranked=list(csv.DictReader((k/"outputs/kev-full-ranking-2026-05-16.csv").read_text(encoding="utf-8").splitlines()))
    flow(k/"visuals/kev-dashboard.svg","Where this project stops","Only step 1 is implemented in this repository.",[
        ("Rank catalog research | implemented","1,592 retained entries. Each score carries a reason."),
        ("Validate the asset | proposed","Confirm product, version, configuration and owner."),
        ("Choose an authorized action | proposed","Use vendor guidance and the organization’s policy."),
        ("Retest and record disposition | proposed","Verify the result or document an approved exception.")])
    bars(k/"visuals/vendor-kev-counts.svg","Most represented vendors in this file","Catalog counts do not rank vendor security.",Counter(r["vendorProject"] for r in kr).most_common(8))
    bars(k/"visuals/cwe-patterns.svg","Most frequent weakness labels","CWE counts can overlap within a vulnerability.",km.cwe_counter(kr).most_common(8))
    bars(k/"visuals/ransomware-use.svg","Ransomware-use field","Unknown does not mean no ransomware use.",Counter(r["knownRansomwareCampaignUse"] for r in kr).most_common())
    bars(k/"visuals/kev-additions-by-year.svg","Catalog additions by year","2026 is partial through the retained snapshot.",sorted(km.additions_by_year(kr).items()))
    counts=Counter(r["priority"] for r in ranked)
    bars(k/"visuals/priority-distribution.svg","Research queue after the model fix","Custom intake labels, not severity or exposure.",[(p,counts[p]) for p in ["First review","Next review","Standard review","Research queue"]])

    t=PROJECTS/"03-mitre-attack-cti-brief"
    flow(t/"visuals/scattered-spider-attack-flow.svg","Connect the identity evidence","Proposed investigation aid; no incident reconstructed.",[
        ("Support contact","Who requested a change? Which verification and approval were recorded?"),
        ("Factor or account change","Which identity, actor and result appear in the audit event?"),
        ("Subsequent access","Can sign-in and application records support or contradict the hypothesis?")])
    flow(t/"visuals/identity-defense-workflow.svg","Test the explanation before acting","Proposed workflow; detection performance is untested.",[
        ("Preserve and connect records","Use stable identifiers and normalized timestamps."),
        ("Check legitimate recovery","Compare authorization, user context and normal activity."),
        ("Use an authorized response","Escalate to the responsible identity or security owner."),
        ("Verify final state and user access","Record what changed and what remains uncertain.")])

    a=PROJECTS/"04-aws-cloud-security-log-investigation"
    flow(a/"visuals/cloudtrail-investigation-workflow.svg","Attempt, outcome, next check","Synthetic fixture: September 1, 2026, 16:32:15Z.",[
        ("eventName: StopLogging","The requested action concerns a CloudTrail trail."),
        ("errorCode: AccessDenied","The record reports a denied request. Do not infer a successful stop."),
        ("Medium review signal","Check intent, related events, trail status and actual log delivery.")])
    flow(a/"visuals/aws-lab-architecture.svg","Proposed AWS template boundaries","Not deployed. Numbering groups resources, not data flow.",[
        ("CloudTrail delivers to its log bucket","Single-Region management events; validation enabled. No S3 object data events."),
        ("Separate evidence bucket","Versioned, encrypted storage. It is not the trail destination."),
        ("Detached VPC, subnet and group","No compute instances, internet gateway or NAT gateway."),
        ("Account analyzer; optional GuardDuty","Access Analyzer is defined. GuardDuty defaults to disabled.")],False)
    bars(a/"visuals/cloudtrail-risk-signals.svg","Review signals from 12 synthetic events","Urgency for review; no confirmed incidents.",[("High",5),("Medium",3),("Informational",2)])

    c=PROJECTS/"05-serenity-bank-capstone"
    flow(c/"visuals/identity-boundaries.svg","Four identities, separate permissions","Academic proposal. These are parallel access paths.",[
        ("Customer","Customer sign-in → application authorization → permitted account record."),
        ("Employee","Workforce sign-in → business role → approved staff application."),
        ("Privileged administrator","Separate admin role → authorized change → audit evidence."),
        ("Application workload","Service identity → scoped API/data permission → logged operation.")],False)
    s=PROJECTS/"06-service-desk-workflows"
    for filename,title,note,steps in [
        ("incident-lifecycle.svg","Resolution requires verification","Proposed incident flow; no ServiceNow execution.",[
            ("Intake and investigation","Record scope, priority, owner, observations and next action."),
            ("Work or accepted handoff","Keep ownership and user updates. Reassignment is not resolution."),
            ("Verify the original task","Check the technical result and obtain user confirmation."),
            ("Resolve, then close under policy","If it recurs before closure, return to investigation. After closure, link a new incident.")]),
        ("request-fulfillment.svg","Approval before fulfillment","Proposed catalog flow; actual record links untested.",[
            ("Request and requested item","Record requested-for, scope, justification and due date."),
            ("Authorized approval","Reject or request clarification if approval is missing."),
            ("Scoped fulfillment task","Implement only approved access or software."),
            ("Verify all required tasks","Test allowed and prohibited actions before completion.")]),
        ("lab-boundaries.svg","Record workflow and real repair differ","All systems below are planned, not configured.",[
            ("ServiceNow learning instance","Ticket state, notes, approval and assignment evidence."),
            ("Owned endpoint or directory lab","Separate evidence is needed for an actual technical action."),
            ("Public portfolio","Only reviewed artifacts; scripted notes remain labeled.")]),
        ("vpn-decision-tree.svg","VPN connected: what to check next","Scripted diagnostic decisions; no live VPN test.",[
            ("Check name resolution","If the internal name fails, compare the approved DNS/profile settings."),
            ("If DNS succeeds, check transport","If the approved port fails, inspect the authorized network path."),
            ("If transport succeeds, check the app","Authentication and the user’s original task still need testing."),
            ("Route with evidence; verify recovery","Hand off the failed layer, observations and next action.")])
    ]:
        flow(s/"diagrams"/filename,title,note,steps)
    print("Generated 21 SVGs from retained evidence and labeled designs.")

if __name__=="__main__":
    main()
