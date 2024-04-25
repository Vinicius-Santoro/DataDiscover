import numpy as np
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
from sklearn.utils._testing import ignore_warnings

# Configura título e ícone da página. Sidebar inicia expandida
st.set_page_config(
    page_title="Análise Exploratória de Dados",
    page_icon="📊",
    layout="wide"
)

# Adiciona título da página
st.title("Análise Exploratória de Dados")

# Recebe o arquivo excel ou csv do usuário
st.header('1. Coletando Dados')
uploaded_file = st.file_uploader("Insira seu arquivo excel ou csv", type=["csv", "xlsx"])

# Gera relatório com pandas profile report
# 1. Se o usuário carregar um arquivo, então:
if uploaded_file is not None:
    # Armazena em cache o report gerado
    @st.cache_data

    # Analisa se o tipo de arquivo é csv ou excel para atribuir para uma variável
    def load_csv(uploaded_file):
        if '.csv' in uploaded_file.name:
            data = pd.read_csv(uploaded_file, encoding="latin-1", sep=";", low_memory=False)
        elif '.xlsx' in uploaded_file.name:
            data = pd.read_excel(uploaded_file)

        # Mensagem de sucesso de carregou com sucesso
        st.success("Arquivo carregado com sucesso.")
        return data
        
    # Atribui o arquivo para a variável df
    df = load_csv(uploaded_file)

    # Gerando profile report com o df carregado pelo usuário.
    pr = ProfileReport(df, explorative=True)
    st.header('**DataFrame Inserido**')

    # Printando DataFrame na tela
    st.write(df)
    st.write('---')
    st.header('**Análise do Arquivo Inserido**')

    # Printando profile report com o df carregado pelo usuário.
    st_profile_report(pr)

# 2. Se o usuário não carregar um arquivo, então vai utilizar um template:
else:
    st.info('Esperando um arquivo excel ou csv ser inserido.')
    if st.button('Clique para utilizar um exemplo'):
        # Armazena em cache o report gerado
        @st.cache_data

        # Gera um dataframe de exemplo
        def load_data():
            a = pd.DataFrame(

                # Cria um dataframe de 10 linhas e 5 colunas com números reais aleatórios
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        
        # Atribui o arquivo para a variável df
        df = load_data()

        # Gerando profile report com o df de exemplo
        pr = ProfileReport(df, explorative=True)
        st.header('**DataFrame Inserido**')

        # Printando DataFrame na tela
        st.write(df)
        st.write('---')
        st.header('**Análise do Arquivo Inserido**')

        # Printando profile report com o df de exemplo.
        st_profile_report(pr)
