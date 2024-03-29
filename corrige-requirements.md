### _Erros encontrados e como foram solucionados_

#### Erro 1

> [!CAUTION]
> AttributeError: module 'numba' has no attribute 'generated_jit'.

#### Solução

> [!TIP]
> 1. Acessar o arquivo env\Lib\site-packages\visions\backends\shared\nan_handling.py"
> 2. Comentar a linha 34 que contém: `@nb.generated_jit(nopython=True)`

#### Erro 2

> [!CAUTION]
> TypeError: OneHotEncoder.__init__() got an unexpected keyword argument 'sparse''.

#### Solução

> [!TIP]
> 1. Acessar o arquivo env\Lib\\site-packages\streamlit\runtime\scriptrunner\script_runner.py"
> 2. Remover o segundo parâmetro da função OneHotEncoder:
> 3. Como estava: `OneHotEncoder(handle_unknown="ignore", sparse=False))`
> 4. Como ficou: `OneHotEncoder(handle_unknown="ignore")`