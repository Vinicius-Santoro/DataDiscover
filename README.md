## Projeto Integrador III

### `Objetivo`
Repositório para versionar o desenvolvimento do motor de busca, sistema de software projetado para encontrar informações armazenadas em um sistema computacional a partir de palavras-chave indicadas pelo utilizador, reduzindo o tempo necessário para encontrar informações.

### `Proposta de Projeto`
O projeto que os alunos Vinicius Naziozeno Santoro do Rio e Henrique Oliveira Neves querem desenvolver, é o Data Discover, motor de busca para estudantes de ciência de dados.

O motor de busca em si retornará artigos acadêmicos da base do Google Scholar.

Abaixo, apresentamos a estrutura do nosso projeto.

### `Estrutura do Projeto`

Itens Obrigatórios

- **Página Principal:** onde ficará a interface para o usuário realizar sua consulta.
  - Após o usuário realizar a consulta, aparecerá os seguintes itens:
    - Lista dos artigos relacionados a consulta, com opção de exportar para csv.
    - Indicador da distribuição de artigos publicados por ano e citação.
    - Indicador da % de sites que publicaram.
- **Página de Análise Exploratória de Dados (EDA):** onde o usuário terá a possibilidade de incluir um arquivo csv e retornaremos para ele:
  - Visualização geral do dataframe inserido.
  - Análises estatísticas:
    - Número de variáveis.
    - Número de registros.
    - Quantidade de células vazias.
    - % de células vazias.
    - Quantidade de linhas duplicadas.
    - % de linhas duplicadas.
    - Tamanho do arquivo.
    - Média do tamanho do arquivo alocado na memória.
  - Tipos de variáveis:
    - Descrição do tipo de variável de cada coluna.
  - Análise específica de cada variável, onde será apresentado:
    - Quantidade de registros distintos.
    - % de registros distintos.
    - Quantidade de registros nulos.
    - Média da variável.
    - Mínimo da variável.
    - Máximo da variável.
    - Quantidade de zeros na variável.
    - % de zeros na variável.
    - Tamanho alocado na memória.
  - Interações entre duas variáveis.
  - Correlações entre duas variáveis.
  - Análise de valores faltantes em cada variável.
  - Análise das primeiras linhas do dataframe.
  - Análise das últimas linhas do dataframe.
- **Página de Comparação de Algoritimos de Machine Learning:** onde o usuário terá a possibilidade de incluir um arquivo csv e retornaremos para ele:
  - Análise do dataset
    - Dimensão do dataset.
    - Detalhe das variáveis.
  - Modelo de performance.
    - Plotagem do modelo de performance.
      - R-Squared.
      - RMSE.
      - Tempo de cálculo.
