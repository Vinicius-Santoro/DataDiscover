## 📅 **Projeto Integrador IV** – DataDiscover, uma ferramenta para potencializar o aprendizado de estudantes de ciência de dados.

![Alt Text](./images/data_discover_home.png)

Bem-vindo ao **DataDiscover**! Essa aplicação foi projetada especificamente
para estudantes e entusiastas de ciência de dados. Nosso objetivo é simplificar
e aprimorar a experiência de aprendizado e prática nessa área.

## 🚀 **Features**

### **🔎 Motor de Busca**
O motor de busca permite que você pesquise artigos acadêmicos no Google Scholar, oferecendo também uma visão analítica dos principais autores e sites relevantes. É ideal para quem precisa explorar rapidamente as principais publicações em um campo específico.

### **🎲 Extração de Dados**
Nesta tela, você pode pesquisar e baixar conjuntos de dados diretamente do Kaggle em formatos CSV e XLSX. A interface facilita o acesso rápido a uma variedade de dados para análise ou treinamento de modelos.
  
### **📊 Análise Exploratória de Dados**
Esta tela oferece uma análise geral e estatística detalhada dos dados em um conjunto selecionado, permitindo ao usuário entender melhor as características e tendências antes de qualquer modelagem.

### **📃 Relatório de Performance de Modelo**
Aqui, você pode comparar diferentes modelos de aprendizado de máquina para determinar qual terá o melhor desempenho com o seu conjunto de dados, facilitando a escolha do modelo mais eficaz.
  
### **😄 Análise de Sentimento**
Nesta tela, você pode carregar uma base de dados e selecionar uma coluna para realizar a classificação de sentimentos (positivo, negativo ou neutro), obtendo insights sobre a opinião expressa nos textos.
  
### **📦 Gerencimento do Banco de Dados**
Esta tela permite visualizar e gerencie todas as bases de dados armazenadas em um banco de dados não relacional, incluindo a opção de excluir conjuntos de dados desnecessários.

## 🛠️ **Tech Stack**

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** MongoDB

## 📂 **Estrutura do Projeto**

```bash
├── /images            		# Imagens do projeto
├── /pages					# Telas da aplicação
│   ├── 1_🔎_Motor de Busca.py  
│   ├── 2_🎲_Extração de Dados.py
│   ├── 3_📊_Análise Exploratória de Dados.py
│   ├── 4_📃_Relatório de Performance de Modelo.py
│   ├── 5_😄_Análise de Sentimento.py
│   ├── 6_📦_Gerencimento do Banco de Dados.py
│   ├── 7_🖥️_Baixe o Código Fonte.py
│   ├── 8_📞_Fale Conosco.py
├── .gitignore				# Ignora os arquivos para o github
├── 0_🏠_Home.py			# Homepage da aplicação e chamada para as telas
├── corrige-requirements.md	# Documentação de correção de possíveis erros
├── requiremets.txt			# Dependências do projeto
└── README.md				# Documentação geral do projeto
```
