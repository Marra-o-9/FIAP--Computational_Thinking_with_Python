#PROBLEMA 1: Calcular o dobro de um número.

#Dado um número pelo usuário
numero = (input("Número que será dobrado: "))
numero = float(numero)

#Calcular o dobro
resultado = numero * 2

#Exibir o resultado
print("O dobro de", numero, "é:", resultado)


#PROBLEMA 2: Dados os valores da base e do expoente, calcule a potência.
num = float(input("Digite a base: "))
num2 = float(input("Digite o expoente: "))

resultado = num ** num2

print(f"O resultado da potência de base {num} com o expoente {num2} é:", resultado)


"""
PROBLEMA 3: Dados dois valores pelo usuário, exibir na tela as respostas de
todas as operações aritméticas.

Exemplo:
Digite o n1: 10
Digite o n2: 3
Soma de 10 com 3 é 13
Subtração de 10 com 3 é 7
/
*
//
%
**
"""

num1 = float(input("Digite o primeiro valor das operações: "))
num2 = float(input("Digite o segundo valor das operações: "))

print(f"Soma de {num1} com {num2} é:", num1 + num2)
print(f"Subtração de {num1} com {num2} é:", num1 - num2)
print(f"Divisão de {num1} com {num2} é:", num1 / num2)
print(f"Multiplicação de {num1} com {num2} é:", num1 * num2)
print(f"Divisão inteira de {num1} com {num2} é:", num1 // num2)
print(f"Módulo de {num1} com {num2} é:", num1 % num2)
print(f"Exponenciação de {num1} com {num2} é:", num1 ** num2)

#Melhor forma:
print(f"""
    Soma de {num1} com {num2} é: {num1 + num2}
    Subtração de {num1} com {num2} é: {num1 - num2}
    Divisão de {num1} com {num2} é: {num1 / num2}
    Multiplicação de {num1} com {num2} é: {num1 * num2}
    Divisão inteira de {num1} com {num2} é: {num1 // num2}
    Módulo de {num1} com {num2} é: {num1 % num2}
    Exponenciação de {num1} com {num2} é: {num1 ** num2}
""")


"""
PROBLEMA 4: Dado um número pelo usuário, calcule o seu cubo.
"""

base = int(input("Digite um número para ser elevado ao cubo: "))

resultado = base ** 3

print(f"A base {base} elevada ao cubo resulta em: {resultado}")


"""
PROBLEMA 5: Dados os valores de a, b e c pelo usuário, calcule o valor de delta.
"""

valor_a = float(input("Digite o valor de a: "))
valor_b = float(input("Digite o valor de b: "))
valor_c = float(input("Digite o valor de c: "))

quadrado_b = valor_b ** 2
ac_4 = -4 * valor_a * valor_c
delta = quadrado_b + ac_4

print(f"O valor de delta é: {delta}")


"""
PROBLEMA 5: Faça um algoritmo que calcule a média de 4 números dados pelo usuário.

Entrada: 4 6 5 7
Saída: 5.5
"""

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))

media = (n1 + n2 + n3 + n4) / 2

print(f"A média dos números solicitados é {media}.")
