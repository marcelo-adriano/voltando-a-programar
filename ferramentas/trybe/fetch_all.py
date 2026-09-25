#!/usr/bin/env python3
"""Baixa (só leitura) os dados de todos os PRs listados em prs.tsv para prs.json.

Para cada PR: dados do PR, comentários, reviews, comentários de linha e arquivos alterados.
"""
import json
import os
import sys

from gen_feedback import api, OWNER

DIR = os.path.dirname(os.path.abspath(__file__))

rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(DIR, "prs.tsv")) if l.strip()]
out = []
for repo, number in rows:
    p = f"repos/{OWNER}/{repo}"
    out.append({
        "repo": repo,
        "number": int(number),
        "pr": api(f"{p}/pulls/{number}"),
        "issue_comments": api(f"{p}/issues/{number}/comments"),
        "reviews": api(f"{p}/pulls/{number}/reviews"),
        "review_comments": api(f"{p}/pulls/{number}/comments"),
        "files": api(f"{p}/pulls/{number}/files"),
    })
    print(repo, number, file=sys.stderr)
json.dump(out, open(os.path.join(DIR, "prs.json"), "w"))
