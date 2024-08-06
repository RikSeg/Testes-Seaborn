import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Teste do dataset Iris")
    data = pd.read_csv('../data/iris(TEST)/iris.csv')
    st.header('Dataset:')
    st.write(data)

    atributo = st.selectbox("Selecione o atributo para comparação", data.columns[:-1])
    st.header(f"Gráfico de {atributo} por Espécie")

    fig = px.scatter(data, x=atributo, y='species', color='species', title=f'{atributo} vs Espécie')
    st.plotly_chart(fig)

if __name__=="__main__":
    main()