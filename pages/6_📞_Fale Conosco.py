import streamlit as st
import base64

st.set_page_config(
    page_title="Fale Conosco",
    page_icon="📞",
    layout="wide"
)

# def main():
#     st.title("Fale Conosco")

#     st.header("Vinicius")
#     st.markdown("Desenvolvedor")
#     st.markdown("[GitHub](https://github.com/seu_perfil_vinicius)")
#     st.markdown("[LinkedIn](https://www.linkedin.com/in/seu_perfil_vinicius)")

#     st.header("Henrique")
#     st.markdown("Desenvolvedor")
#     st.markdown("[GitHub](https://github.com/seu_perfil_henrique)")
#     st.markdown("[LinkedIn](https://www.linkedin.com/in/seu_perfil_henrique)")

# if __name__ == "__main__":
#     main()


import streamlit as st
import base64

# Função para ler a imagem e codificá-la em base64
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()
    return img

# Informações do primeiro humano
profile_image_file_path1 = r"images/vinicius.jpg"
img1 = get_image_as_base64(profile_image_file_path1)
current_role1 = "Vinicius Rio, Analista de Dados no Itaú Unibanco"

# Informações do segundo humano
profile_image_file_path2 = r"images/henrique.jpg"
img2 = get_image_as_base64(profile_image_file_path2)
current_role2 = "Henrique Neves, Engenheiro de Dados no Itaú Unibanco"

# Exibindo as informações
st.write("""
<div style="display: flex; justify-content: center;">
    <div style="flex-grow: 1; margin-right: 20px; text-align: center;">
        <img src="{}" alt="Your Name" width="200" height="200" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
        <h4><i>{}</i></h4>
        <p style="text-align: left;">• 🧑‍💻 Analista de Dados, trabalhando com Python, Athena, QuickSight, Tableu e Alteryx.</p>
        <p style="text-align: left;">• 📝 Cursando o quarto semestre de ciência de dados na FATEC.</p>
        <p style="text-align: left;">• 🎯 Responsável por garantir uma experiência excelente dos clientes no assistente virtual no app Itaú.<p>
        <p style="text-align: left;">• 💻 You can check my projects on Medium: Guilherme Datt</p>
        <p style="text-align: left;">• 📧 How to reach me: guilhermedatt@gmail.com</p>
        <p style="text-align: left;">• 🏠 São Paulo - Brasil</p>
    </div>
    <div style="flex-grow: 1; margin-left: 20px; text-align: center;">
        <img src="{}" alt="Your Name" width="200" height="200" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
        <h4><i>{}</i></h4>
        <p style="text-align: left;">• 🧑‍💻 Analista de Dados, trabalhando com Python, Athena, QuickSight, Tableu e Alteryx.</p>
        <p style="text-align: left;">• 📝 Cursando o quarto semestre de ciência de dados na FATEC.</p>
        <p style="text-align: left;">• 🎯 Responsável por garantir uma experiência excelente dos clientes no assistente virtual no app Itaú.<p>
        <p style="text-align: left;">• 💻 You can check my projects on Medium: Guilherme Datt</p>
        <p style="text-align: left;">• 📧 How to reach me: guilhermedatt@gmail.com</p>
        <p style="text-align: left;">• 🏠 São Paulo - Brasil</p>
    </div>
</div>
""".format(img1, current_role1, img2, current_role2), unsafe_allow_html=True)