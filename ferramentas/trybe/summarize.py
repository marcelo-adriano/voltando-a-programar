#!/usr/bin/env python3
"""Resume prs.json: última avaliação da Trybe, requisitos que faltaram, lint e comentários.

Grava summary.json e imprime um resumo por PR.
"""
import json, os, re, sys

DIR = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(DIR, "prs.json")))

def parse_eval(body):
    if "Resultado do projeto" not in body: return None
    g = lambda k: (re.search(rf"^{k} \| (.+?)\s*$", body, re.M) or [None, None])[1]
    reqs = re.findall(r"^(.+?) \| :(heavy_check_mark|heavy_multiplication_x):", body, re.M)
    return {
        "desempenho": g("Desempenho"), "criterio": g("Critério de Avaliação"),
        "obrig": g("Percentual de cumprimento de requisitos obrigatórios"),
        "total": g("Percentual de cumprimento de requisitos totais"),
        "ok": [r for r, s in reqs if s == "heavy_check_mark"],
        "fail": [r for r, s in reqs if s != "heavy_check_mark"],
    }

summary = []
for e in d:
    pr = e["pr"]
    evals = [(c["created_at"], parse_eval(c["body"])) for c in e["issue_comments"]]
    evals = [(t, v) for t, v in evals if v]
    lints = [c for c in e["issue_comments"] if c["user"]["login"] == "github-actions[bot]"]
    humans = [c for c in e["issue_comments"]
              if not c["user"]["login"].endswith("[bot]") and c["user"]["login"] != "trybe-tech-ops"]
    s = {
        "repo": e["repo"], "n": e["number"], "title": pr["title"],
        "state": "merged" if pr["merged_at"] else pr["state"],
        "created": pr["created_at"][:10], "updated": pr["updated_at"][:10],
        "head": pr["head"]["ref"], "base": pr["base"]["ref"],
        "commits": pr["commits"], "add": pr["additions"], "del": pr["deletions"], "files": pr["changed_files"],
        "n_evals": len(evals),
        "first_eval": evals[0][1] if evals else None, "first_eval_at": evals[0][0][:10] if evals else None,
        "last_eval": evals[-1][1] if evals else None, "last_eval_at": evals[-1][0][:10] if evals else None,
        "last_lint": lints[-1]["body"].strip()[:400] if lints else None,
        "humans": [(c["user"]["login"], c["body"][:300]) for c in humans],
        "reviews": [(r["user"]["login"], r["state"], (r["body"] or "")[:200]) for r in e["reviews"]],
        "review_comments": [(c["user"]["login"], c["path"], c["body"][:300]) for c in e["review_comments"]],
        "file_list": [(f["filename"], f["additions"], f["deletions"]) for f in e["files"]],
    }
    summary.append(s)
json.dump(summary, open(os.path.join(DIR, "summary.json"), "w"), ensure_ascii=False, indent=1)

for s in summary:
    le, fe = s["last_eval"], s["first_eval"]
    print(f"\n### {s['repo']} #{s['n']} [{s['state']}] {s['title']}  ({s['created']}→{s['updated']}, {s['commits']} commits, +{s['add']}/-{s['del']} em {s['files']} arquivos)")
    if le:
        print(f"  avaliação final {s['last_eval_at']}: {le['desempenho']} | {le['criterio']} | obrig {le['obrig']} | total {le['total']} | {len(le['ok'])}/{len(le['ok'])+len(le['fail'])} req  (avaliações: {s['n_evals']}, primeira: obrig {fe['obrig']} total {fe['total']})")
        for r in le["fail"]: print("    ✗", r[:140])
    else:
        print("  sem avaliação automática")
    if s["last_lint"]: print("  lint final:", s["last_lint"].replace("\n", " ")[:250])
    for h in s["humans"]: print("  comentário:", h[0], "-", h[1].replace("\n", " ")[:200])
