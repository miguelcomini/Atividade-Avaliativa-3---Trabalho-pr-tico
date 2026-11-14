                       
"""Fase 4 - estatísticas descritivas da camada Prata (complementa sql/eda_queries.sql).
Uso:  python src/eda.py"""
from pathlib import Path
import pandas as pd

SILVER = Path(__file__).resolve().parent.parent / "data" / "silver" / "ocorrencia_limpo.csv"


def main():
    df = pd.read_csv(SILVER, parse_dates=["data_ocorrencia", "data_publicacao"])
    df["ano"] = df["data_ocorrencia"].dt.year
    ac = df[df["ocorrencia_classificacao"] == "ACIDENTE"]
    print(f"Registros: {len(df)} | período: {df.data_ocorrencia.min():%d/%m/%Y} a {df.data_ocorrencia.max():%d/%m/%Y}")
    print("\n== Frequência por classificação ==")
    print(df["ocorrencia_classificacao"].value_counts().to_string())
    print("\n== Acidentes por ano: estatísticas (anos completos 2007-2025) ==")
    por_ano = ac[ac["ano"] <= 2025].groupby("ano").size()
    print(por_ano.describe().round(1).to_string())
    print("\n== Acidentes por ano: média por período ==")
    for a, b in [(2007, 2010), (2011, 2015), (2016, 2022), (2023, 2025)]:
        print(f"{a}-{b}: {por_ano.loc[a:b].mean():.1f}/ano")
    print("\n== Prazo (dias) da ocorrência até a publicação do relatório (acidentes publicados) ==")
    pub = ac.dropna(subset=["data_publicacao"]).copy()
    pub["dias"] = (pub["data_publicacao"] - pub["data_ocorrencia"]).dt.days
    print(pub["dias"].describe().round(0).to_string())
    print("\nMediana por ano de ocorrência (só relatórios já publicados):")
    print(pub.groupby("ano")["dias"].median().loc[2014:2025].to_string())
    print("\n== Investigações ativas ==")
    ref = df["data_ocorrencia"].max()
    at = ac[ac["investigacao_ativa"] == 1]
    print(f"Acidentes com investigação ativa: {len(at)} | acima de 365 dias: {int(((ref - at.data_ocorrencia).dt.days > 365).sum())}")
    print("\n== total_recomendacoes (só ocorrências com >=1) ==")
    r = df.loc[df.total_recomendacoes > 0, "total_recomendacoes"]
    print(r.describe().round(2).to_string())
    print(f"Outliers (IQR) sinalizados: {int(df.outlier_recomendacoes.sum())}")
    print("\n== Saídas de pista ==")
    print(f"Total: {int(df.ocorrencia_saida_pista.sum())} ({df.ocorrencia_saida_pista.mean()*100:.1f}% das ocorrências)")
    print("\n== Acidentes: % fora de aeródromo (FAER) ==")
    print(f"{(ac.ocorrencia_aerodromo == 'FAER').mean()*100:.1f}%")
    print("\n== Dia da semana (acidentes) ==")
    print(ac["data_ocorrencia"].dt.dayofweek.map(dict(enumerate(["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]))).value_counts().to_string())
    print("\n== Acidentes por mês (todos os anos) ==")
    print(ac["data_ocorrencia"].dt.month.value_counts().sort_index().to_string())


if __name__ == "__main__":
    main()
