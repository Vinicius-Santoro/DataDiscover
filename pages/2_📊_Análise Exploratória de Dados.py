import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Configura título e ícone da página. Sidebar inicia expandida
st.set_page_config(
    page_title="Análise Exploratória de Dados",
    page_icon="📊",
    layout="wide"
)

st.title("Análise Exploratória de Dados")

# Upload CSV data
with st.sidebar.header('I. Coletando Dados'):
    uploaded_file = st.sidebar.file_uploader("Insira seu arquivo excel ou csv", type=["csv", "xlsx"])

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv(uploaded_file):
        if '.csv' in uploaded_file.name:
            data = pd.read_csv(uploaded_file, encoding="latin-1", sep=";", low_memory=False)
        elif '.xlsx' in uploaded_file.name:
            data = pd.read_excel(uploaded_file)
        st.success("Arquivo carregado com sucesso.")
        return data
    df = load_csv(uploaded_file)
    pr = ProfileReport(df, explorative=True)
    st.header('**DataFrame Inserido**')
    st.write(df)
    st.write('---')
    st.header('**Análise do Arquivo Inserido**')
    st_profile_report(pr)
else:
    st.info('Esperando um arquivo excel ou csv ser inserido.')
    if st.button('Clique utilizar um exemplo'):
        # Example data
        @st.cache_data
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**DataFrame Inserido**')
        st.write(df)
        st.write('---')
        st.header('**Análise do Arquivo Inserido**')
        st_profile_report(pr)
