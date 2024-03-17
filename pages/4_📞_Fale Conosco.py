import streamlit as st

st.set_page_config(
    page_title="Fale Conosco",
    page_icon="📞",
)

st.title("Fale Conosco")

with st.expander("Explicação das métricas"):
    st.markdown("#### SMAPE:")
    st.latex(r'''\frac{100\%}{n} \sum_{i=1}^{n} \frac{|Atual_i-Forecast_i|}{|Atual_i|+|Forecast_i|}''')
    st.markdown("""
                - Como é calculado: O SMAPE normaliza os erros relativos dividindo pelos valores reais e previstos. Isso força a métrica a variar entre 0% e 100%. 
                - Como interpretar: A grosso modo a interpretação se da a quantos % o modelo ficou distante do valor real. 
                """)
    st.markdown("#### RMSE:")
    st.latex(r'''\sqrt {\frac{1}{n} \sum_{i=1}^{n}(Forecast_i-Atual_i)^2}''')
    st.markdown("""
                - Como é calculado: O RMSE é calculado tomando-se a raiz quadrada da média dos quadrados dos erros, onde o erro bruto é a diferença entre o valor previsto pelo modelo e o valor real.
                - Como interpretar: Pode ser interpretado como o desvio médio que as previsões têm do alvo.
                """)