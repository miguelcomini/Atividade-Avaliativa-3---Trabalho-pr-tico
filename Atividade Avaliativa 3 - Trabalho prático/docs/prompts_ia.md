# Registro de desenvolvimento do projeto

## 1. Planejamento e organização

O grupo iniciou o trabalho analisando os arquivos disponíveis e o guia do projeto prático. A partir dos requisitos da atividade, foi definida a organização das etapas de desenvolvimento e dos materiais necessários para a entrega.

## 2. Organização e preparação dos dados

O projeto utiliza a base de ocorrências aeronáuticas do CENIPA. Foram consideradas as etapas de organização dos dados nas camadas Bronze, Prata e Ouro, além da estrutura já existente para processamento e visualização.

A base utilizada na validação apresentou 14.626 registros na camada Prata.

## 3. Análise exploratória dos dados (EDA)

Foram elaboradas consultas para investigar os dados e responder às questões propostas no projeto. As análises contemplam a distribuição das ocorrências ao longo dos anos, a localização dos registros e a disponibilidade de relatórios finais.

As consultas SQL foram executadas em uma base SQLite estruturada com o modelo estrela. Os resultados foram comparados com os resultados obtidos por meio do pandas, e as seis consultas verificadas apresentaram resultados correspondentes.

## 4. Modelagem e consultas

O projeto contempla a organização dos dados em um modelo dimensional, com tabelas de dimensão e tabela fato, além de consultas SQL para apoiar a análise. O modelo e as consultas foram organizados para permitir a exploração dos indicadores e sua utilização na etapa de visualização.

## 5. Validação e ajustes

Durante a conferência dos resultados, foram identificadas e ajustadas as seguintes informações:

- O percentual de acidentes de 2023 a 2025 com relatório final foi ajustado para 13%, considerando 63 registros de um total de 483.
- A cobertura de relatórios foi conferida por período: de 82% a 96% entre 2016 e 2022, e de 67% a 89% nos períodos anteriores analisados.
- Foi retirada uma afirmação sobre o tipo de operação dos acidentes fora de aeródromo por não haver dados suficientes para sustentá-la.
- O percentual de registros sem coordenadas foi ajustado para 31%.

## 6. Itens que precisam de verificação final

Antes da entrega, ainda é necessário executar e conferir os seguintes itens nos respectivos ambientes: 

- `load.py` e `schema.sql` no MySQL;
- medidas DAX no Power BI;
- `app.py` no Streamlit.

## 7. Considerações finais

O desenvolvimento foi organizado em etapas de preparação, análise, modelagem e validação dos dados. A conferência dos resultados permitiu corrigir percentuais e retirar interpretações que não eram sustentadas pela base, contribuindo para uma apresentação mais consistente das informações.
