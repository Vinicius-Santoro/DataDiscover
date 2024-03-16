import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="DataDiscover",
    page_icon="🏠",
    initial_sidebar_state="expanded",
)

st.write('# Bem vindo ao <span style="color: #ff6200">DataDiscover</span>', unsafe_allow_html=True)

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

with st.expander("Motor de Busca"):
    st.markdown("<p style='text-align: justify;'>\
            O motor de busca possibilita você ter o retorno dos principais artigos publicados no Google Schoolar. \
            Além disso, é apresentado dois indicadores para você ter uma visão analítica de como estão as distribuições.\
    </p>", unsafe_allow_html=True)

with st.expander("Análise Exploratória de Dados"):
    st.markdown("<p style='text-align: justify;'>\
            A ferramenta de análise exploratória de dados é uma aliada valiosa para analistas e cientista de dados.  \
            Com ela, você pode importar um arquivo Excel ou CSV contendo seus dados brutos e obter uma análise detalhada do seu dataframe.\
            Ela revela padrões, tendências e insights ocultos, permitindo que você compreenda melhor a estrutura dos seus dados.\
             A partir dessa análise, você pode tomar decisões informadas sobre limpeza, transformação e visualização dos dados. \
    </p>", unsafe_allow_html=True)

with st.expander("Relatório de Performance de Modelo"):
    st.markdown("<p style='text-align: justify;'>\
            Imagine que você está construindo modelos de machine learning para resolver um problema específico. \
            O relatório de performance de modelo entra em cena exatamente nesse momento. \
            Basta inserir um arquivo Excel ou CSV e  \
            você descobrirá como seu dataframe se comportaria em 20 diferentes modelos de machine learning. \
            Essa análise inclui métricas de acurácia, precisão, recall e F1-score, permitindo que você escolha o modelo mais adequado para o seu cenário.\
    </p>", unsafe_allow_html=True)

st.write('#### Informações sobre o projeto', unsafe_allow_html=True)
st.markdown("<p style='text-align: justify;'>\
        Esse projeto foi desenvolvido como requisito para obtenção de nota para a disciplina \
        Projeto Integrador III, da Faculdade de Tecnologia de São Paulo (Fatec),\
        do curso de ciência de dados, quarto semestre, período noturno.\
            \
</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: justify;'>\
            •   Alunos: Henrique Oliveira Neves e Vinicius Naziozeno Santoro do Rio.\
</p>", unsafe_allow_html=True)

st.markdown("<p style='text-align: justify;'>\
            •   Orientador: Professora Rosineide Aparecida de Lira Volgarin. \
</p>", unsafe_allow_html=True)