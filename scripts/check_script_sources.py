#!/usr/bin/env python3
"""Inventory script-path URL availability. Never downloads to disk or runs JavaScript.

Run: python3 scripts/check_script_sources.py [--online] [--json]
Without --online: prints inventory summary. Online probe uses HTTP HEAD, then
GET with Range for endpoints rejecting HEAD. Availability != compatibility.
"""
import argparse
import json
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "research/all-script-inventory.json"


def probe(url):
    if not url.startswith(("https://raw.githubusercontent.com/", "https://github.com/")):
        return "unsupported-host"
    for method in ("HEAD", "GET"):
        try:
            headers = {"User-Agent": "Infiniti-Shadowrocket-SourceAudit/1.0"}
            if method == "GET":
                headers["Range"] = "bytes=0-0"
            req = urllib.request.Request(url, method=method, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as response:
                status = response.status
                content_type = response.headers.get("Content-Type", "")
                if status in (200, 206):
                    return f"http-{status} ({content_type.split(';')[0]})"
                return f"http-{status}"
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in (403, 405):
                continue
            return f"http-{exc.code}"
        except (urllib.error.URLError, TimeoutError) as exc:
            return f"network-error ({type(exc).__name__})"
    return "not-verified"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    catalog = json.loads(INVENTORY.read_text(encoding="utf-8"))
    results = []
    for entry in catalog["scripts"]:
        url = entry["url"]
        results.append({
            "name": ", ".join(entry["names"]),
            "url": url,
            "status": probe(url) if args.online else entry["availability"]
        })
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(f"Scripts in inventory: {len(results)}")
        for item in results:
            print(f"{item['status']:38} {item['name'][:24]:24} {item['url']}")
        print("Summary:", dict(Counter(item["status"] for item in results)))
        print("Availability alone does not establish JS safety or Premium functionality.")
    # Reporting mode: broken external sources do not break the safe module CI.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
