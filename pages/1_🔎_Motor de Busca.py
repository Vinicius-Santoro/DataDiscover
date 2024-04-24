import streamlit as st
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Configurar a API do Kaggle
api = KaggleApi()
api.authenticate()

# Função para buscar conjuntos de dados no Kaggle
def search_datasets(query):
    datasets = api.dataset_list(search=query, file_type='csv')
    return datasets

# Layout do aplicativo
st.title('Motor de Busca de Dados do Kaggle')

# Inicializar a variável datasets como uma lista vazia
datasets = []

# Entrada de texto para o usuário inserir o termo de busca
search_term = st.text_input('Digite o termo de busca:')

# Botão de busca
if st.button('Buscar'):
    st.write(f'Buscando por "{search_term}"...')
    datasets = search_datasets(search_term)
    st.write(f'Encontrados {len(datasets)} conjuntos de dados:')
    for dataset in datasets:
        st.write(dataset.ref)

# # Mostrar informações sobre um conjunto de dados selecionado
dataset_selected = st.selectbox('Selecione um conjunto de dados:', [dataset.ref for dataset in datasets])
# if dataset_selected:
#     st.write(f'Informações sobre o conjunto de dados selecionado ({dataset_selected}):')
#     dataset_info = api.dataset_list_files(dataset_selected)
#     for file_info in dataset_info.files:  # Acessando a propriedade 'files' do objeto 'ListFilesResult'
#         st.write(f'Nome do arquivo: {file_info.name}, Tamanho: {file_info.size}')
#     # Se o usuário quiser baixar o conjunto de dados
#     if st.button('Baixar conjunto de dados'):
#         api.dataset_download_files(dataset_selected, unzip=True)
#         st.write('Conjunto de dados baixado com sucesso!')
