import streamlit as st
from PIL import Image

# Configura título e ícone da página. Sidebar inicia expandida.
st.set_page_config(
    page_title="DataDiscover",
    page_icon="🏠",
    initial_sidebar_state="expanded",
    layout="wide"
)

# Texto de boas vindas.
st.write('# Bem vindo ao <span style="color: #ff6200">DataDiscover</span>', unsafe_allow_html=True)

# Texto de descrição do projeto.
st.markdown("<p style='text-align: justify;'>\
            O DataDiscover é um site que centraliza quatro ferramentas projetadas especificamente \
            para estudantes e entusiastas de ciência de dados. Nosso objetivo é simplificar e aprimorar \
            a experiência de aprendizado e prática nessa área. \
</p>", unsafe_allow_html=True)

# Texto de recursos principais.
st.write('#### Recursos principais', unsafe_allow_html=True)
st.markdown("<p style='text-align: justify;'>\
        Clique em cada uma das ferramentas para saber mais. \
</p>", unsafe_allow_html=True)

# Texto de explicação do motor de busca, com expander.
with st.expander("🔎 Motor de Busca"):
    st.markdown("<p style='text-align: justify;'>\
        O motor de busca permite acessar os principais artigos publicados no Google Scholar.  \
        Além disso, são apresentados dois indicadores que oferecem uma visão analítica das distribuições.\
    </p>", unsafe_allow_html=True)
    
# Texto de explicação de extração de dados, com expander.
with st.expander("🎲 Extração de Dados"):
    st.markdown("<p style='text-align: justify;'>\
            A extração de dados permite obter bases de dados diretamente do Kaggle, \
            proporcionando dataframes prontos para testes com as demais ferramentas do DataDiscover.\
    </p>", unsafe_allow_html=True)

# Texto de explicação da análise exploratória de dados, com expander.
with st.expander("📊 Análise Exploratória de Dados"):
    st.markdown("<p style='text-align: justify;'>\
        A ferramenta de análise exploratória de dados é interessante para analistas e cientistas de dados porque\
        é possível importar arquivos Excel ou CSV contendo dados brutos e obter uma análise detalhada do dataframe.\
        A ferramenta revela padrões, tendências e insights ocultos, permitindo uma compreensão mais profunda da estrutura dos dados.\
        Com base nessa análise, você pode tomar decisões informadas sobre limpeza, transformação e visualização dos dados.\
    </p>", unsafe_allow_html=True)

# Texto de explicação do relatório de performance do modelo, com expander.
with st.expander("📃 Relatório de Performance de Modelo"):
    st.markdown("<p style='text-align: justify;'>\
            Imagine que você está construindo modelos de regressão para resolver um problema específico. \
         O relatório de performance de modelo te auxilia nesse momento. \
         Basta inserir um arquivo xlsx ou CSV e você descobrirá como seu dataframe se comportaria em \
         mais de 20 diferentes modelos de machine learning. Essa análise inclui as métricas de avaliação, \
         <b>R-Quadradro Ajustado</b>, <b>R-Quadradro</b> e <b>RMSE</b>, permitindo que você escolha o modelo mais adequado para o seu cenário. \
    </p>", unsafe_allow_html=True)

st.write('#### Possíveis perguntas', unsafe_allow_html=True)

message = st.chat_message("user")
message.write("Por que esse projeto foi desenvolvido?")

message = st.chat_message("assistant")
message.write("\
        Esse projeto foi desenvolvido como requisito para obtenção de nota para a disciplina \
        Projeto Integrador III, da Faculdade de Tecnologia de São Paulo (Fatec),\
        do curso de ciência de dados, quarto semestre, período noturno.\
              ")

message = st.chat_message("user")
message.write("Como o projeto foi desenvolvido?")

message = st.chat_message("assistant")
message.write("\
        Esse projeto foi desenvolvido com as seguintes ferramentas:\n\n\
        **• Planner:** gerenciar e acompanhar todas atividades do projeto.\n\n\
        **• Linguagem Python:** desenvolver o código fonte do projeto.\n\n \
        **• Streamlit:** biblioteca utilizada para desenvolver a interface.\n\n  \
        **• Git:** versionar o código fonte.\n\n\
        **• Github:** hospedar o código fonte.\n\n\
              ")

st.write('#### Quer saber mais? Baixe nossa documentação completa do projeto 🚀', unsafe_allow_html=True)

with open("./images/relato_tecnico_motor_de_busca.pdf", "rb") as file:
    btn = st.download_button(
            label="Download da documentação",
            data=file,
            file_name="relato_tecnico_motor_de_busca.pdf",
            mime="document/pdf"
        )
# teste mac