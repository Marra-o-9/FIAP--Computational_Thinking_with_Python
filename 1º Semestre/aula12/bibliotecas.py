#Pega linhas com a mesma finalidade e separa elas em blocos
#Quando for utilizar novamente esse subalgoritmo, é só chamar ele pelo nome escolhido

"""
import math

resposta = math.sqrt(16)
print(resposta)
"""

"""
from math import sqrt   #importa uma função específica da biblioteca

resposta = sqrt(16)     #e não há necessidade de escrever math. antes da função
print(resposta)
"""

from math import *      #importa todas as funções da biblioteca

resposta = sqrt(16)     #e não há necessidade de escrever o math em nenhuma delas também
print(resposta)