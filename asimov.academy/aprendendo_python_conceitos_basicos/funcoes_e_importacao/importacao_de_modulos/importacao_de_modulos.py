import modulo_para_importacao;
retorno = modulo_para_importacao.minha_funcao();
print(retorno);
print(modulo_para_importacao.x);

# retorna funções especificas de um modulo
from modulo_para_importacao import minha_funcao, x;
retorno_especifico = minha_funcao();
print(retorno_especifico);
print(x);

# retorna todas as funções de um modulo
from modulo_para_importacao import *;
retorno_especifico = minha_funcao();
print(retorno_especifico);
print(x);

# apelidando modulo
import modulo_para_importacao as modulo;
retorno_modulo = modulo.minha_funcao();
print(retorno_modulo);
print(modulo.x);

# retorna funções especificas de um modulo com apelidos
from modulo_para_importacao import minha_funcao as mf, x as X;
retorno_especifico_apelidado = mf();
print(retorno_especifico_apelidado);
print(X);