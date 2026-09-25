#!/usr/bin/env python3
"""Gera feedback.md com comentários e reviews dos PRs de um repositório da tryber.

Uso: gen_feedback.py <repo> <pr> [<pr> ...]  (escreve o markdown no stdout)
AUTOR: quem abriu os PRs, só para o texto de abertura (padrão: marcelo-adriano).
"""
import json
import os
import subprocess
import sys

OWNER = "tryber"
AUTOR = os.environ.get("AUTOR", "marcelo-adriano")


def get(path):
    out = subprocess.run(
        ["gh", "api", path], check=True, capture_output=True, text=True,
    ).stdout
    return json.loads(out)


def api(path):
    data = get(path)
    if not isinstance(data, list):
        return data
    # listas vêm paginadas; busca as páginas seguintes de 100 em 100
    items, page = [], 1
    while True:
        batch = get(f"{path}?per_page=100&page={page}")
        items += batch
        if len(batch) < 100:
            return items
        page += 1


def when(ts):
    return ts.replace("T", " ").replace("Z", " UTC") if ts else ""


def user(obj):
    return (obj.get("user") or {}).get("login", "ghost")


def quote(body):
    """Põe o comentário numa citação, para os títulos dele não se misturarem com os do arquivo."""
    body = (body or "").strip() or "_(vazio)_"
    return "\n".join("> " + line if line else ">" for line in body.splitlines())


def quote_hunk(hunk):
    lines = hunk.splitlines()[-8:]  # só o final do trecho, onde está a linha comentada
    return "```diff\n" + "\n".join(lines) + "\n```"


def pr_section(repo, number):
    pr = api(f"repos/{OWNER}/{repo}/pulls/{number}")
    issue_comments = api(f"repos/{OWNER}/{repo}/issues/{number}/comments")
    reviews = api(f"repos/{OWNER}/{repo}/pulls/{number}/reviews")
    review_comments = api(f"repos/{OWNER}/{repo}/pulls/{number}/comments")

    state = "merged" if pr.get("merged_at") else pr["state"]
    out = [
        f"## PR #{number}: {pr['title']}",
        "",
        f"- Link: {pr['html_url']}",
        f"- Branch: `{pr['head']['ref']}` → `{pr['base']['ref']}`",
        f"- Estado: {state}",
        f"- Aberto em: {when(pr['created_at'])}",
    ]
    if pr.get("merged_at"):
        out.append(f"- Mergeado em: {when(pr['merged_at'])}")
    elif pr.get("closed_at"):
        out.append(f"- Fechado em: {when(pr['closed_at'])}")
    out.append("")

    out += ["### Comentários", ""]
    if not issue_comments:
        out += ["_Nenhum comentário._", ""]
    for c in issue_comments:
        out += [f"#### {user(c)} em {when(c['created_at'])}", "", quote(c["body"]), ""]

    # comentários de linha agrupados pela review a que pertencem
    by_review = {}
    for c in review_comments:
        by_review.setdefault(c.get("pull_request_review_id"), []).append(c)

    out += ["### Reviews", ""]
    if not reviews:
        out += ["_Nenhuma review._", ""]
    for r in reviews:
        out += [f"#### {user(r)} — {r['state']} em {when(r.get('submitted_at'))}", ""]
        if r.get("body"):
            out += [quote(r["body"]), ""]
        for c in by_review.pop(r["id"], []):
            line = c.get("line") or c.get("original_line") or ""
            out += [
                f"**`{c['path']}`{':' + str(line) if line else ''}** — {user(c)} em {when(c['created_at'])}",
                "",
                quote_hunk(c.get("diff_hunk") or ""),
                "",
                quote(c["body"]),
                "",
            ]

    orphans = [c for cs in by_review.values() for c in cs]
    if orphans:
        out += ["### Outros comentários de linha", ""]
        for c in orphans:
            line = c.get("line") or c.get("original_line") or ""
            out += [
                f"**`{c['path']}`{':' + str(line) if line else ''}** — {user(c)} em {when(c['created_at'])}",
                "",
                quote_hunk(c.get("diff_hunk") or ""),
                "",
                quote(c["body"]),
                "",
            ]
    return "\n".join(out)


def main():
    repo, prs = sys.argv[1], sys.argv[2:]
    parts = [
        f"# Feedback dos meus PRs em {OWNER}/{repo}",
        "",
        "Comentários, reviews e comentários de linha dos PRs abertos por "
        f"{AUTOR} no repositório original, salvos na cópia.",
        "",
    ]
    for n in prs:
        parts += [pr_section(repo, n), "---", ""]
    sys.stdout.write("\n".join(parts).rstrip("-\n") + "\n")


if __name__ == "__main__":
    main()
