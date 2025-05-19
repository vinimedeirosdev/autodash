import plotly.express as px

def grafico_vendas_por_loja(df):
    df_agg = df.groupby("filial")["valor"].sum().reset_index()
    fig = px.bar(df_agg, x="filial", y="valor", color="filial",
                 title="Total de Vendas por Filial", labels={"valor": "Valor (R$)"})
    return fig

def grafico_produtos_top(df, top_n=5):
    df_agg = df.groupby("nome_produto")["valor"].sum().reset_index()
    df_agg = df_agg.sort_values(by="valor", ascending=False).head(top_n)
    fig = px.pie(df_agg, values="valor", names="nome_produto",
                 title=f"Top {top_n} Produtos Vendidos")
    return fig