import streamlit as st
import base64

st.set_page_config(
    page_title="Fale Conosco",
    page_icon="📞",
    layout="wide"
)

# Função para ler a imagem e codificá-la em base64
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()
    return img

# Informações do segundo humano
profile_image_file_path1 = r"images/henrique.jpg"
img1 = get_image_as_base64(profile_image_file_path1)
current_role1 = "Henrique Oliveira Neves"

# Informações do primeiro humano
profile_image_file_path2 = r"images/vinicius.jpg"
img2 = get_image_as_base64(profile_image_file_path2)
current_role2 = "Vinicius Naziozeno Santoro do Rio"

# Informações do primeiro humano
profile_image_file_path3 = r"images/victor.jpg"
img3 = get_image_as_base64(profile_image_file_path3)
current_role3 = "Victor da Silva Araujo"

st.title("Fale Conosco")

st.write("""
<div style="display: flex; justify-content: center;">
    <div style="flex-grow: 1; margin-left: 20px; text-align: center; width: 50%;">
        <img src="{}" alt="Your Name" width="200" height="200" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
        <h4><i>{}</i></h4>
        <p style="text-align: left; word-wrap: break-word;">
            Engenheiro de dados no Itaú Unibanco, com proficiência em AWS Glue, Step Functions, Athena, PySpark e Terraform.
            Enquanto avança em sua carreira, ele também está no quinto semestre do curso de Ciência de Dados na FATEC.
            Busca ingressar em um mestrado em Estatística, visando aprofundar em métodos descritivos e indutivos para contribuir
            com a área de dados.
            <br>• Linkedin: <a href="https://www.linkedin.com/in/henrique-oliveira-neves-721b79203/">www.linkedin.com/in/henrique-oliveira-neves/</a>
        </p>
    </div>
    <div style="flex-grow: 1; margin-right: 20px; text-align: center; width: 50%;">
        <img src="{}" alt="Your Name" width="200" height="200" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
        <h4><i>{}</i></h4>
        <p style="text-align: left; word-wrap: break-word;">
            Analista de dados no Itaú Unibanco, onde utiliza Python Pandas, AWS Athena, AWS QuickSight e Tableau para análises e visualizações de dados.
            Atualmente, cursa o quarto semestre de Ciência de Dados na FATEC. Vinicius tem o objetivo de ingressar em um programa de mestrado em
            Matemática Computacional ou Ciência da Computação, buscando aprofundar suas habilidades e contribuir para o avanço da área de dados.
            <br>• Linkedin: <a href="https://www.linkedin.com/in/viniciusrio">www.linkedin.com/in/viniciusrio</a>
        </p>
    </div>
        <div style="flex-grow: 1; margin-left: 20px; text-align: center; width: 50%;">
        <img src="{}" alt="Your Name" width="200" height="200" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
        <h4><i>{}</i></h4>
        <p style="text-align: left; word-wrap: break-word;">
            Aspirante à Oficial de comunicações do Exército Brasileiro e futuro cientista de dados no Santander. Por conta de sua formação
            militar, disciplina e senso de responsabilidade foram extremamente explorados, no qual permitiu diversas experiências.
            Trabalha com a governça de validações dos modelos de risco de crédito do grupo Santander. 
            <br>• Linkedin: <a href="https://www.linkedin.com/in/henrique-oliveira-neves-721b79203/">https://www.linkedin.com/in/iam-victor/</a>
        </p>
    </div>
</div>
""".format(img1, current_role1, img2, current_role2, img3, current_role3), unsafe_allow_html=True)
