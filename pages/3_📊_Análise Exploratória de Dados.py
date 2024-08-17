import os
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
from pymongo import MongoClient

# Configura título e ícone da página. Sidebar inicia expandida
st.set_page_config(
    page_title="Análise Exploratória de Dados",
    page_icon="📊",
    layout="wide"
)

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['meu_banco_de_dados']

# Função para carregar dados de uma coleção específica
def carregar_dados_mongodb(colecao_nome):
    collection = db[colecao_nome]
    dados = list(collection.find({}, {"_id": 0}))  # Exclui o campo '_id'
    return pd.DataFrame(dados)

# Adiciona título da página
st.title("Análise Exploratória de Dados")

# Recebe o arquivo excel ou csv do usuário
st.subheader('1. Coleta de Dados')
uploaded_file = st.file_uploader("Insira seu arquivo xlsx ou csv", type=["csv", "xlsx"])

# Verifica se o arquivo carregado é um CSV
if uploaded_file is not None and uploaded_file.type == "text/csv":
    # Adiciona widgets para selecionar encoding e separador
    user_encoding = st.selectbox("Selecione o encoding:", ["utf-8", "latin1", "ISO-8859-1"])
    user_separator = st.text_input("Digite o separador (padrão é ';'):", ';')

# Gera relatório com pandas profile report
# 1. Se o usuário carregar um arquivo, então:
if uploaded_file is not None:
    # Armazena em cache o report gerado
    @st.cache_data

    # Analisa se o tipo de arquivo é csv ou excel para atribuir para uma variável
    def load_csv(uploaded_file,  user_encoding,  user_separator):
        if '.csv' in uploaded_file.name:
            data = pd.read_csv(uploaded_file, encoding=user_encoding, sep=user_separator, low_memory=False)
        elif '.xlsx' in uploaded_file.name:
            data = pd.read_excel(uploaded_file)

        # Mensagem de sucesso de carregou com sucesso
        st.success("Arquivo carregado com sucesso.")
        return data

    if uploaded_file.type == "text/csv":
        # Atribui o arquivo para a variável df
        df = load_csv(uploaded_file, user_encoding, user_separator)
    else:
        df = pd.read_excel(uploaded_file)

    # Botão de confirmação
    if st.button("Confirmar e Analisar"):
        # Gerando profile report com o df carregado pelo usuário.

        st.info('Esperando um arquivo xlsx ou csv ser inserido.')
        pr = ProfileReport(df, explorative=True)
        st.subheader('2. Visualização do Dataframe')

        # Printando DataFrame na tela
        st.write(df)
        st.write('---')
        st.header('**Análise do Arquivo Inserido**')

        # Printando profile report com o df carregado pelo usuário.
        st_profile_report(pr)

# 2. Se o usuário não carregar um arquivo, então vai utilizar um template:
else:
    
    # Adiciona a funcionalidade de selecionar bases de dados armazenadas no MongoDB
    st.subheader('2. Seleção de Base de Dados Armazenada')


    # Listar as coleções disponíveis no MongoDB
    colecoes = db.list_collection_names()

    # Verifica se há coleções disponíveis
    if colecoes:
        colecao_selecionada = st.selectbox("Selecione uma base de dados:", colecoes)

        if colecao_selecionada and st.button("Confirmar e Analisar"):
            df = carregar_dados_mongodb(colecao_selecionada)
            
            st.success(f"Base de dados '{colecao_selecionada}' carregada com sucesso!")

            # Gerando profile report com o df selecionado pelo usuário.
            pr = ProfileReport(df, explorative=True)
            st.subheader('3. Visualização do Dataframe')

            # Printando DataFrame na tela
            st.write(df)
            st.write('---')
            st.header('**Análise da Base de Dados Selecionada**')

            # Printando profile report com o df carregado pelo usuário.
            st_profile_report(pr)
    else:
        st.warning("Nenhuma base de dados armazenada encontrada.")

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
        st.subheader('2. Visualização do Dataframe')

        # Printando DataFrame na tela
        st.write(df)
        st.write('---')
        st.subheader('3. Análise Exploratória dos Dados')

        # Printando profile report com o df de exemplo.
        st_profile_report(pr)
