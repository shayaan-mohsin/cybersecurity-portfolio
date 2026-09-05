"""
Redact sensitive identifiers from CloudTrail JSON before public sharing.

This helper is intentionally conservative. It replaces common account-specific
values while preserving enough structure for investigation writeups and parser
testing.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ACCOUNT_ID_RE = re.compile(r"\b\d{12}\b")
ACCESS_KEY_RE = re.compile(r"\b(AKIA|ASIA)[A-Z0-9]{16}\b")
IPV4_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

SENSITIVE_KEYS = {
    "accessKeyId",
    "principalId",
    "accountId",
    "sourceIPAddress",
    "userAgent",
    "arn",
    "bucketName",
    "groupId",
    "stackId",
    "sessionName",
}


def redact_string(value: str) -> str:
    value = ACCOUNT_ID_RE.sub("111122223333", value)
    value = ACCESS_KEY_RE.sub("AKIAEXAMPLE000000000", value)
    value = IPV4_RE.sub("203.0.113.10", value)
    value = re.sub(r"arn:aws:iam::111122223333:user/[A-Za-z0-9+=,.@_-]+", "arn:aws:iam::111122223333:user/lab-user", value)
    value = re.sub(r"arn:aws:s3:::[A-Za-z0-9.\-_]+", "arn:aws:s3:::example-lab-bucket", value)
    value = re.sub(r"\bsg-[a-f0-9]{8,17}\b", "sg-0123456789abcdef0", value)
    return value


def redact(value: Any, key_name: str | None = None) -> Any:
    if isinstance(value, dict):
        return {key: redact(item, key) for key, item in value.items()}
    if isinstance(value, list):
        return [redact(item, key_name) for item in value]
    if isinstance(value, str):
        if key_name in SENSITIVE_KEYS:
            if key_name == "sourceIPAddress":
                return "203.0.113.10"
            if key_name == "userAgent":
                return "redacted-user-agent"
            if key_name == "bucketName":
                return "example-lab-bucket"
            if key_name == "groupId":
                return "sg-0123456789abcdef0"
            if key_name == "accountId":
                return "111122223333"
            if key_name == "accessKeyId":
                return "AKIAEXAMPLE000000000"
        return redact_string(value)
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Sanitize CloudTrail JSON for public-safe sharing.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    with args.input.open(encoding="utf-8-sig") as handle:
        payload = json.load(handle)

    sanitized = redact(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(sanitized, handle, indent=2)
        handle.write("\n")

    print(f"Sanitized CloudTrail JSON written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
