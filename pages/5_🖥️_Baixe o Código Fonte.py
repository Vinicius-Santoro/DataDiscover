import streamlit as st

st.set_page_config(
    page_title="Baixe o Código Fonte",
    page_icon="🖥️",
    layout="wide"
)

st.title("Baixe o Código Fonte")

st.write('#### 1.Clone o repositório', unsafe_allow_html=True)
st.code("git clone git@github.com:Vinicius-Santoro/DataDiscover.git")

st.write('#### 2.Navegue para o diretório do projeto', unsafe_allow_html=True)
st.code("cd DataDiscover")

st.write('#### 3.Instale as dependências', unsafe_allow_html=True)
st.code("pip install -r requirements.txt")

st.write('#### 4.Execute o streamlit', unsafe_allow_html=True)
st.code("python -m streamlit run 0_🏠_Home.py")