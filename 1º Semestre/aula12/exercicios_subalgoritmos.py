"""
PROBLEMA 1: Criar um procedimento que passe dois valores referentes a um intervalo e
exiba os números do intervalo.
    intervalo(3,9)
    >> 3 4 5 6 7 8 9
"""


def intervalo(x, y):
    for i in range(x, y + 1, 1):
        print(i, end=" ")


intervalo(3, 9)

"""
PROBLEMA 2: Criar um procedimento que passe dois valores referentes a um intervalo
e a forma "A" para aberto e "F" para fechado e exiba os números do intervalo.
    intervalo(3, 9, "A")
    >> 4 5 6 7 8
    intervalo(3, 9 ,"F")
    >> 3 4 5 6 7 8 9
"""


def intervalo2(x, y, z):
    if z == "A":
        for i in range(x + 1, y, 1):
            print(i, end=" ")
    elif z == "F":
        for i in range(x, y + 1, 1):
            print(i, end=" ")


print(f"\n")
intervalo2(3, 9, "A")
print(f"\n")
intervalo2(3, 9, "F")


"""
PROBLEMA 3: Criar uma função que pegue o número passado por parâmetro e retorne o próximo
número múltiplo de 5.
    print(prox_mult_5(7))
    >> 10
"""


def proximo_multiplo5(x):
    while x % 5 != 0:
        x += 1
    else:
        return x


print(f"\n")
print(proximo_multiplo5(11))


"""
PROBLEMA 4: Criar uma função que pegue um número e o múltiplo por parâmetro e retorne o próximo
número múltiplo.
    print(prox_mult(16, 7))
    >> 21
"""


def proximo_multiplo_var(x, y):
    while x % y != 0:
        x += 1
    else:
        return x


print(proximo_multiplo_var(16, 7))


"""
PROBLEMA 5: Fazer uma função que calcule o fatorial de um número passado por parâmetro
    print(fatorial(4))
    >> 24
"""


def fatorial(x):
    for fat in range(x - 1, 0 - 1, -1):
        if fat > 0:
            x *= fat
        else:
            return x


print(fatorial(4))


"""
PROBLEMA 6: Fazer uma função que retorne True caso um número seja primo e false se não for.
    if primo(17):
            print("Primo")
        else:
            print("Não é primo")
    >> Primo
"""


def numero_primo(x):
    if x == 1 or x == 2:
        return "Primo."
    for i in range(2, x, 1):
        if x % i == 0:
            return "Não é primo."
        elif x % i == 0:
            break
        else:
            return "Primo."


print(numero_primo(7))


"""
PROBLEMA 7: Fazer um procedimento que passe os numeros de um intervalo e mostre os primos 
deste intervalo.
    intervalo_primo(8, 20)
    >> 11 17 19
"""

'''
def numeros_primos(x, y):
    for i in range(x, y + 1, 1):
        if x % i == 0:
'''
