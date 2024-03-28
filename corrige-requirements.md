### _Erros encontrados e como foram solucionados_

> [!CAUTION]
> AttributeError: module 'numba' has no attribute 'generated_jit'.

> [!TIP]
> 1. Acessar o arquivo env\Lib\site-packages\visions\backends\shared\nan_handling.py"
> 2. Comentar a linha 34 que contém: `@nb.generated_jit(nopython=True)`

[!CAUTION]
AttributeError: module 'numba' has no attribute 'generated_jit'.

[!TIP]
1. Acessar o arquivo env\Lib\site-packages\visions\backends\shared\nan_handling.py"

2. Comentar a linha 34 que contém: `@nb.generated_jit(nopython=True)`