# Comandos de decisão

"""
Operadores relacionais

>       Maior
>=      Maior ou igual
<       Menor
<=      Menor ou igual
!=      Diferença
==      Igualdade
"""

x = 10 > 5
print(x)
x = 21 >= 4
print(x)
x = 12 < 10
print(x)
x = 2 + 3 <= 5 - 1
print(x)
x = "A" != "a"
print(x)
x = 25 == 5 * 2
print(x)


"""
PROBLEMA: Dado um número, calcule o módulo (matemático)
"""

numero = float(input("Digite um número para fazer o módulo: "))

if numero < 0:
    numero = numero * -1

print(numero)


"""
PROBLEMA 2: Dado o valor de uma venda, efetue 5% de desconto caso a venda seja maior que 500 (utilize o "se então")
"""

valor = float(input("Digite o valor da venda: "))

if valor > 500:
    desconto = valor * 5/100   #valor = valor * 0.95
    valor = valor - desconto

print(f"A venda tem o valor de {valor}.")


"""
Fórmulas de porcentagem:

Porcentagem =          1000 . 10 / 100
Acréscimo =     1000 + 1000 . 10 / 100
Diminuir =      1000 - 1000 . 10 / 100
"""


"""
PROBLEMA 3: Dada uma venda, efetue o desconto devido.
Se for maior que 500 reais, desconto de 12%, senão, desconto de 6%.
"""

venda = float(input("Digite o valor da venda: "))

if venda > 500:
    venda = venda - venda * 12/100
else:
    venda = venda - venda * 6/100

print(f"A venda tem o valor de {venda}.")

"""
PROBLEMA 4: À partir de uma venda, o cliente ganha 12% se for acima de 500 ou 6% abaixo.
Caso ele tenha um cupom, ganhará mais 20 reais de desconto.
Faça um programa que pegue a venda e mostre no final a venda e o novo valor da venda com os descontos.

Venda: 5000
Tem cupom? [s]im ou [n]ao: s
Venda: 5000
Com desconto:4380
"""

vendainicial = venda = float(input("Digite o valor da venda: "))
cupom = str(input("Tem cupom? [s]im ou [n]ão? "))   #Eu não precisaria ter usado str, input já é um dado texto

if venda > 500:
    venda = venda - venda * 12/100
else:
    venda = venda - venda * 6/100
if cupom == "s" or cupom == "S":    #Operador lógico diminui a possibilidade de erros
    venda = venda - 20

print(f"Valor original da venda: {vendainicial}\nValor atual da venda: {venda}")
