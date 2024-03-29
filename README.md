## Projeto Integrador III

### `Objetivo`
Repositório para versionar o desenvolvimento do motor de busca, sistema de software projetado para encontrar informações armazenadas em um sistema computacional a partir de palavras-chave indicadas pelo utilizador, reduzindo o tempo necessário para encontrar informações.

### `Proposta de Projeto`
O DataDiscover é um site que centraliza três ferramentas projetadas especificamente para estudantes e entusiastas de ciência de dados. Nosso objetivo é simplificar e aprimorar a experiência de aprendizado e prática nessa área.

### `Estrutura do Projeto`

<details>
  <summary><b>Motor de Busca</b></summary>
    O motor de busca possibilita você ter o retorno dos principais artigos publicados no Google Schoolar.
    Além disso, é apresentado dois indicadores para você ter uma visão analítica de como estão as distribuições.
  
  - Após o usuário realizar a consulta, aparecerá os seguintes itens:
    - Lista dos artigos relacionados a consulta, com opção de exportar para csv.
    - Indicador da distribuição de artigos publicados por ano e citação.
    - Indicador da % de sites que publicaram.
</details>

<details>
<summary><b>Análise Exploratória de Dados</b></summary>
      A ferramenta de análise exploratória de dados é uma aliada valiosa para analistas e cientista de dados.
      Com ela, você pode importar um arquivo Excel ou CSV contendo seus dados brutos e obter uma análise detalhada do seu dataframe.
      Ela revela padrões, tendências e insights ocultos, permitindo que você compreenda melhor a estrutura dos seus dados.
      A partir dessa análise, você pode tomar decisões informadas sobre limpeza, transformação e visualização dos dados.

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
</details>

<details>
<summary><b>Relatório de Performance de Modelo</b></summary>
      Imagine que você está construindo modelos de machine learning para resolver um problema específico.
      O relatório de performance de modelo entra em cena exatamente nesse momento.
      Basta inserir um arquivo Excel ou CSV e você descobrirá como seu dataframe se comportaria em 20 diferentes modelos de machine learning.
      Essa análise inclui métricas de acurácia, precisão, recall e F1-score, permitindo que você escolha o modelo mais adequado para o seu cenário.

  - Análise do dataset
  - Dimensão do dataset.
  - Detalhe das variáveis.
  - Modelo de performance.
    - Plotagem do modelo de performance.
      - R-Squared.
      - RMSE.
      - Tempo de cálculo.
</details>

### `Como Baixar o Projeto`
- Clone o repositório.
```bash
git clone git@github.com:Vinicius-Santoro/DataDiscover.git
```

- Instale as bibliotecas necessárias.
```bash
pip install -r requirements.txt
```

- Execute a aplicação
```bash
python -m streamlit run 0_🏠_Home.py
```
> [!TIP]
> Abra seu navegador para visualizar a aplicação funcionando.
