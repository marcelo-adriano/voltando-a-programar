#!/usr/bin/env bash
# Roda mirror.sh em todos os repositórios, sem parar no primeiro erro.
DIR=$(cd "$(dirname "$0")" && pwd)
: > "$DIR/failed.txt"
while read -r repo; do
  "$DIR/mirror.sh" "$repo" 2>&1 || echo "$repo" >> "$DIR/failed.txt"
done < "$DIR/repos.txt"
echo "== FIM. Falhas: $(wc -l < "$DIR/failed.txt")"
cat "$DIR/failed.txt"
