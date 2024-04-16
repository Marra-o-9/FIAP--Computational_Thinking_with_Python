idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade!")


"""
COMPLEMENTO (o contrário de cada símbolo):
>=      <
>       <=
==      !=
!=      ==
<       >=
<=      >  
"""

"""
PROBLEMA 1: Dado um número pelo usuário, verificar se ele é positivo, exibindo a mensagem “O numero é
positivo” ou “O numero não é positivo”.

Entrada: 45 Saída: O numero é positivo
Entrada: -3 Saída: O numero não é positivo
Entrada: 0 Saída: O numero não é positivo
"""

num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo!")
elif num < 0:
    print("O número é negativo!")
else:
    print("O número é nulo!")


"""
PROBLEMA 2: Dada uma idade pelo usuário, verificar e exibir a mensagem “Você é menor de Idade” ou “Você é
maior de Idade”.

Entrada: 15 Saída: Você é menor de Idade
Entrada: 33 Saída: Você é maior de Idade
"""

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")


"""
PROBLEMA 3: Dado um número pelo usuário, verificar se ele é “O número é par” ou “O número é impar”,
exibindo sua respectiva mensagem.

Entrada: 3 Saída: O numero é impar
Entrada: 10 Saída: O numero é par
"""

num = float(input("Digite um número: "))

if num % 2 == 0:
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é ímpar!")


"""
PROBLEMA 4: Dados dois números pelo usuário, exibir o de maior valor.

Entrada: 5 45 Saída: 45
Entrada: 10 8 Saída: 10
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O número maior é {num1}.")
else:
    print(f"O número maior é {num2}")


"""
PROBLEMA 5: Dadas duas notas, calcular e exibir a média simples das mesmas. Caso a média seja inferior a 5
exibir “Você está reprovado”, senão exibir “Você está aprovado”.

Entrada: 7.0 5.0 Saída: 6.0 – Você está aprovado
Entrada: 4.5 3.5 Saída: 4.0 – Você está reprovado
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    print("Você está reprovado.")
else:
    print("Você está aprovado.")


"""
PROBLEMA 6: Dada uma nota, verificar se ela é válida, ou seja, se ela estiver entre 0 e 10 (inclusive) ela é uma
“Nota válida”, senão “Nota inválida”.

Entrada: 3.5 Saída: Nota válida
Entrada: 11.5 Saída: Nota Inválida
"""

nota = float(input("Digite uma nota: "))

if 0 <= nota <= 10:
    print("Essa é uma nota válida!")
else:
    print("Essa é uma nota inválida!")


"""
PROBLEMA 7: Juntar os dois exercícios anteriores, ou seja, pedir a digitação das duas notas, caso uma (ou as duas)
nota seja inválida exibir “Nota inválida!” e terminar o algoritmo; senão, calcular e exibir a média e
exibir se está aprovado (vide saída do exercício anterior).

Entrada: 10.0 4.0 Saída: 7.0 – Você está aprovado
Entrada: 2.0 3.0 Saída: 2.5 – Você está reprovado
Entrada: 14.0 Saída: Nota Inválida!
Entrada: 5.0 -6.0 Saída: Nota Inválida!
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    if media >= 5:
        print(f"A média é {media}.\nVocê está aprovado!")
    else:
        print(f"A média é {media}.\nVocê está reprovado!")
else:
    print("Nota inválida!")


"""
PROBLEMA 8: Dado um número pelo usuário, verifique se ele é “Positivo”, “Negativo” ou “Nulo”(igual a zero).

Entrada: 3 Saída: Positivo
Entrada: -5 Saída: Negativo
Entrada: 0 Saída: Nulo
"""

num = float(input("Digite um número: "))

if num > 0:
    print("Número positivo!")
elif num < 0:
    print("Número negativo!")
else:
    print("Número nulo!")


"""
PROBLEMA 9: Dadas três notas (AV1, AV2 e AV3), fazer um algoritmo que calcule a media. A média consiste em
descartar a menor nota entre as 3 médias calculando a média simples das outras duas. Exibir se o
aluno está “Aprovado” ou “Reprovado” (média menor do que 6).

Entrada: 3.0 7.0 5.0 Saída: 6.0 - Reprovado
Entrada: 5.5 6.0 7.5 Saída: 6.5 – Aprovado
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 > nota3 and nota2 > nota3:
    media = (nota1 + nota2) / 2
elif nota2 > nota1 and nota3 > nota1:
    media = (nota2 + nota3) / 2
elif nota3 > nota2 and nota1 > nota2:
    media = (nota1 + nota3) / 2

if media < 6:
    print(f"A média é {media}.\nReprovado!")
else:
    print(f"A média é {media}.\nAprovado!")


"""
PROBLEMA 10: Dentre três números dados pelo usuário, verificar e exibir o de maior valor.

Entrada: 10 6 17 Saída: 17
Entrada: 5 15 10 Saída: 15
Entrada: 5 -1 0 Saída: 5
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"O maior número é: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é: {num2}")
else:
    print(f"O maior número é: {num3}")
