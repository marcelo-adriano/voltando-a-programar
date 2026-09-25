#!/usr/bin/env bash
# Copia tryber/<repo> para <DESTINO>/<repo> (privado) e adiciona feedback.md.
# Uso: mirror.sh <repo>   — pode ser rodado de novo; pula o que já foi feito.
# DESTINO: conta que recebe as cópias (padrão: marcelo-adriano).
set -euo pipefail

NAME=$1
SRC=tryber/$NAME
DST=${DESTINO:-marcelo-adriano}/$NAME
DIR=$(cd "$(dirname "$0")" && pwd)
MIRROR=$DIR/mirrors/$NAME.git
DST_URL=https://github.com/$DST.git
mkdir -p "$DIR/mirrors" "$DIR/feedback"

echo "== $NAME"

# 1. clone --mirror
if [ ! -d "$MIRROR" ]; then
  git clone --quiet --mirror "https://github.com/$SRC.git" "$MIRROR"
else
  git -C "$MIRROR" remote update --prune >/dev/null
fi
DEFAULT=$(gh api "repos/$SRC" --jq .default_branch)

# 2. repositório privado na minha conta, com Actions desligado antes do push
#    (senão os workflows da Trybe rodariam em cada branch enviada)
if ! gh repo view "$DST" >/dev/null 2>&1; then
  gh repo create "$DST" --private --description "Cópia de $SRC" >/dev/null
fi
gh api -X PUT "repos/$DST/actions/permissions" -F enabled=false >/dev/null

# 3. push de branches e tags (refs/pull/* é recusado pelo GitHub).
#    A branch padrão vai por último para não sobrescrever o commit do feedback.md
#    numa segunda execução.
git -C "$MIRROR" push --quiet "$DST_URL" \
  "+refs/tags/*:refs/tags/*" \
  $(git -C "$MIRROR" for-each-ref --format='+%(refname):%(refname)' refs/heads \
      | grep -v "^+refs/heads/$DEFAULT:" || true)
REMOTE_DEFAULT=$(git ls-remote "$DST_URL" "refs/heads/$DEFAULT" | cut -f1)
if [ -z "$REMOTE_DEFAULT" ]; then
  git -C "$MIRROR" push --quiet "$DST_URL" "refs/heads/$DEFAULT:refs/heads/$DEFAULT"
fi
gh repo edit "$DST" --default-branch "$DEFAULT" >/dev/null

# 4. feedback.md na branch padrão
PRS=$(awk -F'\t' -v r="$NAME" '$1 == r {print $2}' "$DIR/prs.tsv" | tr '\n' ' ')
if [ -n "$PRS" ]; then
  # shellcheck disable=SC2086
  python3 "$DIR/gen_feedback.py" "$NAME" $PRS > "$DIR/feedback/$NAME.md"
  gh api "repos/$DST/contents/feedback.md?ref=$DEFAULT" > "$DIR/feedback/$NAME.existing.json" 2>/dev/null \
    || echo '{}' > "$DIR/feedback/$NAME.existing.json"
  RESULT=$(python3 - "$DIR/feedback/$NAME.md" "$DEFAULT" "$DIR/feedback/$NAME.existing.json" "$DIR/feedback/$NAME.json" <<'EOF'
import base64, json, sys
path, branch, existing_path, out_path = sys.argv[1:]
new = open(path, "rb").read()
existing = json.load(open(existing_path))
body = {"branch": branch, "content": base64.b64encode(new).decode()}
if existing.get("sha"):
    if base64.b64decode(existing["content"]) == new:
        print("igual"); sys.exit()
    body["sha"] = existing["sha"]
    title = "docs: atualiza feedback dos PRs originais"
else:
    title = "docs: adiciona feedback dos PRs originais"
body["message"] = (title + "\n\n"
    "Comentários e reviews dos meus PRs em tryber, copiados junto com o repositório.\n\n"
    "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
json.dump(body, open(out_path, "w"))
print("atualizado" if existing.get("sha") else "criado")
EOF
  )
  if [ "$RESULT" = igual ]; then
    echo "   feedback.md já está em dia"
  else
    gh api -X PUT "repos/$DST/contents/feedback.md" --input "$DIR/feedback/$NAME.json" >/dev/null
    echo "   feedback.md $RESULT (PRs: $PRS)"
  fi
else
  echo "   sem PRs meus, sem feedback.md"
fi

# 5. conferência: toda branch/tag da origem existe no destino com o mesmo commit
#    (exceto a branch padrão, que ganhou o commit do feedback.md).
#    O `|| true` evita que o pipefail derrube o script em repositórios que só têm a
#    branch padrão, onde o grep -v não devolve nenhuma linha.
LOCAL=$(git -C "$MIRROR" for-each-ref --format='%(objectname) %(refname)' refs/heads refs/tags \
          | { grep -v " refs/heads/$DEFAULT$" || true; } | sort)
REMOTE=$(git ls-remote --heads --tags "$DST_URL" | { grep -v '\^{}$' || true; } | tr '\t' ' ' \
          | { grep -v " refs/heads/$DEFAULT$" || true; } | sort)
MISSING=$(comm -23 <(echo "$LOCAL") <(echo "$REMOTE") | grep -c . || true)
N=$(echo "$LOCAL" | grep -c . || true)
if [ "$MISSING" -ne 0 ]; then
  echo "   ERRO: $MISSING de $N refs não batem no destino"
  exit 1
fi
echo "   OK: $N branches/tags + $DEFAULT conferidas"
