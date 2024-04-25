import streamlit as st
import pandas as pd
# import lazypredict
from lazypredict.Supervised import LazyClassifier
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io

st.set_page_config(
    page_title="Relatório de Performance de Modelo",
    page_icon="📃",
    layout="wide"
)

st.title("Relatório de Performance de Modelo")

# Model building
def build_model(df):
    df = df.loc[:100] # FOR TESTING PURPOSE, COMMENT THIS OUT FOR PRODUCTION
    X = df.iloc[:,:-1] # Using all column except for the last column as X
    Y = df.iloc[:,-1] # Selecting the last column as Y

    st.markdown('**1.2. Dimensão do DataFrame**')
    st.write('X')
    st.info(X.shape)
    st.write('Y')
    st.info(Y.shape)

    st.markdown('**1.3. Detalhes das Variáveis**:')
    st.write('Variável X (mostrando as 20 primeiras)')
    st.info(list(X.columns[:20]))
    st.write('Variável Y')
    st.info(Y.name)

    # Build lazy model
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size = split_size,random_state = seed_number)
    reg = LazyRegressor(verbose=0,ignore_warnings=False, custom_metric=None)
    models_train,predictions_train = reg.fit(X_train, X_train, Y_train, Y_train)
    models_test,predictions_test = reg.fit(X_train, X_test, Y_train, Y_test)

    st.subheader('2. Tabela de Performance do Modelo')

    st.write('Conjunto de Treinamento')
    st.write(predictions_train)
    st.markdown(filedownload(predictions_train,'training.csv'), unsafe_allow_html=True)

    st.write('Conjunto de Teste')
    st.write(predictions_test)
    st.markdown(filedownload(predictions_test,'test.csv'), unsafe_allow_html=True)

    st.subheader('3. Plotando Tabela de Performance do Modelo (Conjunto de Teste)')


    with st.markdown('**R-squared**'):
        # Tall
        predictions_test["R-Squared"] = [0 if i < 0 else i for i in predictions_test["R-Squared"] ]
        plt.figure(figsize=(3, 9))
        sns.set_theme(style="whitegrid")
        ax1 = sns.barplot(y=predictions_test.index, x="R-Squared", data=predictions_test)
        ax1.set(xlim=(0, 1))
    st.markdown(imagedownload(plt,'plot-r2-tall.pdf'), unsafe_allow_html=True)
        # Wide
    plt.figure(figsize=(9, 3))
    sns.set_theme(style="whitegrid")
    ax1 = sns.barplot(x=predictions_test.index, y="R-Squared", data=predictions_test)
    ax1.set(ylim=(0, 1))
    plt.xticks(rotation=90)
    st.pyplot(plt)
    st.markdown(imagedownload(plt,'plot-r2-wide.pdf'), unsafe_allow_html=True)

    with st.markdown('**RMSE (capped at 50)**'):
        # Tall
        predictions_test["RMSE"] = [50 if i > 50 else i for i in predictions_test["RMSE"] ]
        plt.figure(figsize=(3, 9))
        sns.set_theme(style="whitegrid")
        ax2 = sns.barplot(y=predictions_test.index, x="RMSE", data=predictions_test)
    st.markdown(imagedownload(plt,'plot-rmse-tall.pdf'), unsafe_allow_html=True)
        # Wide
    plt.figure(figsize=(9, 3))
    sns.set_theme(style="whitegrid")
    ax2 = sns.barplot(x=predictions_test.index, y="RMSE", data=predictions_test)
    plt.xticks(rotation=90)
    st.pyplot(plt)
    st.markdown(imagedownload(plt,'plot-rmse-wide.pdf'), unsafe_allow_html=True)

    with st.markdown('**Tempo de Execução do Cálculo**'):
        # Tall
        predictions_test["Time Taken"] = [0 if i < 0 else i for i in predictions_test["Time Taken"] ]
        plt.figure(figsize=(3, 9))
        sns.set_theme(style="whitegrid")
        ax3 = sns.barplot(y=predictions_test.index, x="Time Taken", data=predictions_test)
    st.markdown(imagedownload(plt,'plot-calculation-time-tall.pdf'), unsafe_allow_html=True)
        # Wide
    plt.figure(figsize=(9, 3))
    sns.set_theme(style="whitegrid")
    ax3 = sns.barplot(x=predictions_test.index, y="Time Taken", data=predictions_test)
    plt.xticks(rotation=90)
    st.pyplot(plt)
    st.markdown(imagedownload(plt,'plot-calculation-time-wide.pdf'), unsafe_allow_html=True)

# Download CSV data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df, filename):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download={filename}>Download {filename} File</a>'
    return href

def imagedownload(plt, filename):
    s = io.BytesIO()
    plt.savefig(s, format='pdf', bbox_inches='tight')
    plt.close()
    b64 = base64.b64encode(s.getvalue()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename} File</a>'
    return href

#---------------------------------#
st.write("""
Nesta implementação, a biblioteca lazypredict é usada para construir vários modelos de aprendizado de máquina de uma só vez.

""")

# Developed by: [Data Professor](http://youtube.com/dataprofessor)

#---------------------------------#
# Sidebar - Collects user input features into dataframe
st.header('1. Coletando Dados')
uploaded_file = st.file_uploader("Insira seu arquivo excel ou csv", type=["csv", "xlsx"])

# Sidebar - Specify parameter settings
st.header('2. Configurando Parâmetros')
# Função st.sidebar.slider para a variável split_size
# 10: valor mínimo
# 90: valor máximo
# 80: valor onde inicia quando a página é carregada
#  5: intervalo

# input
col1, col2 = st.columns([2,2])
with col1:
    split_size = st.slider('Proporção de divisão de dados (% para conjunto de treinamento)', 10, 90, 80, 5)
with col2:
    seed_number = st.slider('Defina o número inicial aleatório', 1, 100, 42, 1)



# Função st.sidebar.slider para a variável seed_number
#   1: valor mínimo
# 100: valor máximo
#  42: valor onde inicia quando a página é carregada
#   1: intervalo

#---------------------------------#
# Main panel

# Displays the dataset
st.subheader('1. DataFrame')

if uploaded_file is not None:
    # Analisa se o tipo de arquivo é csv ou excel para atribuir para uma variável
    def load_csv(uploaded_file):
        if '.csv' in uploaded_file.name:
            data = pd.read_csv(uploaded_file, encoding="latin-1", sep=";", low_memory=False)
        elif '.xlsx' in uploaded_file.name:
            data = pd.read_excel(uploaded_file)

        # Mensagem de sucesso de carregou com sucesso
        st.success("Arquivo carregado com sucesso.")
        return data
        
    # Atribui o arquivo para a variável df
    df = load_csv(uploaded_file)

    st.markdown('**1.1. Analise o DataFrame**')
    st.write(df)
    build_model(df)
else:
    st.info('Esperando um arquivo excel ou csv ser inserido.')
    if st.button('Clique para utilizar um exemplo'):
        # Diabetes dataset
        diabetes = load_diabetes()
        X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
        Y = pd.Series(diabetes.target, name='response')
        df = pd.concat( [X,Y], axis=1 )

        st.markdown('O Dataset "diabetes" do sklearn foi utilizado como exemplo')
        st.write(df.head(5))

        build_model(df)
