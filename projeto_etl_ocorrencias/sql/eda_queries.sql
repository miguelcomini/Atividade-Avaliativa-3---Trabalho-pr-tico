



SELECT t.ano, c.nome AS classificacao, COUNT(*) AS qtd
FROM fato_ocorrencia f
JOIN dim_tempo t ON t.id_data = f.id_data
JOIN dim_classificacao c ON c.id_classificacao = f.id_classificacao
GROUP BY t.ano, c.nome
ORDER BY t.ano, c.nome;


SELECT t.ano,
       COUNT(*) AS acidentes,
       SUM(f.relatorio_publicado) AS com_relatorio,
       ROUND(100.0 * SUM(f.relatorio_publicado) / COUNT(*), 1) AS pct_com_relatorio,
       SUM(f.investigacao_ativa) AS investigacoes_ativas
FROM fato_ocorrencia f
JOIN dim_tempo t ON t.id_data = f.id_data
JOIN dim_classificacao c ON c.id_classificacao = f.id_classificacao
WHERE c.nome = 'ACIDENTE'
GROUP BY t.ano
ORDER BY t.ano;


SELECT u.regiao, u.sigla AS uf, COUNT(*) AS acidentes
FROM fato_ocorrencia f
JOIN dim_cidade ci ON ci.id_cidade = f.id_cidade
JOIN dim_uf u ON u.id_uf = ci.id_uf
JOIN dim_classificacao c ON c.id_classificacao = f.id_classificacao
WHERE c.nome = 'ACIDENTE'
GROUP BY u.regiao, u.sigla
ORDER BY acidentes DESC
LIMIT 10;


SELECT a.codigo, COUNT(*) AS ocorrencias, SUM(f.saida_pista) AS saidas_de_pista
FROM fato_ocorrencia f
JOIN dim_aerodromo a ON a.id_aerodromo = f.id_aerodromo
WHERE a.codigo NOT IN ('FAER', 'NIID', 'NCAD', 'NÃO INFORMADO')
GROUP BY a.codigo
ORDER BY saidas_de_pista DESC, ocorrencias DESC
LIMIT 10;


SELECT f.hora_dia, COUNT(*) AS acidentes
FROM fato_ocorrencia f
JOIN dim_classificacao c ON c.id_classificacao = f.id_classificacao
WHERE c.nome = 'ACIDENTE' AND f.hora_dia IS NOT NULL
GROUP BY f.hora_dia
ORDER BY f.hora_dia;


SELECT t.ano, COUNT(*) AS incidentes
FROM fato_ocorrencia f
JOIN dim_tempo t ON t.id_data = f.id_data
JOIN dim_classificacao c ON c.id_classificacao = f.id_classificacao
WHERE c.nome = 'INCIDENTE'
GROUP BY t.ano
ORDER BY t.ano;
