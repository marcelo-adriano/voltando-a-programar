#!/usr/bin/env bash
# Gera as listas de entrada dos outros scripts (só leitura no GitHub):
#   repos.txt — repositórios da tryber com TURMA no nome
#   prs.tsv   — PRs de AUTOR nesses repositórios (repositório<TAB>número)
# TURMA (padrão: sd-015-a) e AUTOR (padrão: marcelo-adriano) podem ser trocados por variável de ambiente.
set -euo pipefail

TURMA=${TURMA:-sd-015-a}
AUTOR=${AUTOR:-marcelo-adriano}
DIR=$(cd "$(dirname "$0")" && pwd)

gh repo list tryber --limit 20000 --json name \
  --jq ".[] | select(.name | contains(\"$TURMA\")) | .name" \
  | sort > "$DIR/repos.txt"

# Só os PRs em repositórios da turma (PRs em outros repositórios da tryber ficam de fora)
gh search prs --author "$AUTOR" --owner tryber --limit 1000 --json repository,number \
  --jq '.[] | "\(.repository.name)\t\(.number)"' \
  | awk -F'\t' 'NR == FNR { turma[$1] = 1; next } $1 in turma' "$DIR/repos.txt" - \
  | sort -t$'\t' -k1,1 -k2,2n > "$DIR/prs.tsv"

echo "$(wc -l < "$DIR/repos.txt") repositórios em repos.txt"
echo "$(wc -l < "$DIR/prs.tsv") PRs em $(cut -f1 "$DIR/prs.tsv" | sort -u | wc -l) repositórios em prs.tsv"
