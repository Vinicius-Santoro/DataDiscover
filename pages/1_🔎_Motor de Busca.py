import re
import time
import urllib
import requests
import pandas as pd
from time import sleep
import streamlit as st
import plotly.express as px
from bs4 import BeautifulSoup

st.set_page_config(
    page_title="Motor de Busca",
    page_icon="🔎",
    layout="wide",
)

# this function for the getting inforamtion of the web page
def get_paperinfo(paper_url, headers):

  #download the page
  response=requests.get(paper_url,headers=headers)

  # check successful response
  if response.status_code != 200:
    print('Status code:', response.status_code)
    raise Exception('Failed to fetch web page ')

  #parse using beautiful soup
  paper_doc = BeautifulSoup(response.text,'html.parser')
  for div in paper_doc.find_all("div", {'class':'gs_ggs gs_fl'}): 
    div.decompose()

  return paper_doc

# this function for the extracting information of the tags
def get_tags(doc):
  paper_tag = doc.select('[data-lid]')
  # cite_tag = doc.select('[title=Cite] + a')
  cite_tag = doc.find_all('div', {"class": "gs_fl"})
  link_tag = doc.find_all('h3',{"class" : "gs_rt"})
  author_tag = doc.find_all("div", {"class": "gs_a"})

  return paper_tag,cite_tag,link_tag,author_tag

# it will return the title of the paper
def get_papertitle(paper_tag):
  
  paper_names = []
  
  for tag in paper_tag:
    paper_names.append(tag.select('h3')[0].get_text())

  return paper_names

# it will return the number of citation of the paper
def get_citecount(cite_tag):
  cite_count = []
  for i in cite_tag:
    cite = i.text
    tmp = re.findall('Cited by[ ]\d+', cite)
    if tmp:
      cite_count.append(tmp[0])
    else:
      cite_count.append(0)

  return cite_count

# function for the getting link information
def get_link(link_tag):

  links = []

  for i in range(len(link_tag)) :
    if link_tag[i].a:  
      links.append(link_tag[i].a['href']) 
    else:
      links.append(None)

  return links 

# function for the getting autho , year and publication information
def get_author_year_publi_info(authors_tag):
  years = []
  publication = []
  authors = []
  for i in range(len(authors_tag)):
      authortag_text = (authors_tag[i].text).split()
      # year = int(re.search(r'\d+', authors_tag[i].text).group())
      # years.append(year)
      
      input_text_year = " ".join(authors_tag[i].text.split()[-3:])
      datesearch = re.findall("(19\d{2}|20\d{2})", input_text_year)
      if len(datesearch) > 0:
        year = int(datesearch[len(datesearch)-1])
        years.append(year)
      else:
        year = 0
        years.append(year)
      publication.append(authortag_text[-1])
      author = authortag_text[0] + ' ' + re.sub(',','', authortag_text[1])
      authors.append(author)
  
  return years, publication, authors

def cite_number(text):
  if text != 0:
    result = text.split()[-1]
  else:
    result = str(text)
  return result

@st.cache_data
def convert_df(df):
  # IMPORTANT: Cache the conversion to prevent computation on every rerun
  return df.to_csv().encode('utf-8')

html_temp = """
                    <div style="background-color:{};padding:1px">
                    
                    </div>
                    """

# with st.sidebar:
#     st.markdown("""
#     # Sobre
#     Uma ferramenta para extrair informações relevantes de artigos de pesquisa do Google Scholar com base nas informações do usuário.
#     """)
    
#     st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
#     st.markdown("""
#     # Como funciona?
#     Insira suas palavras-chave no campo de texto e selecione quantas páginas serão utilizadas dos resultados do Google Acadêmico.  
#     """)

hide="""
<style>
footer{
	visibility: hidden;
    	position: relative;
}
.viewerBadge_container__1QSob{
    visibility: hidden;
}

<style>
"""
st.markdown(hide, unsafe_allow_html=True)

# # title
# st.markdown("""
# ## Motor de Busca
# Extração de informações relevantes de artigos de pesquisa do Google Scholar.
# """)

# Texto de boas vindas.
st.write('# Motor de Busca <span style="color: #ff6200"></span>', unsafe_allow_html=True)

# Texto de descrição do projeto.
st.markdown("<p style='text-align: justify;'>\
            O motor de busca possibilita você ter o retorno dos principais artigos publicados no Google Schoolar. \
            Além disso, é apresentado dois indicadores para você ter uma visão analítica de como estão as distribuições.\
</p>", unsafe_allow_html=True)


# scraping function
# creating final repository
paper_repos_dict = {
                    'Título do Artigo' : [],
                    'Ano' : [],
                    'Autor' : [],
                    'Citações' : [],
                    'Site de Publicação' : [],
                    'Link do Artigo' : [] }

# adding information in repository
def add_in_paper_repo(papername,year,author,cite,publi,link):
  paper_repos_dict['Título do Artigo'].extend(papername)
  paper_repos_dict['Ano'].extend(year)
  paper_repos_dict['Autor'].extend(author)
  paper_repos_dict['Citações'].extend(cite)
  paper_repos_dict['Site de Publicação'].extend(publi)
  paper_repos_dict['Link do Artigo'].extend(link)
#   for i in paper_repos_dict.keys():
#     print(i,": ", len(paper_repos_dict[i]))
#     print(paper_repos_dict[i])
  df = pd.DataFrame(paper_repos_dict)
  
  return df

# headers
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
url_begin = 'https://scholar.google.com/scholar?start={}&q='
# url_begin = 'https://www.bing.com/search?q={}'
url_end = '&hl=en&as_sdt=0,5='

# input
col1, col2 = st.columns([3,1])
with col1:
  text_input = st.text_input("Pesquisar no Google Scholar", placeholder="O que você está procurando?", disabled=False)
with col2:
  total_to_scrap = st.slider("Quantas páginas para realizar o scrap?", min_value=1, max_value=4, step=1, value=1)

st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
# create scholar url
if text_input:
    text_formated = "+".join(text_input.split())
    input_url = url_begin+text_formated+url_end
    if input_url:
        response=requests.get(input_url,headers=headers)
        # st.info(input_url)
        total_papers = 10 * total_to_scrap
        for i in range (0,total_papers,10):
            # get url for the each page
            url = input_url.format(i)
            # function for the get content of each page
            doc = get_paperinfo(url, headers)

            # function for the collecting tags
            paper_tag,cite_tag,link_tag,author_tag = get_tags(doc)

            # Título do Artigo from each page
            papername = get_papertitle(paper_tag)

            # year , author , publication of the paper
            year , publication , author = get_author_year_publi_info(author_tag)

            # cite count of the paper 
            cite = get_citecount(cite_tag)

            # url of the paper
            link = get_link(link_tag)

            # add in paper repo dict
            final = add_in_paper_repo(papername,year,author,cite,publication,link)

            # use sleep to avoid status code 429
            sleep(20)
		
        final['Ano'] = final['Ano'].astype('int')
        final['Citações'] = final['Citações'].apply(cite_number).astype('int')

        with st.expander("Artigos Encontrados"):
          st.dataframe(final)
          csv = convert_df(final)
          file_name_value = "_".join(text_input.split())+'.csv'
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name=file_name_value,
            mime='text/csv',
        )

        # Plots
        col1, col2 = st.columns([2,1])

        with col1:
          with st.expander("Distribution of papers by year and citation", expanded=True):
            size_button = st.checkbox('Set Citation as bubble size', value=True)
            size_value = None
            if size_button:
              size_value = 'Citações'
            final_sorted = final.sort_values(by='Ano', ascending=True)
            fig1 = px.scatter(
                  final_sorted, 
                  x="Ano", 
                  color="Site de Publicação",
                  size=size_value, 
                  log_x=True, 
                  size_max=60
                  )
            fig1.update_xaxes(type='category')
            st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

        with col2:
          percentage_sites = {}
          sites = list(final_sorted['Site de Publicação'])
          for i in sites:
            percentage_sites[i] = sites.count(i)/len(sites)*100
          df_per = pd.DataFrame(list(zip(percentage_sites.keys(), percentage_sites.values())), columns=['sites', 'percentage'])
    
          fig2 = px.pie(
                df_per, 
                values="percentage", 
                names="sites", 
                )
          with st.expander("Percentage of publication sites", expanded=True):
            st.plotly_chart(fig2, theme="streamlit", use_container_width=True)