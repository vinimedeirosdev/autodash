import pandas as pd

def carregar_dados(caminho="data/vendas.csv"):
    try:
        df = pd.read_csv(caminho, parse_dates=["data_venda"])
        return df
    except FileNotFoundError:
        print("Arquivo não encontrado:", caminho)
        return pd.DataFrame()
