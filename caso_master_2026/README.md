# Caso Master — o relatório da PF de 218 páginas e a crise institucional

**Estado em 04/09/2026, 10h (horário de Brasília). Seções 12 a 16 acrescentadas na tarde e noite do mesmo dia. Correções de 06/09/2026 em [verificacao_personagens_2026-09-06.md](verificacao_personagens_2026-09-06.md).**

Perfis de cada pessoa citada: [personagens.md](personagens.md).

## Mapa das relações e do peso das provas

[![Mapa das relações do caso Master](mapa/mapa_relacoes.png)](mapa/mapa_relacoes.png)

Cada linha é uma relação documentada nas seções abaixo. **Cor = status**: vermelho [I], indício documentado de ilegalidade ou inquérito formal com prova material; amarelo [S], suspeito (conflito de interesse, alegação sem corroboração, omissão sem explicação); verde [L], ato lícito dentro da função; cinza, vínculo sem status. **Espessura = peso da prova**: grossa, prova material; média, relato documentado; fina tracejada, alegação de parte interessada. A etiqueta [I]/[S]/[L] acompanha cada linha para o significado não depender só da cor. Versão vetorial: [mapa/mapa_relacoes.svg](mapa/mapa_relacoes.svg); gerador: [mapa/gen_mapa.py](mapa/gen_mapa.py). Ninguém no mapa foi condenado por nada relacionado ao caso.

Dossiê neutro, montado por consulta à imprensa em 04/09/2026. Não é peça de campanha nem toma partido. Onde as fontes divergem, a divergência está anotada. Onde algo é alegação (não fato apurado), está marcado como tal. Todas as fontes estão listadas ao final.

---

## 1. Correção de premissa: o relatório não "vazou"

O documento veio a público por decisão judicial. Em 01/09/2026 o ministro André Mendonça (STF), relator da Operação Compliance Zero, retirou o sigilo da Petição 16.662, que contém o relatório. Antes disso, em 27/08, ele o recebera da PF.

O que existe em paralelo é um inquérito sobre vazamento seletivo: um perito da PF (João Cláudio Nabas) acessou a extração do celular de Vorcaro em 01/12/2025 e três dias depois produziu os arquivos "Moraes.pdf" e "Toffoli e esposa.pdf", sugerindo à equipe que fossem entregues à imprensa. Foi alvo de busca em maio (7ª fase) e afastado das funções. É esse episódio que dá lastro à expressão "vazamentos seletivos" usada por Lula em 03/09.

## 2. O documento

| Item | Dado |
|---|---|
| Identificação | IPJ-A nº 3298613/2026 (Informação de Polícia Judiciária) |
| Extensão | 218 páginas, assinado por 8 policiais federais |
| Entrega | 27/08/2026, em resposta a despacho de Mendonça de 24/08 com prazo de 72 horas |
| Distribuição interna | 181 páginas sobre o contato "Alexandre de Moraes BRASILIA"; 18 páginas sobre Paulo Gonet (PGR) e Andrei Rodrigues (DG da PF) |
| Base | Extração do iPhone de Daniel Vorcaro apreendido na Compliance Zero (nov/2025) |
| Onde está | PET 16.662, STF, sigilo levantado em 01/09/2026 |

O despacho de 24/08 pedia à PF identificar as pessoas mencionadas nos relatórios de fevereiro, inclusive detentoras de foro por prerrogativa de função. A PF afirma que, em reuniões anteriores, o relator "indagou expressamente" o que havia sobre Moraes nos dados extraídos. Na corporação a reunião de 24/08 ficou conhecida como "cilada": delegados convocados para outro assunto saíram com o despacho de 72 horas.

## 3. Como a PF chegou às mensagens

- Extração física com Cellebrite, indexação com IPED (ferramenta forense).
- Vorcaro usava um rito de três passos: escrevia no app Notas, capturava a tela, enviava a imagem como "visualização única" pelo WhatsApp. O iOS guardava cópia temporária em pasta interna, que sobreviveu à exclusão.
- Cruzando logs do iOS, os PDFs residuais e os registros de envio, a PF reconstruiu 52 notas enviadas ao mesmo destinatário entre outubro e novembro de 2025, todas no mesmo padrão (print → PDF residual → envio em cerca de 12 segundos).
- O número salvo como "Alexandre de Moraes BRASILIA" foi compartilhado com Vorcaro pelo ex-ministro Fábio Faria em 26/12/2023 às 11h43min45s; Vorcaro salvou 13 segundos depois.
- O contato do outro lado ativou apagamento automático em 17/09/2025, usou "apagar para todos" em 01/10/2025 e, em 17/11/2025, respondeu com quatro fotos (08h16, 17h31, 20h21, 20h23). A PF registra isso como prova de interação bidirecional, mas as respostas em texto não foram recuperadas.

Isso é o que contradiz a posição anterior do gabinete de Moraes. Em 06/03/2026 a comunicação do STF negou qualquer contato, dizendo que os arquivos de visualização única de 17/11/2025 "estavam vinculados a pastas de outras pessoas da lista de contatos, jamais ao ministro". A negativa foi repetida cinco vezes.

## 4. O que o relatório contém

### 4.1 Contratos com o escritório da esposa do ministro

- 23/01/2024: contrato Banco Master × Barci de Moraes Advogados (Viviane Barci de Moraes). Três anos, cerca de R$ 3,6 milhões/mês brutos. Total citado como R$ 129 a 131 milhões brutos conforme a fonte; cerca de R$ 108 milhões líquidos. Objeto: advocacia, consultoria jurídica e compliance.
- Metadados da minuta: último editor "Ministro Alexandre de Moraes", com modificações em 11/01 e 15/01/2024. A minuta foi enviada a Vorcaro por Viviane em janeiro de 2024.
- Dados da Receita divulgados em abril/2026 indicam cerca de R$ 80 milhões efetivamente recebidos pelo escritório em 2024–2025.
- Maio a julho/2025: segundo contrato, via Viking (ou Vikings) Participações, R$ 50 milhões, com pagamento parcial em cotas de aeronaves: jato Embraer Legacy 650 (PP-NLR, US$ 5,5 milhões) e helicóptero Airbus EC155 B1 (US$ 1,3 milhão). Mensagens registram que a esposa do ministro já usava as aeronaves; havia fatura pendente de R$ 22,8 milhões.
- O Master concedeu aos filhos de Moraes cartões de crédito com limite de R$ 300 mil, arranjados por Vorcaro.

### 4.2 Instruções internas de Vorcaro sobre esse pagamento

- 15/03/2024, Fábio Faria a Vorcaro, após atraso das parcelas de fevereiro e março: "O careca não pode atrasar".
- Vorcaro a funcionários do banco: "esse Barci de Moraes por favor não deixe atrasar um dia (...) É o pgto mais importante que temos. Pode pagar sempre, sem nota." Pagamento a ser feito "do jeito que for".

### 4.3 Encontros registrados

| Data | Registro |
|---|---|
| 21/12/2023 | Garagem, São Paulo (intermediação de Fábio Faria) |
| 26/12/2023 | Segundo encontro; contato compartilhado |
| 30/12/2023 | Almoço no Six Senses Botanique, Campos do Jordão |
| 02/02/2024 | Jantar em residência no Lago Sul, Brasília |
| abril/2024 | Fórum Jurídico de Londres, bancado por Vorcaro; ministro teria vetado participantes e sugerido Michel Temer; convidados citados: "Andrei", o procurador-geral, "3 ministros STF" e Tony Blair |
| 19–20/03/2025 | Encontro com "hugo e ciro" |
| 19/04/2025 | Feriado em Campos do Jordão |
| 2025 | Segundo fórum de Londres planejado e cancelado |

### 4.4 As mensagens de outubro e novembro de 2025 (véspera da liquidação)

- 30/10/2025, três notas seguidas: relata "informações informais e em confiança de turma do banco central"; diz ter "pessoas de dentro do bacen que são meus amigos", que "participaram das reuniões, então a info é 100%", e que "não posso queimá-los" porque "vão saber que fui eu se chegar ao G" (a PF entende "G" como Gabriel Galípolo, presidente do BC). Envia lista de policiais e procuradores. Pede: "É importante reforçar com Andrei e Paulo pra não deixar ninguém de baixo fazer uma sacanagem".
- 04/11/2025: "Médio a grave seria busca ou quebra de sigilo?"; "Mas pedido deferido por parte deles? Algo que dê pra bloquear?"
- 15/11/2025: "Acha que 2ª já tenho que estar fora?"; "Que loucura, bem na semana que estou resolvendo tudo"; "Aquele mesmo juiz Ricardo? E o Galípolo tá sabendo? Conseguimos fazer algo?"
- 16/11/2025: "Você acha que existe alguma chance disso acontecer amanhã de manhã?"
- 17/11/2025 (véspera da operação): 07h19 menciona "investidores" e "vazada"; 17h22 "Fiz uma correria aqui pro tentar salvar"; 17h26 "Conseguiu ter notícia ou bloquear?"; 23h48 "Amanhã começam as batidas do esteves" (André Esteves, BTG). Dias antes, pedira adiamento de operação policial por causa de feriado.
- Em outra mensagem, Vorcaro fala em "gratidão da minha vida a você".

Conclusão da PF: indícios de uma "rede de monitoramento e influência", com possível infiltração em instâncias altas de instituições distintas, capaz de dar ao banqueiro informação sigilosa para mudar estratégia de negócio e até preparar fuga. Investiga também um grupo de WhatsApp chamado "Master" com servidores do BC.

### 4.5 As 18 páginas sobre Gonet e Andrei

- As mensagens atribuídas a Gonet chegam por intermédio do advogado Ciro Soares (ex-defensor do Master), que dizia repassar falas do PGR.
- 28/03/2025, mensagem atribuída a Gonet sobre a viagem a Londres: "Oba!!!! Tomara que tenha charuto e macalan!"
- Março a junho/2025: tratativas para incluir Pedro Gonet, filho do PGR, na comitiva, com despesas por conta de Vorcaro. O evento de 2025 foi cancelado.
- Mensagem atribuída a Gonet dizendo sentir falta de Vorcaro e estar "torcendo" por ele no dia em que o BRB anunciou a compra de 58% do Master.
- Andrei Rodrigues aparece em anotações sobre convites, passagens e despesas de autoridades para eventos no exterior e na frase "reforçar com Andrei e Paulo". O relatório não descreve mensagem direta entre Vorcaro e Andrei.

### 4.6 Outros nomes citados

Fábio Faria (intermediário), Ciro Soares e Leonardo Palhares (advogados), Guilherme Benazzi (autor da minuta), Paulo Sérgio Neves de Souza (ex-BC), Marcus Vinicius da Mata (Prime You, aeronaves), Angelo Antonio Ribeiro da Silva (signatário e comprovantes), Martha Graeff (namorada), Stella Vorcaro (filha), Pedro Gonet, "Sidney" (motorista em Brasília), Ana Matos (logística de eventos) e um contato "Geraldo" do Brazil Journal (pautas em coberturas).

## 5. Outros ministros do STF no caso (fora do relatório de 27/08, mas no mesmo conjunto probatório)

- Dias Toffoli: relator sorteado em 29/11/2025; deixou a relatoria em 12/02/2026 após a PF encontrar referências a ele no celular (encontros ao menos 10 vezes, segundo a imprensa). Fundo Arleen, ligado ao Master, transferiu R$ 35 milhões à Maridt, empresa dele com os irmãos, dona de resort no Paraná. Ele nega recebimentos.
- Kassio Nunes Marques: o filho advogado recebeu R$ 281,6 mil da Consult Inteligência Tributária, consultoria que recebeu R$ 18 milhões do Master (R$ 6,6 milhões) e da JBS (R$ 11,3 milhões) entre agosto de 2024 e julho de 2025; telefone particular do ministro estava no celular de Vorcaro.
- Luiz Fux: o filho Rodrigo esteve em degustação de uísque em Nova York paga por Vorcaro (maio de 2024) e no camarote dele na Sapucaí (2025); diz não ter tido relação comercial. O convite a Londres com despesas de Vorcaro foi ao filho de Gonet.
- Ricardo Lewandowski (então ministro da Justiça): R$ 6 milhões a family office da família (imprensa, abril/2026).
- Crítica registrada pela Revista Fórum e pela Agência Pública: Mendonça teria "poupado" Toffoli, Fux e Kassio ao concentrar o pedido em Moraes.

## 6. Cronologia: 24/08 → 04/09

| Data | Fato |
|---|---|
| 24/08 (seg) | Mendonça despacha à PF: 72 h para identificar citados, inclusive com foro |
| 27/08 (qui) | PF entrega as 218 páginas. No mesmo dia Vorcaro depõe a juiz auxiliar do gabinete de Mendonça (PET 16.653), sem a PF presente |
| 31/08 (seg) | Mendonça abre vista à PGR por 5 dias |
| 01/09 (ter) | Mendonça levanta o sigilo e pede a Fachin sessão plenária presencial ("caminho inevitável"). Gonet pede nulidade em menos de 12 h. Cúpula do MPF fala em "desânimo". Piauí publica relatório do Coaf sobre nova parcela do "Dark Horse". Oposição: ofício a Lula pedindo demissão de Andrei (Rogério Marinho); novo pedido de impeachment de Moraes com mais de 80 assinaturas (o 54º). Alcolumbre: 109 pedidos contra ministros, "não é normal", sinaliza não pautar. Andrei, a aliados: "abuso de poder". Escritório Barci divulga nota |
| 02/09 (qua) | Paulo Motoryn publica áudios e mensagens do encontro Mendonça × Vorcaro de 14/03/2025 no Instituto Iter. Mendonça confirma "uma única vez", diz que só ouviu e votou contra o Master (STP 976, precatórios). Primeira sessão plenária do STF ignora o tema; Fachin promete "medidas cabíveis", "sem precipitação". Flávio Bolsonaro chama o encontro de "cortina de fumaça". PGR envia ao STF delação de João Carlos Mansur (Reag). Depoimento de Vorcaro (tortura psicológica) vem a público. Ibovespa sobe 3% |
| 03/09 (qui) | Mendonça deixa a sociedade do Iter. Vem a público a delação rejeitada de Vorcaro (Bolsonaro, Tarcísio, Kassab). Estadão revela delação de Antônio Carlos Freixo Júnior (malas de dinheiro, fundo Havengate). Moraes peticiona no INQ 4781 pedindo investigação de Mendonça. Fachin abre procedimento e dá 5 dias úteis a Moraes, Mendonça, Gonet e Andrei; sessão adiada para a 2ª quinzena (a partir de 14/09). Lula grava vídeo. Renan Santos (Missão) protocola impeachment de Moraes e Toffoli |
| 04/09 (sex, até 10h) | Metrópoles: o relatório de inteligência usado por Moraes contra Mendonça traz carimbo "sem valor probatório" e confiança "baixa ou moderada". Vorcaro sinaliza poupar Moraes na 3ª tentativa de delação. Mendonça ainda sem resposta pública à petição de Moraes. Planalto ainda sem resposta ao ofício sobre Andrei |

## 7. Posição de cada ator (estado em 04/09, 10h)

**Alexandre de Moraes.** Não se manifestou pessoalmente sobre as mensagens. Em 03/09 peticionou no INQ 4781 (inquérito das fake news) apontando "fortes indícios" de improbidade, abuso de autoridade, crime de responsabilidade e "favorecimento a determinados grupos políticos" por Mendonça na condução das operações Sem Desconto (INSS) e Compliance Zero, e pediu remessa "imediata" a Fachin. Base: relatório de inteligência da PF que menciona suposto direcionamento contra Alcolumbre, interferência em delações e reuniões sobre afastar Andrei. O próprio documento se classifica como difusão restrita, sem valor probatório, sem cabeçalho nem assinatura de delegado.

**Escritório Barci de Moraes.** Nota: o setor de compliance consultou o ministro, "na condição de marido da sócia", apenas sobre eventuais impedimentos legais (ações no STF, participação em julgamentos de interesse do cliente); os serviços foram prestados; o ministro nunca julgou caso do Master. A PF registra que não há ligações entre Vorcaro e o contato "Vivi Moraes" antes de 11/01/2024.

**André Mendonça.** Sustenta que o plenário é a instância soberana para analisar o material. Confirmou o encontro de 14/03/2025 (intermediado pelo deputado Cezinha de Madureira, PL-SP, e por Ciro Soares), diz que a matéria estava em vista de outro ministro e que votou contra o banco. Saiu da sociedade do Iter em 03/09. Não respondeu publicamente à petição de Moraes até a manhã de 04/09.

**Paulo Gonet (PGR).** Pediu nulidade: "Ao juiz não cabe acusar, menos ainda ao juiz cabe realizar investigações pré-processuais"; ministro não manda investigar colega sem o Plenário. Dentro do MPF, integrantes do Conselho Superior defendem que ele saia do caso e que a apuração fique com o vice-PGR Hindemburgo Chateaubriand (LC 75/1993, art. 57, X). Gonet decidiu permanecer.

**Andrei Rodrigues (PF).** A aliados: Mendonça age "como juiz, investigador e Ministério Público", com "indícios de ilegalidade, abuso de poder e desvio de finalidade". Nega ter conversado com Moraes sobre Vorcaro e diz que não sabia quando o mandado seria expedido. Sobre a delação: "sem interesse técnico", porque acrescenta pouco. Fonte da PF chama o depoimento de 27/08 de "oitiva forjada para atacar Andrei e a PF".

**Edson Fachin (presidência do STF).** Abriu procedimento próprio em 03/09. Quer esclarecer: cumprimento da Lei Orgânica da Magistratura pela PF ao achar indícios contra autoridade com foro; uso de credenciais institucionais para analisar "documento estritamente privado"; possível revelação de informação sob sigilo a investigado; circunstâncias do despacho de Mendonça; controle da atividade policial pela PGR. Prazo de 5 dias úteis. Sessão só na 2ª quinzena de setembro. Ele decide se o caso vai ao Plenário.

**Divisão interna do STF** (Jornal de Brasília): Dino, Zanin e Gilmar Mendes alinhados a Moraes, comparando o método de Mendonça à Lava Jato; dúvidas sobre Kassio, Cármen Lúcia e o próprio Fachin. Julgamento previsto com quórum de 8.

**Lula.** Vídeo em 03/09: "o maior roubo da história do Brasil"; "foi no meu governo que ele foi preso e seu banco fechado"; "Nossa democracia não pode ficar refém de vazamentos seletivos"; "que se investigue todo mundo, sem blindagem de ninguém, doa a quem doer"; cobra que o presidente do STF e a PGR "liderem um processo que garanta a integridade". Não citou nomes. Não respondeu ao ofício que pede a saída de Andrei.

**Davi Alcolumbre (Senado).** Não pretende pautar impeachment; deixa o caso com o STF. Recebeu críticas em plenário (Viana: "acabou").

**Oposição e candidatos.** Flávio Bolsonaro (PL), na Expointer em 02/09: Moraes é "laranja podre", pede afastamento; o partido quer também a saída de Gonet e Andrei; chama o encontro de Mendonça de "cortina de fumaça". Renan Santos (Missão) protocolou impeachment de Moraes e Toffoli em 03/09.

**Mercado.** Ibovespa +3% em 02/09 (perto de 186 mil pontos), dólar a R$ 5,10, atribuído pela imprensa econômica a fluxo estrangeiro e "trade eleitoral".

## 8. Frentes paralelas que explodiram na mesma semana

1. **"Dark Horse"** (filme sobre a campanha de 2018 de Bolsonaro). Flávio Bolsonaro teria pedido US$ 24 milhões a Vorcaro; ao menos US$ 10,6 milhões pagos entre fev e mai/2025 ao fundo Havengate (Texas), cujo agente é Paulo Calixto, advogado de Eduardo Bolsonaro. Piauí (01/09): mais US$ 1,6 milhão em set/2025, total US$ 12,3 milhões. Delação de Freixo Júnior homologada pela PGR (03/09): malas de dinheiro a pedido de Vorcaro, com endereços; dúvida sobre se o dinheiro foi ao filme ou a despesas de Eduardo no exterior. Investigação formal de Vorcaro, Flávio e Eduardo autorizada por Mendonça em 23/07.
2. **Delação rejeitada** (tornada pública em 03/09): Vorcaro afirmou que doações de 2022 (R$ 3 milhões a Bolsonaro, via o cunhado Fabiano Zettel, e R$ 2 milhões a Tarcísio) e R$ 10 milhões em espécie ao PSD foram contrapartida acertada com Gilberto Kassab para manter a Credcesta no governo paulista. Kassab: "fantasioso"; Tarcísio e Bolsonaro negam. A PF e a PGR rejeitaram duas propostas (maio–junho) por não trazerem novidade.
3. **Depoimento de Vorcaro** (27/08, a juiz auxiliar de Mendonça, sem PF): alega tortura psicológica, maus-tratos e ameaças (agentes da escolta teriam falado em jogá-lo de helicóptero), e que a PF barrou a delação para proteger Andrei. "Tenho muito a relatar, mas não querem me ouvir." PF e PGR: nenhum fato concreto; ele busca abrir nova negociação. Em 04/09, sinaliza poupar Moraes nos anexos da 3ª tentativa.
4. **Delação de João Carlos Mansur** (Reag), enviada pela PGR ao STF em 02/09. Conteúdo ainda não público.

## 9. O que está em jogo e próximos marcos

- **Validade do relatório.** A tese da PGR (e de Moraes) é vício de forma: juiz não investiga, e ministro não manda investigar colega sem o Plenário. Se o Plenário anular, as 218 páginas perdem efeito jurídico, embora já tenham efeito público. Do outro lado, a cadeia de custódia (perito afastado, arquivos "Moraes.pdf") será a linha de ataque das defesas.
- **Quem julga ministro do STF.** Não há rito consolidado. Fachin fala em "medidas cabíveis". O impeachment no Senado depende de Alcolumbre, que não vai pautar.
- **Prazos.** Manifestações de Moraes, Mendonça, Gonet e Andrei: 5 dias úteis a partir de 03/09 (vence por volta de 10–11/09, contando o feriado de 7/9). Sessão do STF: semana de 14/09 em diante. Eleição: 1º turno em 04/10/2026, um mês após a crise.
- **Nova delação de Vorcaro.** Terceira tentativa em preparação; ele quer prisão domiciliar e teme "esquecimento no cárcere". A queda do sigilo enfraqueceu esse pedido.
- **Pontas soltas.** Resposta pública de Mendonça a Moraes; resposta do Planalto sobre Andrei; decisão de Gonet sobre se afastar; conteúdo da delação Mansur; investigação sobre servidores do BC e o grupo "Master".

## 10. Ressalvas de leitura

- As respostas de Moraes em texto não foram recuperadas: a PF prova envio e interação (fotos, apagamentos), não o teor do que ele disse.
- Os valores do contrato variam entre R$ 129 e R$ 131 milhões brutos conforme a fonte; o líquido citado é R$ 108 milhões; o efetivamente recebido até 2025, cerca de R$ 80 milhões.
- "G" = Galípolo é interpretação da PF, não confissão.
- As mensagens de Gonet são "atribuídas", repassadas por Ciro Soares; não há mensagem direta Vorcaro × Gonet no relatório.
- O relatório que Moraes usou contra Mendonça é análise de cenário de inteligência, com relatos anônimos e carimbo "sem valor probatório".
- Parte das reações (Andrei, "cilada", divisão do STF) vem de fontes anônimas em colunas (Natália Portinari/UOL, Tainá Falcão/CNN, Jornal de Brasília).
- Este dossiê foi feito em 04/09 pela manhã; o caso muda por hora.

## 11. Fontes consultadas

- Agência Pública, "As 24h de revelações sobre o Master e Vorcaro e a granada sem pino no STF": https://apublica.org/2026/09/analise-as-revelacoes-sobre-master-vorcaro-moraes-e-mendonca/
- Poder360, retirada do sigilo: https://www.poder360.com.br/poder-justica/mendonca-retira-sigilo-de-acao-sobre-vorcaro-e-moraes/
- Poder360, íntegras: https://www.poder360.com.br/poder-justica/leia-as-integras-de-documentos-que-revelam-relacao-de-moraes-com-vorcaro/
- Poder360, "Vorcaro perguntou a Moraes se deveria fugir": https://www.poder360.com.br/poder-justica/vorcaro-perguntou-a-moraes-se-deveria-fugir-2-dias-antes-da-prisao/
- Poder360, "Ex-ministro alertou Vorcaro": https://www.poder360.com.br/poder-justica/ex-ministro-alertou-vorcaro-sobre-pagamento-a-escritorio-barci-de-moraes/
- Poder360, "Mendonça quis saber o que tinha sobre Moraes": https://www.poder360.com.br/poder-justica/mendonca-quis-saber-o-que-tinha-sobre-moraes-no-celular-de-vorcaro-diz-pf/
- Poder360, nota de Mendonça: https://www.poder360.com.br/poder-justica/mendonca-diz-que-esteve-com-vorcaro-uma-vez-e-que-se-limitou-a-ouvi-lo/
- Poder360, Fachin adia sessão: https://www.poder360.com.br/poder-justica/fachin-adia-sessao-sobre-moraes-para-a-2a-quinzena-de-setembro/
- Poder360, Lula "doa a quem doer": https://www.poder360.com.br/poder-eleicoes-2026/sem-citar-moraes-lula-defende-investigacao-do-master-doa-a-quem-doer/
- Poder360, Flávio "cortina de fumaça": https://www.poder360.com.br/poder-eleicoes-2026/flavio-chama-encontro-de-mendonca-com-vorcaro-de-cortina-de-fumaca/
- Poder360, cúpula da PGR: https://www.poder360.com.br/poder-justica/apos-mencao-a-gonet-cupula-da-pgr-cita-desanimo-com-investigacoes/
- A Investigação, método forense: https://www.ainvestigacao.com/p/relatorio-da-pf-refutou-moraes-sobre-mensagens-de-vorcaro
- JUDIT, dossiê: https://judit.io/jurisprudencia-casos-judiciais/dossie-daniel-vorcaro-ministro-pf/
- Band, investigados e citados: https://www.band.com.br/politica/saiba-quem-sao-os-investigados-e-citados-no-relatorio-da-pf-sobre-vorcaro
- Jornal Grande Bahia, PGR pede nulidade: https://jornalgrandebahia.com.br/2026/09/pgr-pede-nulidade-de-relatorio-da-pf-sobre-moraes-e-vorcaro-enquanto-mensagens-atribuidas-a-gonet-ampliam-crise-no-caso-master/
- Brasil de Fato, Moraes acusa Mendonça: https://www.brasildefato.com.br/2026/09/03/moraes-acusa-mendonca-de-abuso-de-autoridade-e-pede-investigacao-a-fachin/
- Brasil de Fato, Lula: https://www.brasildefato.com.br/2026/09/04/doa-a-quem-doer-lula-defende-investigacao-no-caso-master-e-diz-que-pais-nao-pode-ficar-refem-de-vazamentos-seletivos/
- Brasil de Fato, depoimento sem PF: https://www.brasildefato.com.br/2026/09/02/alem-de-encontro-vorcaro-prestou-depoimento-ao-gabinete-de-mendonca-sem-a-presenca-da-pf-moraes-nao-foi-citado/
- Metrópoles, relatório sem valor probatório: https://www.metropoles.com/brasil/relatorio-da-pf-usado-por-moraes-contra-mendonca-nao-tem-valor-probatorio
- CNN Brasil, revolta de Andrei: https://www.cnnbrasil.com.br/blogs/taina-falcao/politica/diretor-da-pf-demonstra-a-aliados-revolta-com-andre-mendonca/
- CNN Brasil, "amigos" no BC: https://www.cnnbrasil.com.br/politica/vorcaro-dizia-ter-amigos-dentro-do-bc-nao-posso-queima-los/
- CNN Brasil, delação rejeitada: https://www.cnnbrasil.com.br/blogs/matheus-teixeira/politica/doacao-a-bolsonaro-e-tarcisio-eram-propina-acertada-por-kassab-diz-vorcaro/
- CNN Brasil, mercado 02/09: https://www.cnnbrasil.com.br/economia/money/mercado/mercado-financeiro-ibovespa-dolar-2-setembro-2026/
- Jornal de Brasília, divisão do STF: https://jornaldebrasilia.com.br/noticias/politica-e-poder/ministros-do-stf-vivem-impasse-sobre-elo-moraes-vorcaro-e-decisao-inedita-desafia-aliancas-internas/
- Jornal de Brasília, Mendonça pede sessão: https://jornaldebrasilia.com.br/noticias/politica-e-poder/mendonca-pede-a-fachin-sessao-do-stf-para-discutir-mensagens-entre-vorcaro-e-moraes-apontadas-pela-pf/
- Gazeta do Povo, Alcolumbre: https://www.gazetadopovo.com.br/republica/alcolumbre-sinaliza-que-nao-pautara-impeachment-de-moraes-109-pedidos-contra-stf/
- Gazeta do Povo, perito da PF: https://www.gazetadopovo.com.br/republica/agente-pf-produziu-provas-contra-moraes-toffoli-vazaram-imprensa/
- ND Mais, ofício a Lula sobre Andrei: https://ndmais.com.br/politica/oposicao-pressiona-lula-para-demissao-de-andrei-no-comando-da-pf-apos-conversas-citarem-protecao-a-vorcaro/
- ND Mais, Mendonça deixa o Iter: https://ndmais.com.br/justica/andre-mendonca-deixa-sociedade-instituto-iter-vorcaro/
- Revista Fórum, oitiva "forjada": https://revistaforum.com.br/politica/oitiva-forjada-atacar-andrei-pf-fonte-vorcaro
- Revista Fórum, Toffoli, Fux e Kassio: https://revistaforum.com.br/politica/toffoli-fux-kassio-poupados-mendonca-master/
- Revista Oeste, Fachin abre procedimento: https://revistaoeste.com/politica/fachin-abre-procedimento-e-cobra-explicacoes-de-moraes-mendonca-gonet-e-chefe-da-pf/
- Senado Notícias, pedido de impeachment: https://www12.senado.leg.br/noticias/materias/2026/09/01/senadores-pedem-impeachment-do-ministro-alexandre-de-moraes-do-stf
- Diário do Centro do Mundo, delação Freixo: https://www.diariodocentrodomundo.com.br/pgr-delacao-repasses-vorcaro-filme-bolsonaro/
- AC24Horas (reproduz Folha), Vorcaro sinaliza poupar Moraes: https://ac24horas.com/2026/09/04/vorcaro-sinaliza-poupar-moraes-em-nova-delacao-premiada/
- Painel Político, "Caso Master racha o STF": https://painelpolitico.com/caso-master-racha-o-stf-e-atinge-campanha-de-2026
- Wikipedia (en), Banco Master scandal (linha do tempo desde nov/2025): https://en.wikipedia.org/wiki/Banco_Master_scandal

## 12. Davi Alcolumbre, presidente do Senado: o que há e o que não há

Alcolumbre não aparece no relatório de 218 páginas. Ele entra no caso por quatro vias distintas, de pesos muito diferentes.

- **A alegação dos US$ 30 milhões.** Em 11/06/2026 a Veja (Robson Bonin) publicou que Vorcaro teria dito, em proposta de delação, ter transferido US$ 30 milhões (cerca de R$ 153 milhões) a Alcolumbre, em conta no exterior, numa operação conduzida por Augusto Lima, ex-sócio dele, como pagamento por apoio a uma demanda do Master. As duas propostas de delação de Vorcaro foram rejeitadas pela PF e pela PGR por não trazerem provas inéditas. Não há corroboração pública. Alcolumbre: "as informações são absolutamente falsas", "jamais recebi valores, no Brasil ou no exterior". É alegação de réu preso, sem prova conhecida, e assim deve ser lida.
- **Os pedidos de impeachment.** Há 109 pedidos contra ministros do STF no Senado; o de 01/09 contra Moraes, com mais de 80 assinaturas, é o 54º. Em 01/09 Alcolumbre disse que a quantidade "não é normal" e, sobre as mensagens, "não achei nada, não tenho que achar nada". Aliados dizem que ele deixará o caso com o STF. Em 02 e 03/09 ele defendeu Moraes: "todo mundo esqueceu que pediram 130 milhões para as mesmas pessoas para fazer um filme, mas o único culpado é o ministro Alexandre de Moraes"; perguntado a quem se referia: "vocês sabem" (o filme "Dark Horse", seção 8). Sobre a petição de Moraes contra Mendonça, em 03/09: "não achei nada, que eu estou sentado naquela cadeira presidindo a sessão e não sei de nada". O senador Carlos Viana (Podemos-MG) representou contra ele no Conselho de Ética por não dar andamento aos pedidos, com pedido de afastamento cautelar. Não foi encontrada nenhuma declaração dele sobre pautar impeachment de Mendonça.
- **A reunião com Moraes.** Segundo o Metrópoles (04/09), Moraes e Alcolumbre, "que são próximos", se reuniram em Brasília no mesmo dia em que Moraes protocolou a petição contra Mendonça (03/09) e "alinharam o discurso sobre a relatoria de Mendonça no processo do Banco Master".
- **O relatório de inteligência da PF.** O documento que Moraes usou contra Mendonça classifica Alcolumbre como possível "alvo estratégico" de Mendonça, que buscaria "neutralizar o poder do senador sobre a pauta do Senado, especialmente no que diz respeito ao processamento de pedidos de impeachment contra ministros do STF"; cita a desavença de 2021, quando Alcolumbre retardou a sabatina de Mendonça, e aponta Antonio Rueda como "rota de acesso" entre os dois. O próprio documento se classifica como de confiança "baixa ou moderada" e "sem valor probatório" (seção 7).

Alcolumbre tem mandato até 2031 e não concorre em 2026.

## 13. Frentes conexas sob o mesmo relator

Mendonça relata, além da Compliance Zero, a Operação Sem Desconto (descontos indevidos em aposentados do INSS). A petição de Moraes de 03/09 ataca a condução dele nas duas. Por isso três outras frentes entram no mesmo tabuleiro.

- **Master e INSS.** O Master tinha acordo de cooperação técnica com o INSS para crédito consignado (2020 a 2025), suspenso em outubro de 2025: 74% dos contratos, cerca de 250 mil, tinham irregularidades, inclusive empréstimos sem validação de identidade. O cartão consignado Credcesta era operado pela PKL One, que a CPMI do INSS encontrou dentro da rede Reag. O relatório do relator da CPMI do INSS (Alfredo Gaspar, PL-AL, 27/03/2026, 4.340 páginas) pediu o indiciamento de 216 pessoas, entre elas Daniel Vorcaro e Fábio Luís Lula da Silva, mas foi rejeitado pela comissão por 19 a 12; um relatório alternativo com 130 nomes não chegou a ser votado e a CPMI encerrou sem relatório aprovado.
- **Fábio Luís Lula da Silva (Lulinha), filho do presidente.** Três inquéritos da PF: 30/07/2026 (autorizado por Mendonça) por suspeita de tráfico de influência para a World Cannabis, empresa ligada a Antônio Carlos Camilo Antunes, o "Careca do INSS", num projeto de canabidiol do Ministério da Saúde; 31/07 (Mendonça) por favorecimento da 3Structure em contratos com a Dataprev (R$ 55,7 milhões); 04/08 (Flávio Dino) por rede de favorecimento com Marco Aurélio Santana Ribeiro, ex-chefe de gabinete de Lula. A empresária Roberta Luchsinger disse à PF que apresentou Lulinha ao Careca; numa mensagem, o Careca pede R$ 300 mil a uma empresa dela "para o filho do cara". A defesa nega qualquer participação, investimento ou pagamento. Em agosto a PGR pediu que parte do caso vá à 1ª instância, por não haver investigado com foro; críticos leem como forma de tirar o caso de Mendonça. Sem decisão.
- **José Ferreira da Silva (Frei Chico), irmão do presidente.** Vice-presidente do Sindnapi, sindicato de aposentados que, segundo a CPMI, fez 26,4 milhões de descontos em folha entre 2015 e março de 2025, somando R$ 599,5 milhões. O sindicato é investigado por PF e CGU. Frei Chico não é investigado na Sem Desconto; a CPMI rejeitou por 19 a 11 os pedidos de convocação dele (16/10/2025) e não pediu seu indiciamento. Ele processa no TJ-SP quem o associa ao esquema, e há decisão judicial mandando remover publicações. Nada o liga ao Master.

Fontes desta parte: Poder360 (Veja e os US$ 30 milhões; "109 pedidos"), Correio Braziliense e InfoMoney (declarações de 02 e 03/09), Metrópoles (reunião com Moraes; Sindnapi), Congresso em Foco (representação de Viana), Bahia Notícias (relatório de inteligência), Agência Pública (Master e INSS), CNN Brasil (três inquéritos de Lulinha; relatório da CPMI), Gazeta do Povo (parecer da PGR), Câmara dos Deputados (convocação rejeitada), Correio Braziliense e CartaCapital (ações de Frei Chico). Links:
- https://www.poder360.com.br/poder-justica/vorcaro-transferiu-us-30-milhoes-a-alcolumbre-diz-revista/
- https://www.poder360.com.br/poder-congresso/alcolumbre-diz-que-109-pedidos-de-impeachment-contra-stf-nao-e-normal/
- https://www.correiobraziliense.com.br/politica/2026/09/7492796-alcolumbre-manda-recado-sobre-impeachment-de-moraes.html
- https://www.infomoney.com.br/politica/alcolumbre-sobre-pedido-para-investigar-mendonca-nao-achei-nada-nao-sei-decisao/
- https://www.metropoles.com/brasil/alcolumbre-e-moraes-se-reuniram-antes-de-pedido-para-investigar-mendonca
- https://www.congressoemfoco.com.br/noticia/121959/carlos-viana-representa-contra-alcolumbre-no-conselho-de-etica
- https://www.bahianoticias.com.br/justica/noticia/75297-pf-cita-alcolumbre-como-possivel-alvo-estrategico-de-mendonca-para-neutralizar-pauta-de-impeachment-no-stf
- https://apublica.org/2026/03/master-como-cpmi-do-inss-e-cpi-do-crime-organizado-se-conectam/
- https://www.cnnbrasil.com.br/politica/entenda-os-tres-inqueritos-em-que-lulinha-e-investigado/
- https://www.cnnbrasil.com.br/politica/relatorio-da-cpmi-do-inss-pede-indicamento-de-lulinha-e-outras-218-pessoas/
- https://www.gazetadopovo.com.br/republica/parecer-para-enviar-inquerito-de-lulinha-a-1a-instancia-e-manobra-para-afastar-mendonca/
- https://www.metropoles.com/colunas/andreza-matais/sindnapi-de-irmao-de-lula-descontou-r-599-milhoes-do-inss-diz-cpmi
- https://www.camara.leg.br/noticias/1212823-cpmi-do-inss-rejeita-convocacao-de-frei-chico-irmao-de-lula/
- https://www.correiobraziliense.com.br/politica/2025/10/7274683-irmao-de-lula-processa-quem-o-associa-a-esquema-de-descontos-e-critica-cpmi-do-inss.html
- https://www.cartacapital.com.br/justica/justica-manda-remover-publicacoes-que-associam-irmao-de-lula-a-fraudes-no-inss/

## 14. Quem investiga quem: o caso "Dark Horse" passo a passo

O ponto de partida é uma correção: **o relator do inquérito "Dark Horse" é André Mendonça**, indicado por Bolsonaro, e não um ministro indicado por Lula. A disputa pela relatoria foi o contrário do que se supõe: o PT tentou levar o caso para Moraes e perdeu.

| Data | Fato |
|---|---|
| 13/05/2026 | O Intercept Brasil publica áudio e mensagens em que Flávio Bolsonaro pede a Vorcaro R$ 134 milhões (US$ 24 milhões) para o filme sobre o pai. O material vem da extração do celular de Vorcaro, apreendido pela PF em novembro de 2025. Flávio confirmou a autenticidade do áudio, segundo a Agência Pública. Em 09/06 o Intercept publica planilha e comprovante bancário |
| 14/05 | O deputado Helio Lopes (PL-RJ) pede a Mendonça e ao TSE apuração do "vazamento seletivo". O senador Rogério Marinho (PL-RN), coordenador da campanha de Flávio, faz pedido semelhante em maio: origem do material, cadeia de custódia, agentes com acesso. Mendonça determinou a abertura de inquérito sobre os vazamentos, atendendo também à defesa de Vorcaro; foi nesse inquérito que a PF identificou o perito que montou "Moraes.pdf" e "Toffoli e esposa.pdf" e sugeriu vazá-los (seção 1) |
| maio e junho | Mais de vinte pedidos de investigação contra Flávio chegam ao STF (PT, PSOL, Rede). O deputado Lindbergh Farias (PT-RJ) apresenta notícia-crime e pede que seja juntada ao inquérito sobre Eduardo Bolsonaro, relatado por **Moraes** |
| 22/06 | Moraes retira a notícia-crime do inquérito de Eduardo e a envia a Fachin |
| junho | A PGR (Gonet) opina que o caso deve ir a **Mendonça**, por prevenção, porque os fatos já estão numa petição relatada por ele |
| 25/06 | Fachin redistribui o caso a Mendonça |
| 26/06 | Lindbergh recorre. O recurso está no gabinete de Mendonça desde então, sem ir ao plenário |
| 23/07 | Mendonça autoriza a PF a abrir inquérito sobre Vorcaro, Flávio e Eduardo (evasão de divisas, lavagem, corrupção), com parecer da PGR de que havia elementos suficientes |
| junho a agosto, segunda frente | A Polícia Civil de SP faz operação contra a GoUp Entertainment, produtora do filme, por suspeita de fraude em licitação de R$ 108 milhões da Prefeitura de São Paulo vencida pelo Instituto Conhecer Brasil, entidade ligada à GoUp, que recebeu R$ 2 milhões em emendas federais do deputado Mario Frias (PL-SP). Essa frente está no STF por representação da deputada Tabata Amaral (PSB-SP) e é relatada por **Flávio Dino**. Em 21/08 (divulgado 24/08), Dino autoriza a Polícia Civil a compartilhar o material com a PF. Mario Frias nega irregularidade |
| agosto | Vem a público o laudo privado contratado pela GoUp ao perito Anísio Castelo Branco (Instituto de Perícia Investigativa), afirmando que os recursos do filme "possuem origem privada comprovada" e não têm ligação com dinheiro público. Em 26/08, ao Globo, o perito admite não ter auditado o fundo Havengate: "Eu não sei quanto foi enviado do Brasil aos EUA, nem sei se foi enviado, porque eu não estou investigando o fundo". A PF pede à GoUp a origem dos recursos; a produtora encomenda nova perícia |
| 01/09 | A piauí publica relatório do Coaf com mais US$ 1,6 milhão em setembro de 2025; total documentado sobe a US$ 12,3 milhões |
| 01 a 03/09 | Aliados de Lula acusam Mendonça de proteger Flávio por manter o sigilo do Dark Horse enquanto levantou o de Moraes e o de Jaques Wagner (fim de julho). Deputados pedem a Fachin o fim do sigilo. Em 03/09 a PGR homologa a delação de Freixo (malas de dinheiro, Havengate) |

**Onde mais Flávio é investigado.** Moraes abriu inquérito, com parecer favorável da PGR, por suposta difamação contra Lula (declaração de que Lula seria delatado por Maduro). Na delação rejeitada de Vorcaro, a doação de R$ 3 milhões à campanha de 2022 aparece como propina; a PF não aceitou a delação e Flávio nega.

**O que pesa.** Nesta frente, os fatos não sustentam a leitura de que o sistema montou o caso contra Flávio: o áudio é autêntico por confirmação do próprio senador; quem relata é o ministro indicado por Bolsonaro; a PGR e Fachin o mantiveram lá contra a vontade do PT; e o sigilo que o PT quer derrubar é mantido por Mendonça. O que os fatos sustentam é que o celular de Vorcaro, sob custódia da PF, vazou para a imprensa em série ao longo de 2026, e que cada lado pediu apuração do vazamento quando o material atingiu o seu campo.

## 15. A Polícia Federal neste caso: o que pesa contra e o que pesa a favor

A PF não é um bloco, e o registro público tem os dois lados. Abaixo, só o documentado.

**O que pesa contra.**
- **Dezembro de 2025.** Um perito da PF acessou a extração do celular em 01/12, produziu "Moraes.pdf" e "Toffoli e esposa.pdf" em 04/12 e sugeriu à equipe entregá-los à imprensa. Foi alvo de busca em maio e afastado. Ou seja: havia material sobre Moraes identificado dentro da PF desde dezembro.
- **19/02/2026.** O relatório oficial da PF sobre o celular recuperou a nota de 30/10/2025 ("reforçar com Andrei e Paulo"), apontou "Andrei" como o diretor-geral e "Paulo" como o PGR, mas registrou o destinatário só como "interlocutor". Em 06/03 a comunicação do STF negou que fosse Moraes, dizendo que os arquivos estavam "vinculados a pastas de outras pessoas". A identificação formal de Moraes como destinatário só veio em 27/08, em 72 horas, porque Mendonça mandou. O ICL Notícias afirma que o cruzamento de horários entre notas e envios já era possível em março; a PF diz que a análise de agosto "não possui caráter exaustivo". Por que seis meses: é a pergunta aberta, e as duas leituras existem, a de que a PF segurou e a de que não fez o trabalho.
- **25/04/2024.** O diretor-geral Andrei Rodrigues participou em Londres de degustação de Macallan paga por Vorcaro (US$ 640 mil), com Moraes, Toffoli, Gonet e Lewandowski, um ano e meio antes de a PF que ele dirige prender o banqueiro. Não respondeu à imprensa sobre isso.
- **Agosto de 2026.** A PF, sob Andrei, produziu um relatório de inteligência de 50 páginas, sem timbre, sem assinatura e sem data, monitorando a atuação do juiz que relata as investigações em que o próprio Andrei é citado (Compliance Zero) e a Sem Desconto. O documento registra reuniões (uma em 13/08), afirma que Mendonça vê Alcolumbre como "provável alvo estratégico", que Mendonça dizia que Andrei tinha "proximidade inadequada" com Lula e cogitava afastá-lo, que Mendonça questionava a imparcialidade de Gonet por proximidade com Gilmar, que Mendonça recebeu dados brutos em formato forense antes da triagem da PF, e que uma servidora guardava discos rígidos com extrações na própria mesa. A Diretoria-Geral consultou a área jurídica sobre "autonomia administrativa" da corporação diante das ordens do relator. Em 01/09, Moraes, também citado no caso, mandou Andrei lhe enviar os relatórios que mencionassem ministros; a PF enviou; Moraes os usou dois dias depois para pedir a investigação de Mendonça. O próprio relatório se declara de confiança "baixa ou moderada", "sem valor probatório", e diz que "a causa não estaria demonstrada".
- **Reunião de 24/08.** Na PF, ficou conhecida como "cilada": delegados convocados para outro assunto saíram com a ordem de 72 horas. A PF registrou que Mendonça "extrapolou a sua competência". Fontes anônimas da PF chamaram o depoimento de Vorcaro de 27/08 de "oitiva forjada".
- **Vazamentos.** Todo o material que saiu na imprensa em 2026 (Vaza Flávio em maio, áudios sobre Mendonça em setembro, os PDFs sobre ministros) veio de extração sob custódia da PF. Um perito foi afastado; o inquérito sobre os vazamentos segue.

**O que pesa a favor.**
- As 218 páginas que expõem Moraes são trabalho da PF, e a técnica que recuperou as notas apagadas também.
- Em 11/02/2026 foi a PF que pediu o afastamento de Toffoli da relatoria; o STF negou por unanimidade e Toffoli saiu no dia seguinte.
- A PF prendeu Vorcaro duas vezes, rejeitou duas delações que a imprensa descreve como tentativas de conseguir prisão domiciliar, e fez buscas em Jaques Wagner (PT), Ciro Nogueira (PP), Cláudio Castro (PL) e Henrique Vorcaro.
- O inquérito do Dark Horse é conduzido pela PF, e foi a PF que pediu à GoUp a origem do dinheiro e a Dino o acesso aos dados de São Paulo.

**Balanço.** O que está provado é conflito de interesses (o diretor-geral em evento pago pelo investigado), custódia porosa (vazamentos em série e um perito montando dossiês) e uma corporação que passou a monitorar o juiz e a entregar esse monitoramento a um ministro investigado. O que não está provado é que a PF tenha fabricado ou escondido prova por ordem de alguém. "Envolvida até o pescoço" descreve o primeiro conjunto; "mentiras" exigiria o segundo, e ele ainda não existe no registro público.

## 16. Flávio Dino: histórico, alinhamentos e o inquérito das emendas

**Trajetória.** Nascido em São Luís. Apoiador de Lula desde a campanha de 1989, quando presidia o DCE da UFMA. Juiz federal até 2006. Governador do Maranhão por dois mandatos, senador em 2023, ministro da Justiça de Lula de janeiro de 2023 a fevereiro de 2024. Indicado por Lula ao STF, aprovado no Senado por 47 a 31, empossado em 22/02/2024. Integra a 1ª Turma com Moraes (presidente), Zanin, Cármen Lúcia e Fux, a turma que julgou Bolsonaro pela tentativa de golpe; em março de 2025 o plenário rejeitou os pedidos para afastar Moraes, Dino e Zanin daquele julgamento.

**Alinhamentos registrados.** Votou com Moraes, Zanin e Gilmar para liberar parte dos "penduricalhos" barrados pela decisão do STF sobre supersalários. Na crise atual, o Jornal de Brasília o coloca, com Zanin e Gilmar, "firmemente alinhado" a Moraes contra o método de Mendonça, com comparações à Lava Jato. Foi Dino, porém, quem autorizou em 04/08/2026 o terceiro inquérito contra Lulinha, filho do presidente que o indicou, e quem em 21/08 liberou à PF os dados de São Paulo sobre a produtora do Dark Horse.

**O inquérito das emendas.** Dino é relator da ADPF 854, ação do PSOL sobre transparência e rastreabilidade das emendas parlamentares. Em 23/11/2025 determinou que a PF investigasse indícios de crime na execução de emendas. Em maio de 2026 abriu apuração sigilosa. Em 14/07/2026 deu dez dias a Hugo Motta para entregar a documentação das emendas sob suspeita e intimou os presidentes de partidos a explicar se interferem na indicação, depois de Valdemar Costa Neto (PL) confirmar em entrevista que os líderes interferem. A PF apontou que Valdemar, sem mandato, teria controlado 21 emendas de cerca de R$ 119 milhões, e Eduardo Cunha ao menos 29; ambos negam. Em 23/08/2026 Dino declarou nulas as indicações de emendas feitas por presidentes de partido ou ex-parlamentares (as "emendas de líder") e mandou as respostas dos partidos à PF. Motta mobilizou a Câmara para "defender o que está sendo feito"; líderes do centro e da direita leem a ofensiva como capaz de alcançar mais aliados.

**O que pesa.** Que Dino é um ministro de origem política, indicado por Lula e alinhado a Moraes, está documentado. Que ele use o inquérito das emendas "para pressionar o Legislativo" é a leitura de quem é alcançado por ele; o registro mostra uma ação de 2021 do PSOL, decisões sucessivas com prazos, e apurações da PF que atingem o presidente do partido de Flávio. Que ele seja o relator do Dark Horse é falso: ele relata a frente paralela da produtora e das emendas de Mario Frias; o inquérito principal é de Mendonça.

Fontes desta parte: CNN Brasil (PGR defende Mendonça como relator, 22/06; Dino autoriza acesso a dados), JB (redistribuição de Fachin, 25/06), CartaCapital e Metrópoles (recurso de Lindbergh), JOTA (Mendonça abre inquérito; inquérito por difamação), Poder360 (perito do Dark Horse, 26/08; relatório paralelo da PF; íntegra do relatório; como a PF descobriu as mensagens), Metrópoles/Reinaldo Azevedo (petição de Moraes item a item), Jovem Pan (dados brutos antes da análise), ICL Notícias (relatório de 19/02), Gazeta do Povo (perito Nabas; Marinho pede apuração), Metrópoles (Helio Lopes; Motta e as emendas), Band (decisão de Dino, 24/08), STF (ADPF 854; investigação de emendas; vazamento), Agência Brasil e Brasil de Fato (intimação dos partidos; nulidade das emendas de líder), Congresso em Foco e CNN (perfil de Dino), Agência Pública (nota sobre o áudio; escândalo do filme). Links:
- https://www.cnnbrasil.com.br/politica/pgr-defende-mendonca-como-relator-de-pedido-investigacao-sobre-dark-horse/
- https://www.jb.com.br/brasil/justica/2026/06/1060089-fachin-redistribui-caso-dark-horse-e-relatoria-vai-para-andre-mendonca.html
- https://www.cnnbrasil.com.br/politica/lindbergh-recorre-para-evitar-que-mendonca-seja-relator-de-caso-dark-horse/
- https://www.cartacapital.com.br/politica/mendonca-segura-recurso-sigiloso-sobre-o-futuro-do-caso-dark-horse/
- https://www.jota.info/stf/do-supremo/mendonca-abre-investigacao-que-envolve-flavio-bolsonaro-sobre-repasses-ao-filme-dark-horse
- https://www.jota.info/eleicoes/eleicoes-2026/flavio-bolsonaro-sera-investigado-no-stf-por-dizer-que-lula-sera-delatado-por-maduro
- https://www.band.com.br/politica/noticias/dino-autoriza-pf-a-acessar-investigacao-sobre-produtora-do-dark-horse-202608241747
- https://www.poder360.com.br/poder-justica/perito-diz-que-nao-rastreou-origem-de-dinheiro-de-dark-horse/
- https://apublica.org/nota/flavio-bolsonaro-audio-vazado-com-vorcaro-cobra-r-134-milhoes/
- https://www.metropoles.com/brasil/bolsonarista-aciona-stf-para-apurar-audio-de-flavio-a-vorcaro
- https://www.gazetadopovo.com.br/republica/marinho-pede-stf-investigacao-vazamento-mensagens-flavio-vorcaro/
- https://noticias.stf.jus.br/postsnoticias/stf-determina-abertura-de-investigacao-para-apurar-vazamento-de-mensagens-de-celular-de-daniel-vorcaro/
- https://www.diariocarioca.com/2026/09/02/politica/judiciario/mendonca-e-acusado-de-proteger-flavio-bolsonaro-e-pressionado-para-quebrar-sigilo-do-caso-dark-horse
- https://www.poder360.com.br/poder-justica/pf-produziu-relatorio-paralelo-sobre-atuacao-de-mendonca-no-caso-master/
- https://www.poder360.com.br/poder-justica/leia-o-relatorio-da-pf-que-moraes-usou-para-imputar-crimes-a-mendonca/
- https://www.metropoles.com/colunas/reinaldo-azevedo/item-a-item-por-que-moraes-pede-investigacao-de-mendonca-li-o-texto
- https://jovempan.com.br/politica/relatorio-diz-que-mendonca-recebeu-dados-de-processos-antes-da-analise-da-pf/
- https://iclnoticias.com.br/como-pf-ligou-mensagem-de-vorcaro-a-moraes/
- https://www.poder360.com.br/poder-justica/saiba-como-a-pf-descobriu-as-mensagens-de-vorcaro-para-moraes/
- https://www.gazetadopovo.com.br/republica/agente-pf-produziu-provas-contra-moraes-toffoli-vazaram-imprensa/
- https://www.poder360.com.br/poder-justica/moraes-vorcaro-e-andrei-degustaram-macallan-juntos-em-londres/
- https://www.congressoemfoco.com.br/noticia/19105/veja-quem-e-flavio-dino-novo-ministro-do-stf-indicado-por-lula
- https://jornaldebrasilia.com.br/noticias/politica-e-poder/moraes-zanin-dino-e-gilmar-votam-juntos-para-liberar-penduricalhos-que-haviam-sido-barrados-no-stf/
- https://noticias.stf.jus.br/postsnoticias/stf-rejeita-pedidos-para-afastar-ministros-da-analise-de-denuncia-sobre-golpe/
- https://www.transparencia.org.br/noticias/apos-alerta-de-entidades-dino-manda-investigar-possiveis-crimes-com-emendas/
- https://www.correiobraziliense.com.br/politica/2026/05/7420380-dino-determina-abertura-de-investigacao-sigilosa-sobre-emendas-parlamentares.html
- https://agenciabrasil.ebc.com.br/justica/noticia/2026-07/dino-intima-partidos-explicar-controle-de-emendas-parlamentares
- https://www.brasildefato.com.br/2026/08/23/flavio-dino-declara-nulas-emendas-parlamentares-solicitadas-ou-indicadas-por-presidentes-de-partidos-e-envia-respostas-de-partidos-a-pf/
- https://www.metropoles.com/brasil/motta-mobiliza-camara-para-defender-emendas-questionadas-por-dino

---

*Dossiê compilado com auxílio de IA (Claude) a partir exclusivamente de matérias publicadas. Correções e fontes adicionais são bem-vindas via issue ou pull request.*
