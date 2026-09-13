# Caso Banco Master

Caderno de acompanhamento do caso Banco Master no Supremo Tribunal Federal.

- `relatorio_dessigilo_2026-09-11.md` e `.html`: relatório completo sobre o levantamento do sigilo de 15 procedimentos da Operação Compliance Zero, decidido por André Mendonça em 10 de setembro de 2026 a pedido de Edson Fachin. Cobre o gatilho da crise (relatório da PF sobre Moraes), a cronologia de 24 de agosto a 11 de setembro, a lista dos procedimentos abertos e dos que seguem sigilosos, o que o material revela frente a frente, as reações, os despachos de Fachin de 11 de setembro e o que está em jogo na sessão de 15 de setembro.
- `documentos/`: íntegras em PDF dos documentos citados, com o texto extraído em `.txt` ao lado dos arquivos mais antigos. Nomes no formato `AAAA-MM-DD_autor_procedimento_assunto`. Alguns documentos do acervo são grandes demais para o repositório — os autos completos de primeira instância (328 MB e 157 MB) e o volume dos habeas corpus da 1ª fase (104 MB), acima do limite de 100 MB do GitHub. Nesses casos o relatório cita o caminho do arquivo dentro do acervo.
- `transcricoes/`: transcrições dos documentos do acervo lidos na íntegra. São vinte e uma, em ordem cronológica dos fatos:
  - `gt_conciliacao_carteiras_brb_2025.md` — os dois relatórios do grupo de trabalho que o BRB montou em fevereiro de 2025, de 4 de abril e 19 de maio, com os lastros assinados no mesmo dia, as averbações que não existiam e a descoberta da Tirreno.
  - `trilha_regulatoria_bcb_fgc_2025.md` — o processo de supervisão do Banco Central sobre o Master (PE 285696), do pedido de socorro ao FGC em abril de 2025 aos atos de liquidação de 18 de novembro.
  - `decisao_1a_instancia_17nov2025_sequestro.md` — a decisão do juiz Ricardo Augusto Soares Leite que autorizou os bloqueios da 1ª fase, e a remessa ao STF em 7 de dezembro.
  - `representacao_operacao_ostap_bender_02out2025.md` — as 126 páginas de 2 de outubro de 2025 que abriram a investigação do DF, sob o nome que a operação tinha antes de virar Compliance Zero.
  - `frente_sao_paulo_ipl_2025_prisao_outubro.md` — a denúncia anônima que abriu a frente de São Paulo e o pedido de prisão de Vorcaro de 21 de outubro de 2025, engolido pela mudança de foro.
  - `decisoes_pet15198_2a_fase_toffoli.md` — as três decisões de Toffoli de janeiro de 2026 sobre a frente de São Paulo, os FIDCs e os bloqueios de R$ 5,77 bilhões.
  - `decisao_compartimentacao_pet15198_19fev2026.md` — a regra de circulação interna de informações na PF, o sigilo nível III, e as decisões sobre a CAE do Senado, a CPI do Crime Organizado e o desmembramento de 6 de julho.
  - `decisao_3marco2026_pet15556_pgr_recusa.md` — a decisão que abriu a 3ª fase e o registro de que a PGR se recusou a endossá-la.
  - `representacao_pf_pet15556_3a_fase.md` — a representação de 164 páginas que abriu a 3ª fase, com a mecânica da "Turma" e a reconstrução de como Vorcaro soube da operação antes dela.
  - `relatorio_bacen_desig_cessoes_master.md` — o laudo do Departamento de Monitoramento do Sistema Financeiro do Banco Central sobre as cessões, com a análise de fluxo financeiro de 1 em 867.
  - `acordao_referendo_2a_turma_23mar2026.md` — as 108 páginas do referendo na Segunda Turma, com o voto-vogal de Gilmar Mendes.
  - `sindicancias_banco_central_belline_paulo_sergio.md` — as duas sindicâncias patrimoniais que o Banco Central abriu contra os próprios servidores da supervisão bancária, concluídas em 4 e 5 de março de 2026.
  - `relatorio_kroll_machado_meyer_brb.md` — o Relatório Final de Investigação Independente que o BRB encomendou, de 31 de março de 2026.
  - `inquerito_projeto_dv_inq5035.md` — o inquérito do "Projeto DV", com a ata notarial de Erechim e o acordo de confidencialidade.
  - `ipja_celular_vorcaro.md` — as duas informações de análise da PF sobre o iPhone apreendido com Vorcaro, de 11 e 12 de março de 2026: a fabricação da versão da Tirreno e os seis imóveis de R$ 146,6 milhões.
  - `relatorio_pf_ipj-a_3298613_2026.md` — o relatório de 218 páginas da PF sobre o celular de Vorcaro.
  - `manifestacao_pgr_pet16662.md` — a manifestação de Gonet pedindo a nulidade do relatório.
  - `oitivas_ipl_banco_central_2026.md` — a portaria do IPL 2026.0053200 e as sínteses das oitivas, entre elas o interrogatório de Vorcaro e o relato da reunião de 3 de dezembro de 2024 com o BTG no Banco Central.
  - `laudos_periciais_agosto_2026.md` — as duas perícias criminais federais de 13 e 14 de agosto de 2026: a Tirreno sem lastro nem conta bancária, e a conclusão pericial de gestão fraudulenta no BRB.
  - `aneabrb_parte_lesada_e_memorial_conselheiro.md` — a disputa civil de abril de 2026 sobre quem fica com o que for recuperado, e o memorial do conselheiro eleito pelos minoritários ao MPF.
  - `decisao_mendonca_08set2026_relatorios_inteligencia.md` — a decisão que afastou os diretores da PF e descreve os relatórios de inteligência.
- `dados/inventario_acervo_stf_2026-09-11.csv`: inventário completo da pasta compartilhada do STF (25,3 GB), extraído pela API de compartilhamento em 11 de setembro de 2026: 4.305 arquivos (4.256 PDFs e 49 vídeos) em 15 pastas, uma por procedimento, com caminho, tamanho, tipo, data e id de cada peça. As pastas maiores são Pet 15198 (1.040 arquivos, 16,3 GB, com cópias de autos de origem em mídia DVD) e Inq 5026 (1.021 arquivos, 3 GB).
- `dados/andamentos_portal_stf_2026-09-11.csv`: índice dos 2.670 andamentos dos 15 procedimentos dessigilados e da Pet 16.704, extraído do portal de consulta processual do STF em 11 de setembro de 2026, com os ids das peças em PDF (`https://portal.stf.jus.br/processos/downloadPeca.asp?id=<id>&ext=.pdf`).

## Como o acesso foi feito

- Portal do STF: `https://portal.stf.jus.br/processos/detalhe.asp?incidente=<n>`; as abas são carregadas de `abaAndamentos.asp`, `abaDecisoes.asp`, `abaPartes.asp` e `abaInformacoes.asp` com o mesmo parâmetro. Incidentes: Pet 15.556 (7514886), Inq 5.026 (7473347), Inq 5.035 (7498168), Rcl 88.121 (7450195), Pet 15.198 (7473336), Pet 15.478 (7505188), Pet 15.504 (7509527), Pet 15.562 (7515623), Pet 15.563 (7515626), Pet 15.693 (7533109), Pet 15.976 (7576883), Pet 15.977 (7576885), Pet 15.978 (7576893), Pet 16.019 (7586934), Pet 16.662 (7681133), Pet 16.704 (7687920).
- O servidor do portal não envia o certificado intermediário "GlobalSign GCC R6 AlphaSSL CA 2025". Clientes de linha de comando precisam adicioná-lo à cadeia (disponível no repositório público da GlobalSign, indicado no campo AIA do certificado). Navegadores completam a cadeia sozinhos.
- Pasta compartilhada do STF com os 25,3 GB: o link publicado na Nota à Imprensa 47 foi trocado pelo STF ao longo de 11 de setembro. O endereço vigente é `https://stfjusbr.sharepoint.com/:f:/s/CompartilhamentoExterno/IgDJRO5i5dOxRIrXcE1u5wd7AfBNkvN1Eo2vIcJOei7LdEM?e=lMrQQi` (site "CompartilhamentoExterno"). O primeiro endereço, no site "STI--CRCS", deixou de funcionar. Abre em navegador.
