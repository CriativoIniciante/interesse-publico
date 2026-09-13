# Sempre online e aberto: regras para contribuir e para novos commits

O acervo fica público, online e aberto a melhorias de qualquer pessoa. Abertura sem regras vira ruído; regras sem abertura viram um arquivo privado. Este texto define as duas coisas. A carta (`CARTA.md`) manda quando conflitar com ele.

## 1. O que fica sempre online

| O que | Onde | Quem pode ver |
|---|---|---|
| Código, carta, método, regras, lista de fontes | este repositório | todos |
| Manifestos diários de hashes e carimbos `.ots` | `manifestos/` e `carimbos/` neste repositório | todos |
| Metadados, versões, diffs, entidades | índice público (Datasette) e JSONL mensal no repositório ou em release | todos |
| Análises, dossiês, contestações, erratas | `analises/`, `dossies/`, `erratas/` neste repositório e no portal | todos |
| Boletim diário (coletado, mudado, falhado) | `boletins/` e portal | todos |
| Evidência bruta (WARC, imagens) | armazenamento de objetos, fora do git | hashes públicos; acesso ao conteúdo integral para pesquisa, sob pedido, por causa do direito autoral |

Regras de permanência:

- Nada sai do ar por decisão de uma pessoa. Encerrar ou pausar o projeto exige aviso público com 90 dias de antecedência, no repositório e no portal, e entrega completa dos dados a pelo menos um espelho independente antes do desligamento.
- O repositório é espelhado automaticamente em pelo menos um serviço independente do GitHub (Codeberg ou GitLab) e registrado no Software Heritage, que arquiva repositórios públicos de graça e para sempre.
- Toda release mensal leva o manifesto do mês e nunca é apagada.
- Se o portal cair, o repositório continua legível: os documentos são Markdown e os dados são JSONL e CSV, sem dependência de programa para abrir.

## 2. Quem pode fazer o quê

| Papel | Pode |
|---|---|
| Qualquer pessoa | abrir issue de contestação, de nova fonte ou de erro; abrir pull request; comentar |
| Coletor automático | acrescentar em `evidencia/`, `manifestos/`, `carimbos/`, `boletins/`. Só acrescentar |
| Mantenedor | revisar e fundir pull requests; assinar commits de merge; responder contestações |
| Dois mantenedores com convicções declaradas diferentes | aprovar mudanças na camada 3 e publicar dossiês |
| Todos os mantenedores | assinar mudanças na carta |

Mantenedores são listados no fim deste arquivo, com declaração pública de vieses e conflitos de interesse. Pessoa que não declarou não revisa a camada 3.

## 3. O que cada camada aceita

| Camada | Pasta | Quem altera | Revisão |
|---|---|---|---|
| 1. Evidência | `evidencia/`, `manifestos/`, `carimbos/` | só o coletor | nenhuma; humanos não fazem commit aqui; a verificação automática bloqueia qualquer modificação ou remoção |
| 2. Descrição | `descricao/`, `fontes.yaml` | qualquer pessoa por pull request | um mantenedor |
| 3. Interpretação | `analises/`, `dossies/` | qualquer pessoa por pull request | dois mantenedores, um que não escreveu, convicções diferentes; indício de ilícito segue o protocolo 5.2 do método |
| 0. Governo | `CARTA.md`, `CONTRIBUINDO.md`, `METODO.md` | qualquer pessoa por pull request | carta: 14 dias abertos a comentário e assinatura de todos os mantenedores; método e regras: um mantenedor, com 7 dias abertos |
| Código | `coletores/`, `scripts/` | qualquer pessoa por pull request | um mantenedor; mudança em coletor aparece no boletim do dia seguinte |

Correção de erro em qualquer camada é commit novo com a marca `corrige:` no título. O registro errado permanece acessível no histórico e, quando publicado, ganha a marca de corrigido ou retratado na própria página.

## 4. Regras de commit

1. Um branch por mudança. Nada é commitado direto no branch principal.
2. Mensagem em português, com esta forma:

```
<área>: <o que muda, até 72 caracteres>

<por quê, em frases curtas, com link para a issue ou para a evidência>

Camada: 0 | 1 | 2 | 3 | codigo
Refs: #<issue>, <hash de evidência>, <URL>
Signed-off-by: Nome <email>
```

   Áreas: `carta`, `metodo`, `regras`, `fontes`, `coletor`, `descricao`, `analise`, `dossie`, `errata`, `boletim`, `manifesto`, `corrige`.

3. `Signed-off-by` é o certificado de origem do desenvolvedor (DCO, `git commit -s`): quem assina afirma que tem o direito de contribuir aquele conteúdo sob a licença do projeto. Substitui contrato de cessão.
4. Commit de merge é sempre assinado criptograficamente pelo mantenedor (GPG ou Sigstore). Assinatura do autor é recomendada, não exigida de quem contribui de fora.
5. Sem reescrita de história no branch principal: sem force push, sem rebase de commit publicado, sem squash que apague autoria. Erro se corrige com commit novo.
6. Sem remoção em `evidencia/`, `manifestos/`, `carimbos/`, `dossies/`, `erratas/`. A verificação automática recusa.
7. Sem segredos. Chaves de API, credenciais e tokens ficam nos segredos do CI. A verificação automática varre cada pull request.
8. Sem dado pessoal de pessoa privada além do que já está na fonte pública citada.
9. Dado gerado por programa vem com o programa: o script que gerou o arquivo está no mesmo commit ou é referenciado pelo hash do commit que o contém. Saída de modelo de linguagem traz modelo, versão e hash do prompt no cabeçalho do arquivo.
10. Mudança em `fontes.yaml` traz justificativa pelos critérios da seção 2.1 do método e o resultado do teste de acesso, no campo `teste`.
11. Todo pull request preenche o modelo em `.github/PULL_REQUEST_TEMPLATE.md`.

## 5. Prazos

| Evento | Prazo |
|---|---|
| Pull request aberto | um mantenedor responde em 14 dias |
| Contestação aberta | resposta inicial em 7 dias, decisão fundamentada em 30 dias |
| Mudança na carta | 14 dias abertos a comentário antes da fusão |
| Direito de resposta antes de dossiê | prazo dado por escrito, nunca menor que 7 dias |
| Discordância entre mantenedores | registrada no pull request; decisão por maioria; a posição minoritária fica registrada no dossiê ou na análise |

## 6. Verificações automáticas

Rodam em todo pull request e push que toque `historia-brasil/`. Estão em `.github/workflows/historia-brasil.yml`.

| Verificação | Efeito |
|---|---|
| `fontes.yaml` válido: campos obrigatórios, ids únicos, `verificado` booleano, `tipo` na lista | bloqueia |
| Modificação ou remoção em `evidencia/`, `manifestos/`, `carimbos/`, `dossies/`, `erratas/` | bloqueia |
| Rodapé `Camada:` nos commits | avisa; o mantenedor completa no merge |
| Varredura de segredos | bloqueia |

O que o CI não faz: julgar conteúdo. Isso é trabalho de gente, pelas regras da seção 3.

## 7. Licenças (proposta, pendente de decisão do autor)

| Conteúdo | Licença proposta | Por quê |
|---|---|---|
| Código | AGPL-3.0 | quem rodar uma versão modificada como serviço tem de abrir o código; protege a abertura do acervo |
| Carta, método, regras, análises, dossiês | CC BY-SA 4.0 | livre para copiar e derivar, desde que aberto e com crédito |
| Metadados e manifestos | ODbL 1.0 | banco de dados aberto, derivados também abertos |
| Evidência bruta | não licenciada pelo projeto | direito autoral de terceiros; regras de acesso na seção 1 |

Enquanto os arquivos `LICENSE` não existirem, o repositório não está formalmente aberto a reuso. Esta é a primeira decisão a tomar.

## 8. Conduta

Critica-se a evidência, o método e o texto, não a pessoa. Contestação vem com evidência. Ninguém expõe dado privado de ninguém, inclusive de quem é objeto de dossiê. Ameaça, assédio ou tentativa de pressão sobre mantenedores é registrada publicamente e, quando for o caso, comunicada à autoridade.

## 9. Configuração que só o dono do repositório pode fazer

1. Criar o branch `main` e torná-lo o padrão. Hoje o padrão é um branch de sessão.
2. Proteger `main`: exigir pull request, exigir aprovação, exigir status verde do workflow, proibir force push e remoção do branch, exigir commits de merge assinados.
3. Ativar o GitHub Pages a partir da pasta `docs/` ou de um workflow, para carta, método, boletins e erratas.
4. Adicionar o espelho: um workflow que faz push para Codeberg ou GitLab a cada merge, e o registro no Software Heritage em https://archive.softwareheritage.org/save/.
5. Escolher as licenças e adicionar os arquivos `LICENSE`.
6. Ativar a varredura de segredos do GitHub no repositório.
7. Preencher a lista de mantenedores abaixo.

## Mantenedores

| Nome | Contato público | Declaração de vieses e conflitos | Desde |
|---|---|---|---|
| a preencher | | link para declaração no repositório | |

Regra: mínimo de dois mantenedores antes de publicar qualquer conteúdo da camada 3.
