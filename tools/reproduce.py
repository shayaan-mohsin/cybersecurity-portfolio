"""Recreate published analysis artifacts without cloud credentials or network access."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def load_cloud():
    path = ROOT/"projects/04-aws-cloud-security-log-investigation/scripts/analyze_cloudtrail.py"
    spec = importlib.util.spec_from_file_location("cloud", path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

def cloud_index():
    return {
        "purpose": "Generated service/action index, not executable rules. The analyzer does not load this file.",
        "source": "../scripts/analyze_cloudtrail.py",
        "actions": [{"event_name": name, "event_source": service}
                    for name, service in sorted(load_cloud().EXPECTED.items())],
        "root_identity_rule": "Also reviews Root identity on events that reach the successful-action logic.",
        "limitations": "See cloudtrail-detection-catalog.md for conditions, outcomes and unsupported behavior."
    }

def main():
    h="projects/01-nist-csf-risk-assessment"
    k="projects/02-cisa-kev-vulnerability-prioritization"
    a="projects/04-aws-cloud-security-log-investigation"
    commands=[
        [f"{h}/scripts/analyze_hhs_breaches.py",f"{h}/data/hhs-ocr-breach-sample-2026-05-16.csv","--as-of","2026-05-16","--output-dir",f"{h}/outputs"],
        [f"{k}/scripts/analyze_kev.py",f"{k}/data/known_exploited_vulnerabilities-2026-05-16.csv","--as-of","2026-05-16","--output-dir",f"{k}/outputs"],
        [f"{a}/scripts/analyze_cloudtrail.py",f"{a}/data/sample-cloudtrail-events.json","--output-dir",f"{a}/outputs"],
        ["tools/generate_portfolio_visuals.py"]
    ]
    for command in commands:
        subprocess.run([sys.executable,*command],cwd=ROOT,check=True)
    (ROOT/a/"detections/cloudtrail-detection-rules.json").write_text(json.dumps(cloud_index(),indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
