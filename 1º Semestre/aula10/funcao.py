#Função def

import math


#exibe dos números de 1 ao 10 na tela
#Definição dos sub-algoritmos
def exibe_1_10():
    inicio = 1
    fim = 10
    intervalo = 1
    for contador in range(inicio, fim + 1, intervalo):
        print(f"{contador} ", end="")


#Programa principal
print("Testando: ")
exibe_1_10()
exibe_1_10()
exibe_1_10()
exibe_1_10()
#chamar esse programa quantas vezes quiser
#ele já está pronto, é só pedir


def exibe_intervalo(i, f, incr) -> None:
    for contador in range(i, f + 1, incr):
        print(f"{contador} ", end="")


inicio = 1
fim = 10
intervalo = 1
print()
exibe_intervalo(inicio, fim, intervalo)     #mudar os parâmetros
exibe_intervalo(6, 17, 1)                   #exibir intervalos especificados a qualquer momento
exibe_intervalo(-56, 20, 23)                #usar o comando de forma dinâmica


#Função
#Calcular a raiz quadrada de um número
def raiz2(n: float) -> float:    #retorna dados flutuantes
    return n ** (1/2)


resp = raiz2(25)
print(f"\nRaiz quadrada: {resp}")

resp = math.sqrt(25)
print(f"\nRaiz quadrada: {resp}")


def maior3n(n1: int, n2: int, n3: int) -> int:
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return maior


maior = max(34, 56, 21)
print(maior)

maior = maior3n(34, 56, 21)
print(maior)
