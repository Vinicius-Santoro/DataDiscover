import streamlit as st

st.set_page_config(
    page_title="Fale Conosco",
    page_icon="📞",
    layout="wide"
)

def main():
    st.title("Fale Conosco")

    st.header("Vinicius")
    st.markdown("Desenvolvedor")
    st.markdown("[GitHub](https://github.com/seu_perfil_vinicius)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/seu_perfil_vinicius)")

    st.header("Henrique")
    st.markdown("Desenvolvedor")
    st.markdown("[GitHub](https://github.com/seu_perfil_henrique)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/seu_perfil_henrique)")

if __name__ == "__main__":
    main()
