#Lista de Exercícios - While

"""
PROBLEMA 1: Dado um número, exibir os seus 10 primeiros múltiplos
Entrada: 2      Saída: 2 4 6 8 10 12 14 16 18 20
"""

numero = int(input("Digite um número: "))
multiplicando = 0

while multiplicando != 10:
    multiplicando += 1
    resultado = numero * multiplicando
    print(f"{resultado}")


"""
V2: Exibir em formato de tabuada
"""

numero = int(input("Digite um número: "))
multiplicando = 0

while multiplicando != 10:
    multiplicando += 1
    resultado = numero * multiplicando
    print(f"{numero} x {multiplicando} = {resultado}")


"""
V3: Pedir o multiplicador e exibir no formato de tabuada
"""

numero = int(input("Digite um número: "))
limite = int(input("Digite o multiplicando: "))
multiplicando = 0

while multiplicando != limite:
    multiplicando += 1
    resultado = numero * multiplicando
    print(f"{numero} x {multiplicando} = {resultado}")


"""
PROBLEMA 2: Somar números até que seja digitado zero.
Entrada: 4 6 9 3 0      Saída: 22
"""

numero = int(input("V1 - Digite um número: "))
soma = numero

while numero > 0:
    outro_numero = int(input("Digite outro número: "))
    soma = numero + outro_numero
    while outro_numero > 0:
        outro_numero = int(input("Digite outro número: "))
        soma += outro_numero
    else:
        numero = 0

print(soma)

"""
V2: Somar números até que seja digitado um número negativo.
"""

numero = int(input("V2 - Digite um número: "))
soma = numero

while numero >= 0:
    outro_numero = int(input("Digite outro número: "))
    soma = numero + outro_numero
    while outro_numero >= 0:
        outro_numero = int(input("Digite outro número: "))
        soma += outro_numero
    else:
        numero = -1

print(soma)


"""
V3: Somar números até que seja digitado um número negativo. O número negativo não fará parte da somatória.
"""

numero = int(input("V3 - Digite um número: "))
soma = numero

while numero >= 0:
    outro_numero = int(input("Digite outro número: "))
    if outro_numero >= 0:
        soma = numero + outro_numero
        while outro_numero >= 0:
            outro_numero = int(input("Digite outro número: "))
            if outro_numero >= 0:
                soma += outro_numero
        else:
            numero = -1
    else:
        numero = -1

if soma >= 0:
    print(soma)


"""
PROBLEMA 3: Em uma votação, existem 3 candidatos: 1 – Huguinho, 2 – Zezinho e 3 – Luizinho.
Pedir e acumular votos até que em votos seja digitado o numero 0 (zero).
Ao final, exibir a quantidade de votos de cada usuário.

1 – HUGUINHO
2 – ZEZINHO
3 – LUIZINHO 
0 - SAIR

ENTRADA: 
3 3 2 3 1 3 1 0
SAÍDA: 
1 – HUGUINHO: 2 VOTOS
2 – ZEZINHO: 1 VOTO
3 – LUIZINHO: 4 VOTOS

* versão todos em um
"""

voto = 1
continuar = "S"
huguinho = zezinho = luizinho = 0   #recurso foda

while voto != "0" and continuar == "S":
    voto = input("Digite os votos para, Huguinho[1], Zezinho[2], Luizinho[3]: ")
    continuar = input("Deseja continuar a inserir votos? [s]im ou [n]ão? ").upper()
    while continuar != "S" and continuar != "N":
        continuar = input("Erro! Continuar? [s]im ou [n]ão? ").upper()
    if voto == "1":
        huguinho += 1
    elif voto == "2":
        zezinho += 1
    elif voto == "3":
        luizinho += 1
    else:
        print("Número de escolha inválido")
        break
#podia ter usado match case
print(f"""
1 - Huguinho: {huguinho} voto(s)
2 - Zezinho: {zezinho} voto(s)
3 - Luizinho: {luizinho} voto(s)
""")
