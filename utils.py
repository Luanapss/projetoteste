import pandas as pd

def carregar_dados(caminho_csv):
    return pd.read_csv(caminho_csv)

def calcular_media_geral(df):
    return df["valor"].mean()

def calcular_total_por_categoria(df):
    return df.groupby("categoria")["valor"].sum()