# Guia do Dashboard no Power BI

O Power BI Desktop precisa ser aberto no seu computador (Windows). Este guia traz tudo que é preciso para montar o painel: conexão, relacionamentos, medidas DAX e layout. As medidas foram escritas com base no esquema do `sql/schema.sql`, mas **não foram executadas no Power BI**: teste cada uma e ajuste se algum valor divergir da tabela de conferência no final.

## 1. Conexão com o MySQL

1. Instale o conector MySQL (MySQL Connector/NET) se o Power BI pedir.
2. **Obter dados → Banco de dados MySQL**. Servidor `localhost`, banco `ocorrencias_aeronauticas`, modo **Importar**.
3. Selecione as 6 tabelas: `fato_ocorrencia`, `dim_classificacao`, `dim_aerodromo`, `dim_tempo`, `dim_cidade`, `dim_uf`.

## 2. Modelo (Exibição de Modelo)

Relacionamentos 1:N, filtro em uma direção (da dimensão para a fato):

| De (1) | Para (N) |
|---|---|
| `dim_classificacao[id_classificacao]` | `fato_ocorrencia[id_classificacao]` |
| `dim_aerodromo[id_aerodromo]` | `fato_ocorrencia[id_aerodromo]` |
| `dim_tempo[id_data]` | `fato_ocorrencia[id_data]` |
| `dim_cidade[id_cidade]` | `fato_ocorrencia[id_cidade]` |
| `dim_uf[id_uf]` | `dim_cidade[id_uf]` |

Observação: `dim_tempo` só tem as datas que têm ocorrência (não é um calendário contínuo). Por isso **não marque como tabela de datas** e evite funções como `SAMEPERIODLASTYEAR`; as medidas abaixo usam a coluna `ano`.

## 3. Medidas DAX

Crie uma tabela de medidas (Inserir dados → tabela vazia `_Medidas`) e adicione:

```dax
Total Ocorrências = COUNTROWS ( fato_ocorrencia )

Acidentes =
CALCULATE ( [Total Ocorrências], dim_classificacao[nome] = "ACIDENTE" )

Incidentes Graves =
CALCULATE ( [Total Ocorrências], dim_classificacao[nome] = "INCIDENTE GRAVE" )

Saídas de Pista = SUM ( fato_ocorrencia[saida_pista] )

Data Mais Recente =
CALCULATE ( MAX ( dim_tempo[data] ), REMOVEFILTERS ( dim_tempo ) )

Acidentes Últimos 12 Meses =
VAR ult = [Data Mais Recente]
RETURN
    CALCULATE (
        [Acidentes],
        REMOVEFILTERS ( dim_tempo ),
        dim_tempo[data] > EDATE ( ult, -12 ),
        dim_tempo[data] <= ult
    )

Média Anual Acidentes 2019-2024 =
CALCULATE (
    DIVIDE ( [Acidentes], DISTINCTCOUNT ( dim_tempo[ano] ) ),
    REMOVEFILTERS ( dim_tempo ),
    dim_tempo[ano] >= 2019,
    dim_tempo[ano] <= 2024
)

Variação % vs Ano Anterior =
VAR a = MAX ( dim_tempo[ano] )
VAR ant = CALCULATE ( [Acidentes], REMOVEFILTERS ( dim_tempo ), dim_tempo[ano] = a - 1 )
RETURN DIVIDE ( [Acidentes] - ant, ant )

Acidentes Acumulado no Ano =
CALCULATE (
    [Acidentes],
    FILTER (
        ALL ( dim_tempo ),
        dim_tempo[ano] = MAX ( dim_tempo[ano] )
            && dim_tempo[data] <= MAX ( dim_tempo[data] )
    )
)

Acidentes com Relatório =
CALCULATE (
    SUM ( fato_ocorrencia[relatorio_publicado] ),
    dim_classificacao[nome] = "ACIDENTE"
)

% Acidentes com Relatório = DIVIDE ( [Acidentes com Relatório], [Acidentes] )

% Relatório 2023-2025 =
CALCULATE (
    [% Acidentes com Relatório],
    REMOVEFILTERS ( dim_tempo ),
    dim_tempo[ano] >= 2023,
    dim_tempo[ano] <= 2025
)

Investigações Ativas =
CALCULATE (
    SUM ( fato_ocorrencia[investigacao_ativa] ),
    dim_classificacao[nome] = "ACIDENTE"
)

Investigações Ativas > 12 Meses =
VAR ult = [Data Mais Recente]
RETURN
    CALCULATE (
        COUNTROWS ( fato_ocorrencia ),
        fato_ocorrencia[investigacao_ativa] = 1,
        dim_classificacao[nome] = "ACIDENTE",
        REMOVEFILTERS ( dim_tempo ),
        dim_tempo[data] < EDATE ( ult, -12 )
    )

% Acidentes Fora de Aeródromo =
DIVIDE (
    CALCULATE ( [Acidentes], dim_aerodromo[fora_aerodromo] = 1 ),
    [Acidentes]
)

Cor KPI Acidentes =
SWITCH (
    TRUE (),
    [Acidentes Últimos 12 Meses] <= [Média Anual Acidentes 2019-2024], "#2E8B57",
    [Acidentes Últimos 12 Meses] <= [Média Anual Acidentes 2019-2024] * 1.15, "#F2A900",
    "#D6342C"
)
```

Use `Cor KPI Acidentes` em **Formato condicional → Cor da fonte → Valor do campo** no cartão de acidentes.

### Valores de conferência

Se as medidas estiverem certas, sem filtros, os valores devem bater com estes (calculados na camada Prata):

| Medida | Valor esperado |
|---|---|
| Total Ocorrências | 14.626 |
| Acidentes | 3.003 |
| Saídas de Pista | 921 |
| Acidentes Últimos 12 Meses | 157 |
| Média Anual Acidentes 2019-2024 | 151,8 |
| % Relatório 2023-2025 | 13,0% |
| Investigações Ativas | 466 |
| % Acidentes Fora de Aeródromo | 61,6% |

(Investigações ativas > 12 meses: 320 com corte de 365 dias; o `EDATE` pode diferir em 1 ou 2.)

## 4. Layout da página (regra dos 5 segundos)

**Título e contexto (topo):** "Segurança de voo no Brasil: o aprendizado está chegando a tempo?" e, ao lado, "Fonte: CENIPA · dados até 09/05/2026 · atualização mensal (carga manual do ETL)".

**Faixa de KPIs (5 cartões grandes):** Acidentes (12 meses) com semáforo · Investigações abertas há mais de 12 meses · % acidentes 2023–2025 com relatório · Saídas de pista no ano · % acidentes fora de aeródromo. Cada cartão com uma linha de ação ("Se vermelho: ...").

**Meio (tendências):**
- Colunas empilhadas: acidentes por ano e classificação (eixo `dim_tempo[ano]`, legenda `dim_classificacao[nome]`).
- Colunas: % de acidentes com relatório por ano (`% Acidentes com Relatório`).
- Colunas: acidentes por hora do dia (`fato_ocorrencia[hora_dia]`).

**Base (detalhe):**
- Tabela de aeródromos com saídas de pista (filtro visual: excluir FAER, NIID, NCAD).
- Barras: acidentes por UF.
- Mapa de bolhas com `latitude` e `longitude` (31% dos registros não têm coordenadas).

**Filtros (segmentações):** ano, classificação (padrão: acidente e incidente grave), região. Dica: deixe incidentes fora do padrão por causa do salto de registros em 2023.

## 5. Publicação

Para demonstrar ao vivo, abra o `.pbix` com o MySQL ligado. Para o repositório, salve o `.pbix` em `powerbi/` (ou prints em `docs/img/`).
