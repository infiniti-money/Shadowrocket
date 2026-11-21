#!/usr/bin/env python3
"""Check v3.4 recovery module structure; never executes remote scripts."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
content = (ROOT / "modules/Infiniti-All-In-One-Extended.sgmodule").read_text(encoding="utf-8")
catalog = json.loads((ROOT / "research/all-script-inventory.json").read_text(encoding="utf-8"))
expected = {item["url"] for item in catalog["scripts"]}
assert len(expected) == len(catalog["scripts"]) == 39
assert not re.search(r"(?im)^\s*(?:ca-p12|ca-passphrase)\s*=", content)
sections = re.findall(r"(?m)^\[([^\]]+)\]\s*$", content)
assert sections == ["Rule","Header Rewrite","Url Rewrite","Script","MITM"], sections

def active(section):
    block = content.split("[" + section + "]\n", 1)[1].split("\n[", 1)[0]
    return [s.strip() for s in block.splitlines()
            if s.strip() and not s.strip().startswith("#")]

for name,count in {"Rule":3, "Header Rewrite":1, "Url Rewrite":3, "Script":2, "MITM":1}.items():
    assert len(active(name))==count, (name,len(active(name)),count)

active_urls=[]
for line in active("Script"):
    match=re.search(r"script-path=(https?://[^,\s]+)",line)
    assert match and "type=" in line and "pattern=" in line, line
    active_urls.append(match.group(1))
assert len(set(active_urls))==2
assert all("app2smile/rules" in u for u in active_urls)
archived = re.findall(r"(?m)^# Source: (https?://\S+)$", content)
assert len(archived)==37 and len(set(archived))==37
assert set(active_urls).isdisjoint(archived)
assert set(active_urls+archived)==expected
assert all(item["url"] not in active_urls
           for item in catalog["scripts"]
           if item.get("availability")=="source-previously-404")
mitm=active("MITM")[0]
assert mitm.count("%APPEND%")==1 and mitm.startswith("hostname = %APPEND% ")
assert "api.revenuecat.com" not in mitm and "buy.itunes.apple.com" not in mitm
print("PASS: recovery v3.4 retains 39 distinct URLs (2 active, 37 archived)")
print("PASS: 3 filter rules, 1 header, 3 URL rewrites, MITM without shared purchases")
print("WARNING: Shadowrocket runtime and app functionality remain unverified")
