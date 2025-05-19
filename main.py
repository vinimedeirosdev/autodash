import streamlit as st
import pandas as pd
from scripts.etl import carregar_dados
from scripts.graficos import grafico_vendas_por_loja, grafico_produtos_top

st.set_page_config(page_title="AutoDash - Dashboard de Vendas", layout="wide")

st.title("📊 AutoDash - Vendas de Autopeças")
st.markdown("Dashboard interativo com dados de vendas por filial, produto e período.")

# Carrega os dados
df = carregar_dados()

# Filtros
filiais = st.sidebar.multiselect("Filial", df['filial'].unique(), default=df['filial'].unique())
produtos = st.sidebar.multiselect("Produto", df['nome_produto'].unique())
data_ini, data_fim = st.sidebar.date_input("Período", [df['data_venda'].min(), df['data_venda'].max()])

# Filtro aplicado
df_filtrado = df[
    (df['filial'].isin(filiais)) &
    (df['data_venda'] >= pd.to_datetime(data_ini)) &
    (df['data_venda'] <= pd.to_datetime(data_fim))
]
if produtos:
    df_filtrado = df_filtrado[df_filtrado['nome_produto'].isin(produtos)]

# Exibição
st.subheader("📈 Vendas por Loja")
st.plotly_chart(grafico_vendas_por_loja(df_filtrado), use_container_width=True)

st.subheader("🏆 Top Produtos Vendidos")
st.plotly_chart(grafico_produtos_top(df_filtrado), use_container_width=True)

st.subheader("📄 Tabela de Vendas Filtradas")
st.dataframe(df_filtrado)

# Exportação (simples)
if st.button("📥 Exportar para Excel"):
    df_filtrado.to_excel("reports/relatorio_vendas.xlsx", index=True)
    st.success("Relatório exportado para 'reports/relatorio_vendas.xlsx'")
