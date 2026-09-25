#!/usr/bin/env python3
"""Mostra as linhas adicionadas nos PRs de um repositório. Uso: show.py <repo> [pr] [--max N]"""
import json, os, sys

DIR = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
mx = 400
if "--max" in args:
    i = args.index("--max"); mx = int(args[i+1]); del args[i:i+2]
repo = args[0]
prs = [int(a) for a in args[1:]]
skip = ("package-lock.json", ".bson", ".png", ".jpg", ".xlsx", "talker.json")
for e in json.load(open(os.path.join(DIR, "prs.json"))):
    if not e["repo"].endswith(repo) or (prs and e["number"] not in prs): continue
    print(f"################ {repo} #{e['number']}")
    for f in e["files"]:
        if f["filename"].endswith(skip): continue
        patch = f.get("patch") or "(sem patch)"
        lines = [l[1:] for l in patch.splitlines() if l.startswith("+")] or patch.splitlines()
        print(f"======= {f['filename']} (+{f['additions']}/-{f['deletions']})")
        for l in lines[:mx]: print(l)
        if len(lines) > mx: print(f"... (+{len(lines)-mx} linhas)")
