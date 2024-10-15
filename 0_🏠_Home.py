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
st.write('# Bem vindo ao <span style="color: #ff6200">DataDiscover</span>',
         unsafe_allow_html=True)

# Texto de descrição do projeto.
st.markdown("<p style='text-align: justify;'>\
            O DataDiscover é um site que centraliza seis ferramentas\
            projetadas especificamente para estudantes e entusiastas de\
            ciência de dados. Nosso objetivo é simplificar e aprimorar a\
            experiência de aprendizado e prática nessa área.\
</p>", unsafe_allow_html=True)

# Texto de recursos principais.
st.write('#### Recursos principais', unsafe_allow_html=True)
st.markdown("<p style='text-align: justify;'>\
        Clique em cada uma das ferramentas para saber mais.\
</p>", unsafe_allow_html=True)

# Texto de explicação do motor de busca, com expander.
with st.expander("🔎 Motor de Busca"):
    st.markdown("<p style='text-align: justify;'>\
        O motor de busca permite que você pesquise artigos acadêmicos\
        no Google Scholar, oferecendo também uma visão analítica dos\
        principais autores e sites relevantes. É ideal para quem precisa\
        explorar rapidamente as principais publicações em um campo específico\
    </p>", unsafe_allow_html=True)
    
# Texto de explicação de extração de dados, com expander.
with st.expander("🎲 Extração de Dados"):
    st.markdown("<p style='text-align: justify;'>\
        Nesta tela, você pode pesquisar e baixar conjuntos de dados\
        diretamente do Kaggle em formatos CSV e XLSX. A interface facilita\
        o acesso rápido a uma variedade de dados para análise ou treinamento\
        de modelos.\
    </p>", unsafe_allow_html=True)

# Texto de explicação da análise exploratória de dados, com expander.
with st.expander("📊 Análise Exploratória de Dados"):
    st.markdown("<p style='text-align: justify;'>\
        Esta tela oferece uma análise geral e estatística\
        detalhada dos dados em um conjunto selecionado, permitindo ao usuário\
        entender melhor as características e tendências antes de qualquer\
        modelagem.\
    </p>", unsafe_allow_html=True)

# Texto de explicação do relatório de performance do modelo, com expander.
with st.expander("📃 Relatório de Performance de Modelo"):
    st.markdown("<p style='text-align: justify;'>\
        Aqui, você pode comparar diferentes modelos de\
        aprendizado de máquina para determinar qual terá o\
        melhor desempenho com o seu conjunto de dados,\
        facilitando a escolha do modelo mais eficaz.\
    </p>", unsafe_allow_html=True)

# Texto de explicação tela de análise de sentimento, com expander.
with st.expander("😄 Análise de Sentimento"):
    st.markdown("<p style='text-align: justify;'>\
        Nesta tela, você pode carregar uma base\
        de dados e selecionar uma coluna para realizar\
        a classificação de sentimentos (positivo, negativo ou neutro),\
        obtendo insights sobre a opinião expressa nos textos.\
    </p>", unsafe_allow_html=True)

# Texto de explicação da tela de banco de dados com expander.
with st.expander("📦 Gerencimento do Banco de Dados"):
    st.markdown("<p style='text-align: justify;'>\
        Esta tela permite visualizar e gerencie todas\
        as bases de dados armazenadas em um banco de dados não\
        relacional, incluindo a opção de excluir conjuntos de\
        dados desnecessários.\
    </p>", unsafe_allow_html=True)

st.write('#### Possíveis perguntas', unsafe_allow_html=True)

message = st.chat_message("user")
message.write("Por que esse projeto foi desenvolvido?")

message = st.chat_message("assistant")
message.write("\
    Esse projeto criado para centralizar e facilitar o acesso\
    a ferramentas essenciais para estudantes e entusiastas de\
    ciência de dados, oferecendo uma plataforma única onde eles\
    podem aprender, praticar e aprimorar suas habilidades de\
    forma simplificada e eficiente.\
")

message = st.chat_message("user")
message.write("Como esse projeto pode ajudar um estudante de dados? ")

message = st.chat_message("assistant")
message.write("\
    O DataDiscover ajuda estudantes de dados ao fornecer\
    ferramentas integradas que cobrem desde a busca e\
    análise de artigos acadêmicos até a extração de dados, \
    nálise exploratória, avaliação de modelos de aprendizado\
    de máquina, e análise de sentimentos. Isso permite que\
    os estudantes ganhem experiência prática e consolidem\
    seus conhecimentos em um ambiente centralizado.\
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
