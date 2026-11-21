#!/usr/bin/env python3
"""Validate Ultimate v3.3 ALL ACTIVE source references, not runtime behavior."""
from pathlib import Path
import json, re

root=Path(__file__).resolve().parents[1]
s=(root/"modules/Infiniti-All-In-One-Extended.sgmodule").read_text(encoding="utf-8")
inv=json.loads((root/"research/all-script-inventory.json").read_text(encoding="utf-8"))
expected={x["url"] for x in inv["scripts"]}
assert len(expected)==39
assert not re.search(r"(?im)^\s*(?:ca-p12|ca-passphrase)\s*=",s), "CA private secrets"
sections=re.findall(r"(?m)^\[([^\]]+)\]\s*$",s)
assert sections==["Rule","Header Rewrite","Url Rewrite","Map Local","Script","MITM"],sections

def active(name):
    body=s.split(f"[{name}]\n",1)[1].split("\n[",1)[0]
    return [x.strip() for x in body.splitlines() if x.strip() and not x.lstrip().startswith("#")]

for name,count in {"Rule":5,"Header Rewrite":2,"Url Rewrite":5,"Map Local":1,"Script":39,"MITM":1}.items():
    assert len(active(name))==count,(name,len(active(name)),count)

urls=[]
names=[]
for line in active("Script"):
    p=re.search(r"script-path=(https?://[^,\s]+)",line)
    assert p and "type=" in line and ("pattern=" in line or "type=cron" in line),line
    urls.append(p.group(1));names.append(line.split("=",1)[0].strip())
assert len(set(urls))==39 and set(urls)==expected
assert len(set(names))==39
hostline=active("MITM")[0]
assert hostline.startswith("hostname = %APPEND% ") and hostline.count("%APPEND%")==1
hosts=[x.strip() for x in hostline.split("=",1)[1].replace("%APPEND%","",1).split(",")]
assert len(hosts)==len(set(hosts))==26
print("PASS: 39 unique active script URLs, six config sections and 26 MITM host patterns")
print("WARNING: 20 sources previously 404, overlapping API handlers; runtime NOT verified")
