import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Configura título e ícone da página
st.set_page_config(
    page_title="Gerenciamento de Dados MongoDB",
    page_icon="🗂️",
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

# Função para excluir todos os documentos de uma coleção
def excluir_todos_dados_mongodb(colecao_nome):
    collection = db[colecao_nome]
    collection.drop()  # Exclui a coleção inteira
    return colecao_nome

# Adiciona título da página
st.title("Gerenciamento de Dados MongoDB")

# Texto de descrição do projeto.
st.markdown("<p style='text-align: justify;'>\
        Esta tela permite visualizar e gerencie todas\
        as bases de dados armazenadas em um banco de dados não\
        relacional, incluindo a opção de excluir conjuntos de\
        dados desnecessários.\
</p>", unsafe_allow_html=True)

# Seleção da coleção
colecoes = db.list_collection_names()
colecao_selecionada = st.selectbox("Selecione uma coleção:", colecoes)

# Variável para armazenar o DataFrame
df = None

if colecao_selecionada:
    st.subheader(f"Visualização dos Dados da Coleção '{colecao_selecionada}'")

    # Carregar e exibir dados
    df = carregar_dados_mongodb(colecao_selecionada)
    st.write(df.head(10))

    st.subheader(f"Baixar os Dados da Coleção '{colecao_selecionada}'")
    # Botão para baixar os dados como CSV
    if not df.empty:
        csv = df.to_csv(index=False)
        st.download_button(
            label="Baixar dados como CSV",
            data=csv,
            file_name=f"{colecao_selecionada}.csv",
            mime="text/csv"
        )

    st.subheader(f"Excluir Dados da Coleção '{colecao_selecionada}'")

    # Botão para excluir todos os dados
    if st.button("Excluir todos os dados"):
        try:
            excluidos = excluir_todos_dados_mongodb(colecao_selecionada)
            st.success(f"{excluidos} documentos foram excluídos com sucesso!")

            # Limpar o DataFrame
            df = pd.DataFrame()  # Atualiza o DataFrame para um DataFrame vazio
            st.write(df)  # Exibe o DataFrame vazio
        except Exception as e:
            st.error(f"Erro ao excluir dados: {e}")

else:
    if df is not None and not df.empty:
        st.subheader(f"Visualização dos Dados da Coleção Selecionada")
        st.write(df)
    else:
        st.warning("Nenhuma coleção selecionada.")
