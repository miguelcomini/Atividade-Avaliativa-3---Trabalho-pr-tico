# Roteiro da apresentação (10 a 15 min)

1. **Problema (1 min):** acidentes não caem e o relatório final chega tarde. Quem usa: gerente de segurança operacional.
2. **Bronze e Prata (3 min):** mostrar `data/raw` intocado e rodar `python src/transform.py`. Citar 3 tratamentos: UF ausente, coordenadas fora do Brasil, colunas duplicadas.
3. **Ouro no MySQL (3 min):** mostrar o DER do README, o `schema.sql` (PK, FK, UNIQUE, CHECK) e rodar `python src/load.py`. Mostrar `SELECT COUNT(*)` na fato = 14.626.
4. **EDA (2 min):** executar uma consulta de `sql/eda_queries.sql` (Q2) e comentar que 63 de 483 acidentes de 2023–2025 têm relatório.
5. **Dashboard (3 min):** KPIs, tendências, detalhe, filtros. Mostrar a ação ligada a um indicador vermelho.
6. **MVP (1 min):** briefing pré-voo por aeródromo e horário (aba do `app.py`).
7. **Limitações e IA (1 min):** sem taxa por voos; como a IA foi usada e conferida.

Perguntas prováveis: por que esquema estrela? Por que não imputar coordenadas? O que é o outlier de recomendações? Por que incidentes ficam fora do filtro padrão?
