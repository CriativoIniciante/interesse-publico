#!/usr/bin/env bash
# Avisa quando commits não seguem a forma de CONTRIBUINDO.md, seção 4.
# Uso: checa_commits.sh <base_sha> <head_sha>. Nunca falha: aviso, não bloqueio.
set -uo pipefail
base="${1:?base sha}"; head="${2:?head sha}"
areas='carta|metodo|regras|fontes|coletor|descricao|analise|dossie|errata|boletim|manifesto|corrige'
avisos=0
while read -r sha; do
  [ -z "$sha" ] && continue
  titulo=$(git log -1 --format=%s "$sha")
  corpo=$(git log -1 --format=%b "$sha")
  problemas=()
  if ! [[ "$titulo" =~ ^($areas)(\([a-z0-9_-]+\))?:\  ]]; then
    problemas+=("título sem área ('<área>: ...')")
  fi
  if [ "${#titulo}" -gt 72 ]; then problemas+=("título com mais de 72 caracteres"); fi
  if ! grep -qE '^Camada: (0|1|2|3|codigo)$' <<<"$corpo"; then problemas+=("sem rodapé 'Camada:'"); fi
  if ! grep -qE '^Signed-off-by: ' <<<"$corpo"; then problemas+=("sem 'Signed-off-by' (git commit -s)"); fi
  if [ "${#problemas[@]}" -gt 0 ]; then
    avisos=$((avisos+1))
    echo "aviso ${sha:0:8}: $titulo"
    for p in "${problemas[@]}"; do echo "    - $p"; done
  fi
done < <(git rev-list --reverse "$base..$head")
if [ "$avisos" -eq 0 ]; then echo "ok: todos os commits seguem a forma"; else echo "$avisos commit(s) fora da forma; o mantenedor completa no merge"; fi
exit 0
