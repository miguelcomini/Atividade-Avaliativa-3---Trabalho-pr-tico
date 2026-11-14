# Relatório de Análise Exploratória (EDA)

**Base:** ocorrências aeronáuticas do CENIPA, camada Prata/Ouro · **Registros:** 14.626 · **Período:** 01/01/2007 a 09/05/2026 (2026 é ano parcial).
**Reprodução:** as consultas estão em `sql/eda_queries.sql` (MySQL) e as estatísticas em `python src/eda.py`.

## 1. Estatísticas descritivas

| Classificação | Registros | % |
|---|---|---|
| Incidente | 10.363 | 70,9% |
| Acidente | 3.003 | 20,5% |
| Incidente grave | 1.260 | 8,6% |

**Acidentes por ano (2007–2025, 19 anos completos):** média 154,3 · mediana 153 · desvio padrão 28,6 · mínimo 103 (2007) · máximo 205 (2012).

| Período | Média de acidentes por ano |
|---|---|
| 2007–2010 | 113,0 |
| 2011–2015 | 187,6 |
| 2016–2022 | 151,1 |
| 2023–2025 | 161,0 |

**Outras variáveis**

- Recomendações de segurança (ocorrências com pelo menos 1): média 2,68, mediana 2, Q1 = 1, Q3 = 3, máximo 83. O limite de outlier pelo IQR é 6, e 117 ocorrências passam dele (mantidas e sinalizadas).
- Saídas de pista: 921 registros (6,3% das ocorrências).
- Acidentes fora de aeródromo (código FAER): 61,6%.
- Dados ausentes: 4.568 sem coordenadas (31%, já contando as 146 anuladas por estarem fora do Brasil), 2 sem hora, 25 sem UF.

## 2. Perguntas de negócio

### P1. Os acidentes estão diminuindo?
Consulta: **Q1** (acidentes por ano e classificação).

**Resposta: não.** Houve um salto de 2010 (128) para 2011 (187) e pico em 2012 (205). Desde 2014 ficou estável entre 138 e 175 por ano, e 2023–2025 (155, 175 e 153) está acima de 2022 (138). Sem queda sustentada, a meta de redução precisa de ações novas, e não só de acompanhamento.

### P2. O relatório final chega a tempo de gerar aprendizado?
Consulta: **Q2** (acidentes com relatório publicado e investigações ativas por ano).

**Resposta: não, e piorou.** De 2016 a 2022, entre 82% e 96% dos acidentes de cada ano têm relatório (antes disso, entre 67% e 89%). A partir de 2023 cai para 34% (2023), 5% (2024) e 1% (2025). Somando 2023 a 2025, só 63 de 483 acidentes (13%) têm relatório. Há 466 acidentes com investigação ativa e 320 deles têm mais de 12 meses.

Prazo até a publicação (apenas relatórios já publicados): mediana de 775 dias, média de 1.012. A mediana subiu de 467 dias (ocorrências de 2014) para 907 (2019) e 831 (2022). Os valores de 2024 e 2025 (322 e 354 dias) **não indicam melhora**: só entram os relatórios rápidos, porque os demais ainda não saíram.

### P3. Onde e quando os acidentes acontecem?
Consultas: **Q3** (região e UF) e **Q5** (hora do dia).

**Onde:** SP lidera (595), seguido de MT (323), RS (259), MG (238) e PA (211). Cerca de 62% dos acidentes são fora de aeródromo (FAER). A base não diz o tipo de operação, então não dá para separar por segmento (agrícola, particular etc.).

**Quando:** há dois blocos de pico: 11h–14h (218 a 284 por hora) e 18h–20h, com o máximo às 20h (331). O horário no CENIPA parece estar em UTC (o pico das 20h corresponderia ao fim da tarde no horário de Brasília); confirmar no dicionário de dados da fonte antes de apresentar horários locais. Por dia da semana, sábado concentra mais acidentes (541) e segunda menos (354). Por mês, janeiro lidera (342) e agosto e junho têm os menores números (177 e 179).

### P4. Quais aeródromos concentram mais saídas de pista?
Consulta: **Q4** (sem FAER e sem códigos genéricos NIID/NCAD).

**Resposta:** SBBI (24 saídas em 128 ocorrências), SBJD (16), SBNV (16), SBBP (16), SBMT (14) e SBPR (13). A contagem não é ajustada pelo número de pousos e decolagens, então aeródromos mais movimentados tendem a aparecer mais. Serve para priorizar a atenção, não para ranquear risco.

### P5. Os dados são confiáveis para comparar anos?
Consulta: **Q6** (incidentes por ano).

**Resposta: para acidentes, sim; para incidentes não graves, não a partir de 2023.** Os incidentes saltam de 393 (2022) para 1.176 (2023) e 2.456 (2024), enquanto acidentes e incidentes graves ficam estáveis. Isso sugere mudança no critério ou na obrigação de registro, e não aumento de risco. Por isso o dashboard usa por padrão acidentes e incidentes graves.

## 3. Problemas de qualidade encontrados

- Códigos NIID e NCAD aparecem como aeródromo, mas parecem códigos genéricos (local não identificado). Ficam fora do ranking de aeródromos.
- 146 coordenadas fora do Brasil (provável erro de digitação) foram anuladas na Prata.
- 1 ocorrência com 0 aeronaves envolvidas (inconsistente), sinalizada.
- Sem dados de movimentos de voo, não é possível calcular taxas (ocorrências por 100 mil pousos).

## 4. Ações sugeridas a partir dos achados

| Achado | Ação |
|---|---|
| Acidentes estáveis em ~154 por ano | Concentrar prevenção nas causas recorrentes e em quem opera fora de aeródromo |
| Relatório final chega tarde | Operadores devem usar o histórico (MVP de briefing pré-voo) enquanto o relatório não sai |
| 320 investigações abertas há mais de 12 meses | Priorizar a fila e publicar declaração intermediária |
| Aeródromos reincidentes em saída de pista | Briefing de pista e ponto de arremetida definidos antes do pouso |
