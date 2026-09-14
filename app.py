import streamlit as st
from utils import carregar_dados, calcular_media_geral, calcular_total_por_categoria

st.title("Dashboard de Vendas")

arquivo = st.file_uploader("Envie um CSV de vendas", type="csv")

if arquivo:
    df = carregar_dados(arquivo)
    st.write("Prévia dos dados:", df.head())
    st.metric("Média de vendas", f"R$ {calcular_media_geral(df):.2f}")
    st.bar_chart(calcular_total_por_categoria(df))