import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="DataDiscover",
    page_icon="🏠",
    initial_sidebar_state="expanded",
)

st.write('# Bem vindo ao <span style="color: #ff6200">DataDiscover</span>', unsafe_allow_html=True)

st.write('#### O que é nosso projeto?', unsafe_allow_html=True)

# Não utilizar markdown com cores preto ou branco por conta do dark/light mode
st.markdown("<p style='text-align: justify;'>\
            O DataDiscover é um site que centraliza três ferramentas projetadas especificamente \
            para estudantes e entusiastas de ciência de dados. Nosso objetivo é simplificar e aprimorar \
            a experiência de aprendizado e prática nessa área. \
</p>", unsafe_allow_html=True)

st.write('#### Recursos principais', unsafe_allow_html=True)

st.markdown("<p style='text-align: justify;'>\
        Clique em cada uma das ferramentas para saber mais. \
</p>", unsafe_allow_html=True)
