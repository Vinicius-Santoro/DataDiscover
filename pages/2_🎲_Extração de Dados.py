import os
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from pymongo import MongoClient

st.set_page_config(
    page_title="Extração de Dados",
    page_icon="🎲",
    layout="wide",
)

# Configurar a API do Kaggle
api = KaggleApi()
api.authenticate()

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['meu_banco_de_dados']

# Função para buscar conjuntos de dados no Kaggle
def search_datasets(query):
    datasets = api.dataset_list(search=query, file_type='csv')
    return datasets

# Texto de boas-vindas
st.write('# Extração de Dados <span style="color: #ff6200"></span>', unsafe_allow_html=True)

# Texto de descrição do projeto
st.markdown("<p style='text-align: justify;'>\
            A extração de dados permite obter bases de dados diretamente do Kaggle, \
            proporcionando dataframes prontos para testes com as demais ferramentas do DataDiscover.\
</p>", unsafe_allow_html=True)

# Entrada de texto para o usuário inserir o termo de busca
search_term = st.text_input('Digite o termo de busca por conjunto de dados no Kaggle:')

if search_term == "":
    st.button('Buscar')
else:
    # Botão de busca
    st.write(f'Buscando por "{search_term}"...')
    datasets = search_datasets(search_term)
    dataset_names = [dataset.ref for dataset in datasets]
    selected_dataset = st.selectbox('Selecione um conjunto de dados:', dataset_names) if datasets else None
    if selected_dataset:
        st.write(f'Você selecionou o conjunto de dados: {selected_dataset}')
        dataset_info = api.dataset_list_files(selected_dataset)
        if st.button('Baixar conjunto de dados'):
            # Obtém o caminho absoluto para a pasta de downloads
            download_path = os.path.join(os.path.expanduser("~"), "Downloads")
            # Define o caminho de destino para o download (apenas o arquivo)
            destination_path = os.path.join(download_path, selected_dataset.split('/')[-1])
            api.dataset_download_files(selected_dataset, path=destination_path, unzip=True)

            # Após o download, ler o arquivo CSV baixado
            csv_file_path = os.path.join(destination_path, os.listdir(destination_path)[0])
            df = pd.read_csv(csv_file_path)

            # Armazenar no MongoDB usando o nome do conjunto de dados como o nome da coleção
            collection_name = selected_dataset.replace('/', '_')
            collection = db[collection_name]
            collection.insert_many(df.to_dict(orient='records'))

            st.success(f'Conjunto de dados "{selected_dataset}" baixado e armazenado com sucesso no banco de dados!')