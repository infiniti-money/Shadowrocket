#!/usr/bin/env python3
"""Verify remote rule lists without executing arbitrary remote JavaScript.

CI checks HTTP status, UTF-8 decoding, size, and rule syntax. The network and
upstream hosts may fail temporarily. This is not an iOS runtime validator.
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "rules" / "upstreams.json"
ALLOWED = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "IP-CIDR", "IP-CIDR6", "USER-AGENT", "PROCESS-NAME", "PROCESS-PATH", "URL-REGEX", "GEOIP", "AND", "OR", "NOT"}
MAX_BYTES = 2_500_000


def validate_content(data: bytes, url: str) -> tuple[int, int]:
    if not data or len(data) > MAX_BYTES:
        raise ValueError(f"Empty or oversized list ({len(data)} bytes)")
    content = data.decode("utf-8-sig")
    checked, invalid = 0, []
    for line_no, line in enumerate(content.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith(("#", ";", "//")):
            continue
        kind = s.split(",", 1)[0].strip()
        if kind not in ALLOWED or "," not in s:
            invalid.append(f"{line_no}: {s[:100]}")
        checked += 1
    if invalid:
        raise ValueError(f"{url}: unexpected list syntax: {'; '.join(invalid[:5])}")
    if not checked:
        raise ValueError("No active rules found")
    return checked, len(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="validate manifest and references only")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    refs = set()
    failed = False
    for entry in manifest["rules"]:
        url = entry["url"]
        if not url.startswith("https://raw.githubusercontent.com/"):
            print(f"ERROR non-allowlisted remote: {url}")
            failed = True
            continue
        if url in refs:
            print(f"ERROR duplicate source: {url}")
            failed = True
        refs.add(url)
        module = ROOT / entry["module"]
        if not module.is_file() or url not in module.read_text(encoding="utf-8"):
            print(f"ERROR broken reference {entry['id']} in {module}")
            failed = True
            continue
        if args.offline:
            print(f"OK offline {entry['id']}")
            continue
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Infiniti-Shadowrocket-UpstreamCheck/1.1"})
            with urllib.request.urlopen(request, timeout=20) as response:
                payload = response.read(MAX_BYTES + 1)
            count, size = validate_content(payload, url)
            print(f"OK {entry['id']}: {count} rules / {size} bytes")
        except (urllib.error.URLError, UnicodeError, ValueError, TimeoutError) as exc:
            print(f"ERROR {entry['id']}: {exc}")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
