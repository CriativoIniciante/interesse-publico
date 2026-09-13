#!/usr/bin/env bash
# Recusa modificação ou remoção em pastas que só aceitam acréscimo.
# Uso: protege_camadas.sh <base_sha> <head_sha>
# Regra: CONTRIBUINDO.md, seções 3 e 4 (item 6).
set -euo pipefail
base="${1:?base sha}"; head="${2:?head sha}"
prefixo="historia-brasil"
protegidas=(evidencia manifestos carimbos dossies erratas)
args=()
for p in "${protegidas[@]}"; do args+=("$prefixo/$p"); done

# D = removido, M = modificado, R = renomeado, T = tipo alterado. Acréscimo (A) é permitido.
violacoes=$(git diff --name-status --diff-filter=DMRT "$base" "$head" -- "${args[@]}" || true)
if [ -n "$violacoes" ]; then
  echo "Recusado: as pastas ${protegidas[*]} só aceitam acréscimo."
  echo "Arquivos modificados, removidos ou renomeados:"
  echo "$violacoes" | sed 's/^/  /'
  echo "Correção se faz com arquivo novo marcado como corrigido, nunca alterando o original."
  exit 1
fi
echo "ok: nenhuma modificação ou remoção em ${protegidas[*]}"
