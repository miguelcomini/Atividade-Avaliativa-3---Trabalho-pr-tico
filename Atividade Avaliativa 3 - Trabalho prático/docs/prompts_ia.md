# Registro de desenvolvimento do grupo e apoio de IA

Ferramenta: Claude (Anthropic), sessão de 13/11/2026. A seção 1 registra essa sessão como ela aconteceu. **Se o grupo usou IA em outros momentos (Prata, DDL, carga, app.py), acrescente essas conversas na tabela com os prompts reais.** Não inclua entradas que não aconteceram.

## 1. Sessão de 13/11/2026 (documentação, EDA e guia do Power BI)

| # | Fase | Técnica | Prompt (resumo) | O que a IA gerou | O que foi conferido ou corrigido |
|---|---|---|---|---|---|
| 1 | Planejamento | Zero-shot, com arquivos anexos | Anexei o `dados.py`, o zip do repositório e o `ocorrencia.csv`, com prints da atividade de Dashboards, e disse que serviam para fazer a atividade final. | Leitura do repositório existente (Bronze, Prata, Ouro e app Streamlit). Duas perguntas de esclarecimento sobre formato e problema; sem preferência, a IA seguiu as opções recomendadas. | Confirmado que o CSV anexado gera a mesma Prata do zip (14.626 linhas). |
| 2 | Escopo | Zero-shot, com PDF anexo | Enviei o guia do projeto prático (PDF) e disse "essa é a atividade". | A IA trocou o plano para a rubrica do guia. Criou README com DER em Mermaid, `.gitignore`, `requirements.txt`, `.env.example`, `sql/eda_queries.sql`, `src/eda.py`, `docs/relatorio_eda.md`, `docs/powerbi_guia.md` e `docs/roteiro_apresentacao.md`. | As 6 consultas SQL foram executadas num SQLite com o mesmo modelo estrela e os resultados bateram com o pandas. |
| 3 | Escopo | Zero-shot | Confirmei que a atividade é só o trabalho prático. | A IA confirmou que não mexeu nas atividades de Dashboards e de Análise Exploratória. | |

## 2. Trabalho realizado e validação pelos integrantes do grupo

Os integrantes do grupo ficaram responsáveis por orientar o desenvolvimento do trabalho, analisar os resultados, conferir os dados e revisar as entregas. As validações e correções descritas abaixo representam a conferência humana realizada sobre os materiais produzidos durante o desenvolvimento. O registro de uso de IA foi mantido para identificar corretamente as etapas em que houve apoio da ferramenta.

## 3. Supervisão humana e limites

Erros da IA encontrados e corrigidos na própria sessão:

- O README dizia 14% de acidentes de 2023 a 2025 com relatório (53 de 483). O correto, recalculado nos dados, é 13% (63 de 483).
- O relatório dizia que a cobertura de relatórios ficava entre 84% e 96% "até 2022". Conferindo a consulta Q2, o correto é 82% a 96% de 2016 a 2022 e 67% a 89% antes.
- Uma frase sobre o tipo de operação dos acidentes fora de aeródromo não tinha base nos dados e foi retirada.
- O percentual de registros sem coordenadas foi corrigido de 30% para 31%.

Não testado: o `load.py` e o `schema.sql` no MySQL, as medidas DAX no Power BI e o `app.py` no Streamlit. O grupo precisa rodar esses três antes de entregar.

## 4. Complementos a serem preenchidos pelo grupo

- Outras conversas com IA (quais prompts, qual técnica, o que mudou no código depois).
- Ao menos um ajuste que o grupo mesmo fez em código sugerido pela IA.
