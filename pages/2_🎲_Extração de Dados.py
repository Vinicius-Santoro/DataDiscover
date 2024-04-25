import streamlit as st
# from streamlit.server.server import Server
from kaggle.api.kaggle_api_extended import KaggleApi

# Configurar a API do Kaggle
api = KaggleApi()
api.authenticate()

# Função para buscar conjuntos de dados no Kaggle
def search_datasets(query):
    datasets = api.dataset_list(search=query, file_type='csv')
    return datasets

# Texto de boas vindas.
st.write('# Extração de Dados <span style="color: #ff6200"></span>', unsafe_allow_html=True)

# Texto de descrição do projeto.
st.markdown("<p style='text-align: justify;'>\
            O motor de busca possibilita você ter o retorno dos principais artigos publicados no Google Schoolar. \
            Além disso, é apresentado dois indicadores para você ter uma visão analítica de como estão as distribuições.\
</p>", unsafe_allow_html=True)

# Entrada de texto para o usuário inserir o termo de busca
search_term = st.text_input('Digite o termo de busca por conjunto de dados no Kaggle:')

if search_term == "":
    st.info('Esperando um arquivo excel ou csv ser inserido.')
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
            api.dataset_download_files(selected_dataset, unzip=True)
            st.write('Conjunto de dados baixado com sucesso!')
