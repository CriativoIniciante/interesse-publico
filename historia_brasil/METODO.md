# Arquivo vivo da história do Brasil: método proposto

Proposta de método para um sistema que se alimenta e se atualiza sozinho para guardar o registro público do Brasil: o acervo digital gratuito da Biblioteca Nacional para trás, e as notícias dos grandes veículos e dos jornalistas independentes para frente, todo dia. A carta de princípios, que manda quando conflitar com este texto, está em `CARTA.md`. Versão 0, setembro de 2026.

## 0. Resumo em uma página

O sistema faz sozinho: coletar, preservar, carimbar no tempo, revisitar, comparar, apontar e publicar o que coletou e o que falhou. O sistema não faz sozinho: acusar, concluir sobre pessoas, publicar juízo.

Três camadas separadas, que nunca se misturam:

| Camada | Conteúdo | Quem altera | Regra |
|---|---|---|---|
| 1. Evidência | cópia bruta (WARC), hash SHA-256, carimbo de tempo | ninguém | só acrescenta, nunca edita nem apaga |
| 2. Descrição | texto extraído, título, autor, veículo, datas, versões, entidades | programas, com correção humana registrada | toda correção fica no histórico |
| 3. Interpretação | divergências, contradições, alterações, padrões, dossiês | pessoas, com apoio de programas | assinada, datada, versionada, ligada às evidências |

Princípio que resolve quase toda dúvida: toda afirmação aponta para uma evidência preservada, com hash, que qualquer pessoa pode abrir e conferir.

A confiabilidade vem de quatro mecanismos, não de boa intenção: imutabilidade com prova pública de existência no tempo, cópias em lugares independentes, lacunas publicadas com o mesmo destaque do conteúdo, e contestação pública com resposta registrada. A honestidade vem de um vocabulário fixo, de critérios publicados antes de serem aplicados, da simetria auditável, e de um protocolo escrito de antemão para quando aparecer indício de crime.

## 1. O que "história" significa aqui

O que se preserva:

1. O registro publicado: o que foi dito, por quem, onde, quando. Inclui manchete, texto, autor, hora de publicação e hora de modificação.
2. A mudança do registro: edições, trocas de título, remoções. O que um veículo publicou às 9h e apagou às 11h é história, e é a parte que mais se perde.
3. Os documentos primários: Diário Oficial, votações, decisões judiciais, dados oficiais. São a régua contra a qual as afirmações são medidas.
4. O registro retrospectivo: a Hemeroteca Digital Brasileira e o acervo da BNDigital, para ligar o presente ao passado com a mesma estrutura de dados.

O que não se preserva: opinião privada, dado de pessoa privada sem função pública, conteúdo que não foi publicado. O arquivo guarda o que foi tornado público.

## 2. Fontes

### 2.1 Critérios de entrada

Uma fonte entra na lista quando: publica regularmente; tem autor ou responsável identificável; é pública. Entra por commit, com justificativa. Sai por commit, com justificativa. A lista é pública em `fontes.yaml`. Pluralidade é regra de desenho, não resultado esperado: a lista tem de cobrir o espectro político e editorial, e o boletim diário mostra a cobertura por fonte, para que a falta de pluralidade seja visível.

### 2.2 Inventário inicial

| Grupo | Fontes | Acesso | Limites |
|---|---|---|---|
| Agências públicas | Agência Brasil, Agência Câmara, Agência Senado | RSS | verificar licença de reuso; Câmara e Senado também têm API de dados abertos |
| Grandes veículos | G1, Folha, Estadão, O Globo, UOL, CNN Brasil, Correio Braziliense, Poder360, Metrópoles | RSS, muitos com paywall parcial | texto integral protegido por direito autoral: fica em acervo fechado |
| Independentes e nicho | Agência Pública, Intercept Brasil, Ponte, Repórter Brasil, Brasil de Fato, Mídia Ninja, CartaCapital, Piauí, Nexo, Congresso em Foco, Gazeta do Povo, Revista Oeste, O Antagonista, newsletters (Substack tem `/feed`), canais de YouTube (RSS por `channel_id`), Bluesky (API pública e Jetstream, sem autenticação), Telegram (pré-visualização pública `t.me/s/<canal>`) | RSS, API, HTML | X/Twitter tem API paga e instável: não depender; guardar via Wayback o que for citado |
| Verificadores | Lupa, Aos Fatos, Comprova, Fato ou Fake, Estadão Verifica | RSS e Google Fact Check Tools API (padrão ClaimReview, chave gratuita) | verificação é opinião fundamentada de terceiro, entra na camada 2 como registro, não como veredito do arquivo |
| Documentos primários | Diário Oficial da União (in.gov.br), API da Câmara, API do Senado, STF, STJ, TSE, Portal da Transparência, IBGE, DATASUS | API e HTML | régua para contradição com fonte primária |
| Arquivos terceiros | Wayback Machine (Save Page Now 2, seis capturas por minuto autenticado; CDX para consulta), Common Crawl | API | cópia fora do controle do operador |
| Retrospectivo | Hemeroteca Digital Brasileira, BNDigital | interface DocReader; sem API pública documentada | ver 2.3 |

Feeds testados em 8 de setembro de 2026, de dentro de um ambiente com proxy, estão em `fontes.yaml` com o campo `verificado`. Refazer o teste na máquina que vai coletar.

### 2.3 Biblioteca Nacional: como tratar

O que se sabe: a Hemeroteca Digital Brasileira está em memoria.bn.gov.br, na interface DocReader, com busca por texto OCR. Não há API pública documentada. Os termos da BN dizem que a instituição guarda o acervo mas não detém os direitos autorais; títulos protegidos exigem autorização do detentor para reuso; a citação obrigatória é "Acervo da Fundação Biblioteca Nacional – Brasil". Periódicos do século XIX e início do XX estão em domínio público; para o século XX é preciso conferir título a título.

O caminho proposto, na ordem:

1. Pedido formal à Fundação Biblioteca Nacional, Coordenadoria de Publicações Seriadas e equipe da BNDigital, apresentando a carta, o método e o pedido de acesso em lote ou de um conjunto de dados de OCR e metadados. Instituições respondem melhor a projeto público, com finalidade declarada, do que a tráfego anônimo. Esta é a via honesta e a única sustentável.
2. Enquanto o pedido tramita: coleta lenta, identificada e limitada aos títulos em domínio público, respeitando `robots.txt`, com intervalo de vários segundos entre páginas, em horário de baixa carga, parando ao primeiro sinal de bloqueio. Guardar imagem da página e o OCR da própria BN, com a referência `bib`, `pasta` e `pagfis` da interface, para que cada citação leve à página original.
3. Reprocessar o OCR com ferramenta atual (Tesseract em português, ou Kraken para tipografia antiga), guardar as duas versões e marcar qual é qual. OCR ruim é a maior fonte de erro em pesquisa de hemeroteca.
4. Faixa própria e lenta: a Hemeroteca é trabalho de anos e não pode competir com a coleta diária. Fila separada, orçamento separado.

O que não fazer: raspar a BN em paralelo, sem identificação, ou republicar imagem de título protegido.

### 2.4 Como o sistema se alimenta sozinho sem se desviar

- Descoberta: links citados nas matérias coletadas e autores recorrentes geram propostas de novas fontes em uma fila. Ninguém entra na lista sem aprovação humana e commit com justificativa. O sistema propõe; a pessoa decide; o critério é público.
- Entidades: pessoas, órgãos e lugares são ligados a identificadores do Wikidata quando existe correspondência inequívoca, para que o mesmo político em 1990 e em 2026 seja a mesma entidade.
- Reexecução: toda análise da camada 3 declara suas entradas por hash; quando entra dado novo, a análise é reexecutada e a saída nova é versionada ao lado da antiga.
- Saúde: o próprio sistema é uma fonte. Falha de coletor, feed que mudou de endereço, bloqueio, tudo vira registro e aparece no boletim.

## 3. Arquitetura

```
coletores ──> evidência (WARC + SHA-256 + manifesto diário + carimbo OTS + cópia no Wayback)
                 │
                 ├──> revisita (+2h, +24h, +7d, +30d, +365d) ──> versões e diffs
                 │
                 └──> descrição (texto, metadados, entidades) ──> índice (SQLite FTS5, Datasette)
                                                                       │
                                                       interpretação (análises versionadas e assinadas)
                                                                       │
                                                       publicação + boletim diário + contestação + erratas
```

### 3.1 Coleta

- Agendamento: a cada hora para feeds, uma vez por dia para consolidação, manifesto e carimbo. GitHub Actions serve para começar; depois uma máquina pequena própria, porque depender de um único provedor contraria a carta.
- Identificação: `User-Agent` com nome do projeto e endereço de contato. `robots.txt` respeitado. No máximo uma requisição por segundo por domínio. Bloqueio ou pedido de parada é respeitado e registrado.
- Registro bruto: cada resposta HTTP vira um registro WARC (biblioteca `warcio`), com cabeçalhos, corpo, hora e hash. WARC é o formato do Internet Archive e das bibliotecas nacionais: sobrevive a mudança de ferramenta.
- Cópia externa: cada URL coletada é enviada ao Save Page Now do Internet Archive, e o link da captura é guardado. Se o arquivo local for questionado, existe uma cópia em instituição terceira, feita no mesmo dia.
- Conteúdo fechado: o que está atrás de paywall e não vem no feed é guardado como veio (título, resumo, link, hora). Não se contorna paywall.

### 3.2 Revisita e diff

Cada item é buscado de novo em 2 horas, 24 horas, 7 dias, 30 dias e 1 ano. Muda título, muda texto, some a página, muda a data: cada versão é guardada e o diff é gerado. Isto é a camada mais valiosa e a mais barata. A referência é o NewsDiffs, de 2012, e o `diffengine` do DocNow, que faz exatamente isto a partir de RSS e envia ao Wayback. Alteração sem nota de correção é fato observável, entra na camada 2 e pode ser publicada automaticamente, porque é um diff, não um juízo.

### 3.3 Preservação e prova de integridade

- Armazenamento endereçado por conteúdo: o nome do arquivo é o hash. Mesmo conteúdo, mesmo arquivo. Só acrescenta.
- Manifesto diário: lista de todos os hashes coletados no dia, com URL, hora e tamanho. O hash do manifesto é a raiz do dia.
- Carimbo de tempo: a raiz do dia recebe carimbo OpenTimestamps (`ots stamp`), que ancora o hash na cadeia do Bitcoin, gratuito, verificável por qualquer pessoa sem confiar no operador. O arquivo `.ots` e o manifesto ficam no git. Isto prova que o conteúdo existia naquela data e não foi alterado depois, inclusive contra quem opera o sistema.
- Commits assinados: GPG ou Sigstore, para que a autoria de cada mudança no código, na lista de fontes e na carta seja verificável.
- Cópias: regra 3-2-1. Original em armazenamento de objetos (Backblaze B2, Cloudflare R2 ou similar), segunda cópia em provedor diferente, terceira no Internet Archive via Save Page Now. Metadados e manifestos também no git, que é a cópia mais fácil de espelhar.
- Verificação de fixidez: uma vez por ano, recalcular todos os hashes e publicar o relatório. Arquivo que não é verificado não está preservado.

### 3.4 Descrição

- Extração de texto com `trafilatura`, que é o que melhor separa texto de matéria de ruído de página em avaliações independentes. Guardar também o HTML bruto, porque extratores erram.
- Metadados: título, subtítulo, autor, veículo, URL canônica, publicado em, modificado em, idioma, seção. Quando o veículo declara a hora de modificação e ela não bate com o diff observado, isso é registro.
- Deduplicação por URL canônica e por similaridade de texto (simhash), sem apagar nada: duplicata é marcada, não removida.
- Entidades ligadas ao Wikidata. Modelos de linguagem podem ajudar a extrair e classificar, com a saída marcada como automática, com modelo, versão e hash do prompt.
- Formato: JSONL por dia mais SQLite com FTS5. Datasette publica isso com busca e API sem código adicional.

### 3.5 Interpretação

Cada análise é uma pasta com: pergunta registrada antes de olhar o dado, método, lista de entradas por hash, código, saída, autoria (pessoa, ou modelo com versão e prompt), revisor, status (rascunho, revisado, publicado, contestado, corrigido, retratado). Análise que não declara entradas não é publicada.

Tipos de análise, do mais mecânico ao que mais exige gente:

| Tipo | Detecção | Publicação |
|---|---|---|
| Alteração não declarada | automática, diff | automática, é fato observável |
| Divergência entre fontes | automática, mesma entidade e mesmo fato com valores incompatíveis | automática como lista, sem juízo sobre quem errou |
| Contradição com fonte primária | automática, afirmação contra documento oficial ou dado público | após confirmação humana |
| Padrão por fonte ou ator | estatística, contagem das anteriores | após revisão humana, com método e intervalo de incerteza |
| Indício de ilícito | humana, a partir das anteriores ou de documento | protocolo da seção 5 |

Modelos de linguagem: servem para extrair, agrupar, resumir e sugerir. Não servem para decidir. Usar mais de um modelo e tratar a discordância entre eles como sinal de que a pessoa precisa olhar. Prompts são públicos e versionados.

### 3.6 Publicação

- Portal com busca (Datasette ou site estático gerado), página por fonte, página por entidade, linha do tempo, diffs.
- Boletim diário automático: quantos itens por fonte, o que mudou, o que sumiu, o que falhou na coleta, quais análises foram reexecutadas, quais contestações entraram e saíram.
- Direito autoral: texto integral protegido não é publicado. Publica-se metadado, trecho curto, hash, link original e link do Wayback. O texto integral fica em acervo fechado para preservação e pesquisa. Quem quiser conferir uma citação abre o original ou a captura do Wayback.
- Licenças do próprio projeto: código em licença livre (AGPL ou MIT), metadados e manifestos em CC BY-SA ou ODbL, para que espelhar seja fácil e lícito.

### 3.7 Contestação e errata

Canal público (issues do repositório ou formulário que vira issue). Qualquer registro pode ser contestado, com evidência. A contestação recebe número, prazo e resposta escrita. Contestação e resposta ficam arquivadas e ligadas ao registro. Página de erratas com o mesmo destaque da inicial. Nada é apagado: corrigido ou retratado ganha marca e texto explicativo, o original continua acessível.

## 4. Confiabilidade do próprio sistema

O ponto mais difícil não é confiar nas fontes, é fazer com que se possa confiar no arquivo sem confiar em quem o opera.

- Prova de tempo e integridade fora do controle do operador: carimbo OpenTimestamps e cópia no Internet Archive. Se amanhã alguém acusar o arquivo de ter fabricado ou alterado um registro, a prova está em terceiros.
- Lacunas publicadas: o que não foi coletado, e por quê, é saída de primeira classe. Coleta que falha em silêncio distorce tanto quanto edição.
- Reprodutibilidade: qualquer número publicado se regenera a partir dos hashes declarados e do código no commit indicado.
- Separação de papéis no código: o coletor não tem opinião; a análise mora em outro lugar e é versionada separadamente.
- Auditoria de simetria: métricas por fonte e por ator (registros, alterações, contradições, dossiês, correções do próprio arquivo) publicadas todo mês, para que qualquer pessoa verifique se o arquivo está tratando lados diferentes com critérios diferentes.
- Espelhos: incentivar cópias independentes. Muitas cópias mantêm as coisas seguras. Um arquivo com uma só cópia é um arquivo em risco, inclusive de pressão sobre quem o mantém.
- Declaração de vieses de quem opera, pública, no repositório. O autor deste repositório trabalha com hipóteses sobre mortalidade no Brasil que são objeto de disputa pública; isso tem de estar declarado onde qualquer leitor veja.

## 5. Protocolo para indício de crime, distorção ou desonestidade

Escrito antes, para não ser decidido sob pressão. Vale para qualquer pessoa, partido, veículo ou instituição.

### 5.1 Vocabulário obrigatório

Definido em `CARTA.md`, item 4: fato registrado, divergência, contradição com fonte primária, alteração não declarada, padrão, indício de ilícito. Investigado, denunciado, réu e condenado são termos distintos; a instância da condenação é sempre dita. "Criminoso" só com condenação, e mesmo assim se diz "condenado por X em Y instância".

Isto não é cautela vazia. Calúnia, artigo 138 do Código Penal, é imputar falsamente fato definido como crime. A defesa do arquivo é a evidência preservada e a precisão da linguagem: descreve-se a conduta documentada, cita-se o dispositivo legal que pode se aplicar, diz-se o que falta para confirmar. A exceção da verdade existe, mas a melhor defesa é nunca afirmar mais do que a evidência sustenta.

### 5.2 Passos quando surge indício de ilícito

1. Preservar primeiro. Todas as evidências com hash, carimbo e cópia no Wayback antes de qualquer outra coisa. Evidência some.
2. Abrir dossiê, não publicar conclusão. O dossiê lista as evidências, a leitura proposta e o que falta.
3. Revisão por pelo menos duas pessoas, uma que não escreveu o dossiê, de preferência com convicções políticas diferentes. Discordância registrada por escrito no dossiê.
4. Direito de resposta antes da publicação: procurar a pessoa ou instituição, dar prazo razoável, publicar a resposta na íntegra ou registrar o silêncio.
5. Publicar com: evidências, raciocínio, limites, resposta, data, nomes dos revisores, assinatura.
6. Comunicar. Publicado o dossiê com indício de ilícito, o arquivo envia cópia ao Ministério Público ou à autoridade policial e registra o número do protocolo. Qualquer pessoa pode comunicar crime de ação pública, artigo 5º, parágrafo 3º, do Código de Processo Penal. Isto é regra adotada de antemão, não decisão caso a caso.
7. Manter. Dossiê contestado ou errado recebe correção ou retratação à vista, nunca remoção.

### 5.3 Os dois erros que o protocolo evita

Fugir: quando a evidência é forte, dizer "polêmica", "ambos os lados", "acusações", em vez de dizer o que os documentos mostram e quem fez. Equilíbrio falso é distorção, e o protocolo obriga a nomear.

Atropelar: quando a evidência é fraca, publicar porque a hipótese agrada a quem opera. O protocolo obriga a dizer que é fraca. As duas regras são a mesma regra: a afirmação segue a evidência, para qualquer lado.

### 5.4 O que fica com a máquina e o que fica com gente

Máquina: detectar diff, detectar divergência, cruzar afirmação com documento primário, contar, agrupar, preparar o dossiê com as evidências já listadas. Gente: decidir que há indício de ilícito, escrever a leitura, revisar, ouvir o acusado, assinar, comunicar. Um sistema que acusa sozinho não é confiável; um sistema que preserva e aponta sozinho, e deixa a acusação para pessoas identificadas e responsáveis, é.

## 6. Riscos legais e éticos

| Tema | Norma | Consequência para o desenho |
|---|---|---|
| Direito autoral | Lei 9.610/1998; art. 46 permite citação e pequenos trechos, não há exceção clara para preservação por arquivo privado | acervo fechado para texto integral; publicação de metadados, trechos curtos, hashes e links; pedir licença a quem puder dar (agências públicas, independentes) |
| Dados pessoais | Lei 13.709/2018, LGPD; art. 4º, II, afasta a lei para fins jornalísticos e acadêmicos, com ressalvas | minimizar dado de pessoa privada; figura pública no exercício da função é matéria pública; ter política de dados escrita |
| Honra | Código Penal, arts. 138 a 140 | vocabulário da seção 5.1; evidência sempre ligada; direito de resposta prévio |
| Direito de resposta | Lei 13.188/2015 | canal público, prazo, publicação na íntegra |
| Remoção de conteúdo | Marco Civil, Lei 12.965/2014, art. 19, com a decisão do STF de 2025 sobre responsabilidade de plataformas | processo escrito de notificação e resposta; o arquivo não é rede social, mas terá um |
| Termos de uso e robots | contratuais; BN exige autorização para títulos protegidos e citação da fonte | identificação, limite de taxa, pedido formal à BN, parada ao primeiro bloqueio |
| Segurança de quem opera | pressão, ameaça, processo estratégico contra participação pública | cópias fora do país e fora do controle do operador; carta pública que já responde às objeções previsíveis; nunca operar sozinho na camada 3 |

## 7. Ferramentas e custo mínimo

Python 3.12 e bibliotecas: `feedparser`, `httpx`, `trafilatura`, `warcio`, `sqlite-utils`, `datasette`, `opentimestamps-client`, `rclone` para cópias, GPG ou `gitsign` para assinatura. Nada disso é exótico; tudo tem mais de cinco anos de uso em arquivos e redações.

Estimativa de volume para a coleta diária, sem a Hemeroteca:

| Item | Valor |
|---|---|
| Itens por dia, 30 a 40 fontes | 1.500 a 3.000 |
| HTML bruto por item | 200 a 400 KB |
| WARC por dia, sem compressão | 400 MB a 1,2 GB |
| WARC por ano, comprimido | 50 a 100 GB |
| Texto extraído por ano | 3 a 5 GB |
| Custo de armazenamento de objetos | cerca de US$ 6 por TB por mês por cópia |
| Máquina pequena | R$ 30 a R$ 60 por mês |

Hemeroteca em faixa separada: 1 a 2 MB por página de imagem; um título de um ano pode ter milhares de páginas. Orçamento próprio.

Git guarda código, carta, lista de fontes, manifestos, carimbos `.ots`, metadados e análises. Não guarda WARC nem imagem.

## 8. Roteiro por fases

| Fase | Entrega | Pronta quando |
|---|---|---|
| 0 | carta, método, lista de fontes, declaração de vieses, pedido à BN enviado | tudo publicado e assinado; protocolo do pedido registrado |
| 1 | coletor de feeds, WARC, hash, manifesto diário, carimbo OTS, Save Page Now, boletim diário | 30 dias seguidos sem falha silenciosa; toda falha apareceu no boletim |
| 2 | revisitas e diffs; Datasette público com metadados; página de lacunas | primeiro mês de diffs publicado; alterações não declaradas listadas por fonte |
| 3 | fontes primárias (DOU, Câmara, Senado, tribunais, dados oficiais) e verificadores via ClaimReview | cruzamento afirmação contra documento rodando e com taxa de erro medida em amostra |
| 4 | Hemeroteca: acordo ou coleta lenta em domínio público; OCR reprocessado; mesma estrutura de dados | um título completo do século XIX preservado e pesquisável de ponta a ponta |
| 5 | camada 3 completa: entidades, contradições, padrões, dossiês, protocolo da seção 5, canal de contestação, erratas | primeiro dossiê publicado com revisão dupla, direito de resposta e comunicação registrada |
| 6 | espelhos independentes, auditoria externa anual de fixidez e simetria | pelo menos dois espelhos mantidos por terceiros; relatório de auditoria publicado |

Ordem importa: preservar antes de analisar. Um ano de coleta bruta sem nenhuma análise vale mais do que um mês de análise sem coleta preservada.

## 9. O que não recomendo

- Depender de um único provedor, inclusive do GitHub, para o que precisa sobreviver.
- Deixar modelo de linguagem publicar juízo sobre pessoa sem revisão humana assinada.
- Raspar a Biblioteca Nacional em ritmo agressivo ou sem identificação.
- Publicar texto integral protegido.
- Dar nota única de "confiabilidade" a veículos. Publicar métricas observáveis (alterações não declaradas, contradições com fonte primária, correções) e deixar o leitor concluir.
- Começar pela análise. Quem começa pela análise coleta o que confirma a hipótese.
- Operar a camada 3 sozinho.

## 10. Decisões que são suas

1. Âmbito: política e instituições, ou toda a notícia. O volume e o risco mudam muito.
2. Quem revisa a camada 3 com você, e como se garante convicção diferente da sua.
3. Aceita a regra de comunicar ao Ministério Público após publicação de dossiê com indício de ilícito, como consta na carta.
4. Onde hospedar e quanto gastar por mês.
5. Licenças do código e dos metadados.
6. Nome do projeto.

## Fontes consultadas para este documento

- Hemeroteca Digital Brasileira, portal e guia: https://bndigital.bn.gov.br/hemeroteca-digital/ e https://www.gov.br/bn/pt-br/atuacao/colecoes-e-servicos-aos-leitores/publicacoes-seriadas/tutorial-basico_hdb_v5.pdf
- Termos de uso da Biblioteca Nacional para arquivos digitais e direitos autorais: https://antigo.bn.gov.br/servicos/direitos-autorais
- Save Page Now 2, documentação pública: https://archive.org/details/spn-2-public-api-page-docs e https://wiki.archiveteam.org/index.php/Internet_Archive/Save_Page_Now
- OpenTimestamps, cliente: https://github.com/opentimestamps/opentimestamps-client
- NewsDiffs: https://github.com/ecprice/newsdiffs ; diffengine: https://github.com/DocNow/diffengine
- Google Fact Check Tools API: https://developers.google.com/fact-check/tools/api
- Bluesky, Jetstream e API pública: https://docs.bsky.app/docs/advanced-guides/firehose e https://docs.bsky.app/blog/jetstream
- Agência Brasil, feeds: https://agenciabrasil.ebc.com.br/feed/
