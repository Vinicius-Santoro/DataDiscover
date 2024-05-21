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

# Informações do primeiro humano
profile_image_file_path1 = r"images/vinicius.jpg"
img1 = get_image_as_base64(profile_image_file_path1)
current_role1 = "Vinicius Naziozeno Santoro do Rio"

# Informações do segundo humano
profile_image_file_path2 = r"images/henrique.jpg"
img2 = get_image_as_base64(profile_image_file_path2)
current_role2 = "Henrique Oliveira Neves"

st.write("""
<div style="display: flex; justify-content: center;">
    <div style="flex-grow: 1; margin-right: 20px; text-align: center; width: 50%;">
        <img src="{}" alt="Your Name" width="200" height="200" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
        <h4><i>{}</i></h4>
        <p style="text-align: left; word-wrap: break-word;">
            Analista de dados no Itaú Unibanco, onde utiliza Python Pandas, AWS Athena, AWS QuickSight e Tableau para análises e visualizações de dados.
            Atualmente, cursa o quarto semestre de Ciência de Dados na FATEC. Vinicius tem o objetivo de ingressar em um programa de mestrado em
            Matemática Computacional ou Ciência da Computação, buscando aprofundar suas habilidades e contribuir para o avanço da área de dados.
        </p>
    </div>
    <div style="flex-grow: 1; margin-left: 20px; text-align: center; width: 50%;">
        <img src="{}" alt="Your Name" width="200" height="200" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
        <h4><i>{}</i></h4>
        <p style="text-align: left; word-wrap: break-word;">
            Engenheiro de dados no Itaú Unibanco, com proficiência em AWS Glue, Step Functions, Athena, PySpark e Terraform.
            Enquanto avança em sua carreira, ele também está no quarto semestre do curso de Ciência de Dados na FATEC.
            Busca ingressar em um mestrado em Estatística, visando aprofundar em métodos descritivos e indutivos para contribuir
            com a área de dados.
        </p>
    </div>
</div>
""".format(img1, current_role1, img2, current_role2), unsafe_allow_html=True)
