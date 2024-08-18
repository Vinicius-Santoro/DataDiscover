import streamlit as st
import pandas as pd
from transformers import pipeline
import tempfile

# Função para carregar o modelo de análise de sentimento
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Função para classificar o sentimento
def get_sentiment(text, sentiment_model):
    result = sentiment_model(text)
    label = result[0]['label']
    if label == '1 star' or label == '2 stars':
        return 'Negativo'
    elif label == '3 stars':
        return 'Neutro'
    elif label == '4 stars' or label == '5 stars':
        return 'Positivo'

# Função para converter DataFrame em bytes para download
def converter_df_para_bytes(df):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
        with pd.ExcelWriter(tmp.name, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Resultados')
        tmp.seek(0)
        return tmp.read()

# Carregar o modelo de sentimento
sentiment_model = load_sentiment_model()

# Configuração da aplicação
st.title('Classificação de Sentimento em Colunas de Arquivos')

# Upload do arquivo
uploaded_file = st.file_uploader("Envie seu arquivo CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file:
    # Leitura do arquivo
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Exibir as colunas
    st.write("Colunas disponíveis no arquivo:")
    st.write(df.columns)

    # Seleção da coluna para análise de sentimento
    coluna_selecionada = st.selectbox("Selecione a coluna para classificar o sentimento", df.columns)

    # Botão para confirmar a seleção da coluna
    if st.button('Confirmar Coluna'):
        st.session_state['coluna_confirmada'] = coluna_selecionada
        st.write(f'Coluna "{coluna_selecionada}" confirmada.')

    # Verificar se a coluna foi confirmada
    if 'coluna_confirmada' in st.session_state:
        coluna_confirmada = st.session_state['coluna_confirmada']

        # Botão para classificar sentimento
        if st.button('Classificar Sentimento'):
            # Realizar a classificação de sentimento
            df['Sentimento'] = df[coluna_confirmada].apply(lambda x: get_sentiment(str(x), sentiment_model))

            # Exibir o dataframe com os resultados
            st.write("Resultados da Classificação de Sentimento:")
            st.write(df)

            # Converter o DataFrame para bytes para download
            output_filename = uploaded_file.name.split('.')[0] + '_classificado.xlsx'
            arquivo_bytes = converter_df_para_bytes(df)

            # Botão de download
            st.download_button(
                label="Baixar Arquivo com Sentimento",
                data=arquivo_bytes,
                file_name=output_filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
