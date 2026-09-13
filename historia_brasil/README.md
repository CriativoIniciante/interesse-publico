# Arquivo vivo da história do Brasil

Projeto para um sistema que se alimenta e se atualiza sozinho para guardar o registro público do Brasil: o acervo digital gratuito da Biblioteca Nacional para trás, e as notícias dos grandes veículos e dos jornalistas independentes para frente, todo dia.

Estado: fase 0, proposta de método. Nenhum coletor escrito ainda.

## Arquivos

- `CARTA.md`: carta de princípios. O que o sistema promete, em 15 itens. Manda quando conflitar com o método.
- `METODO.md`: método proposto. Fontes, arquitetura em três camadas (evidência, descrição, interpretação), prova de integridade, protocolo para indício de crime ou distorção, riscos legais, ferramentas, custo e roteiro por fases.
- `CONTRIBUINDO.md`: sempre online e aberto. O que fica público e onde, quem pode alterar cada camada, regras de commit, prazos, verificações automáticas, licenças propostas e o que só o dono do repositório pode configurar.
- `fontes.yaml`: lista inicial de fontes com feed, tipo e resultado do teste de acesso.
- `scripts/valida_fontes.py`: valida `fontes.yaml`. `scripts/protege_camadas.sh`: recusa modificação ou remoção nas pastas só de acréscimo. `scripts/checa_commits.sh`: avisa sobre commits fora da forma.
- `.github/workflows/historia-brasil.yml` (na raiz do repositório): roda as três verificações e a varredura de segredos em todo pull request. Modelos de pull request e de issue (contestação, nova fonte, erro) em `.github/`.

## Em uma frase

O sistema coleta, preserva com hash e carimbo de tempo, revisita, compara e aponta sozinho; pessoas identificadas decidem, revisam, ouvem o acusado, assinam e comunicam.

## Próximos passos

1. Ler e ajustar a carta. As decisões que são do autor estão na seção 10 do método.
2. Configurar o repositório para ficar aberto de verdade: seção 9 de `CONTRIBUINDO.md` (branch `main` protegido, licenças, Pages, espelho, mantenedores).
3. Enviar o pedido formal à Biblioteca Nacional, seção 2.3 do método.
4. Fase 1: coletor de feeds com WARC, hash, manifesto diário, carimbo OpenTimestamps e cópia no Internet Archive.
