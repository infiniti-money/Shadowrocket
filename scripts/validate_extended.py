#!/usr/bin/env python3
"""Structural checks for one-URL Ultimate v3.2, not a runtime/security certification."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
content = (root / "modules/Infiniti-All-In-One-Extended.sgmodule").read_text(encoding="utf-8")
inventory = json.loads((root / "research/all-script-inventory.json").read_text(encoding="utf-8"))
expected = {item["url"] for item in inventory["scripts"]}
assert len(expected) == len(inventory["scripts"]) == 39
assert not re.search(r"(?im)^\s*(?:ca-p12|ca-passphrase)\s*=", content), "Private CA secret detected"
sections = re.findall(r"(?m)^\[([^\]]+)\]\s*$", content)
assert sections == ["Rule","Header Rewrite","Url Rewrite","Map Local","Script","MITM"], sections

def section(name):
    s = content.split(f"[{name}]\n", 1)[1].split("\n[", 1)[0]
    return [line.strip() for line in s.splitlines() if line.strip() and not line.strip().startswith("#")]

counts = {"Rule":5, "Header Rewrite":2,"Url Rewrite":5,"Map Local":1,"Script":7,"MITM":1}
for name,count in counts.items():
    assert len(section(name)) == count, (name,len(section(name)),count)

active = [re.search(r"script-path=(https?://[^,\s]+)", line).group(1) for line in section("Script")]
commented = re.findall(r"(?m)^# script-path=(https?://[^,\s]+)", content)
assert len(active)==7 and len(commented)==32
assert set(active).isdisjoint(commented)
assert len(set(active+commented))==39 and set(active+commented)==expected
previously_404 = {item["url"] for item in inventory["scripts"]
                  if item.get("availability")=="source-previously-404"}
assert not previously_404.intersection(active), "Previously 404 script unexpectedly enabled"
assert previously_404.issubset(commented), "Missing broken URL archive entry"
mitm=section("MITM")[0]
assert mitm.startswith("hostname = %APPEND% ") and mitm.count("%APPEND%")==1
hosts = [v.strip() for v in mitm.split("=",1)[1].replace("%APPEND%","",1).split(",")]
assert len(hosts)==21 and len(hosts)==len(set(hosts))
print("PASS: Ultimate v3.2: 5 rules, 5 URL rewrites, 2 header rewrites, 1 map local")
print("PASS: 39 unique JS URLs (7 active and 32 commented), 21 MITM host patterns")
print("WARNING: network availability, script behavior and TLS trust NOT verified")
