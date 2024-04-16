"""
PROBLEMA 14: Dados três números pelo usuário, exibi-los em ordem crescente.

Entrada: 1 2 3      Saída: 1 2 3
Entrada: 1 3 2      Saída: 1 2 3
Entrada: 2 1 3      Saída: 1 2 3
Entrada: 2 3 1      Saída: 1 2 3
Entrada: 3 1 2      Saída: 1 2 3
"""

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f"Os números em ordem crescente são: {n3}, {n2}, {n1}.")
    else:
        print(f"Os números em ordem crescente são: {n2}, {n3}, {n1}.")
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f"Os números em ordem crescente são: {n3}, {n1}, {n2}.")
    else:
        print(f"Os números em ordem crescente são: {n1}, {n3}, {n2}.")
else:
    if n1 > n2:
        print(f"Os números em ordem crescente são: {n2}, {n1}, {n3}.")
    else:
        print(f"Os números em ordem crescente são: {n1}, {n2}, {n3}.")


"""
PROBLEMA 15: Dados três números pelo usuário, analisá-los e exibir a mensagem “3 números diferentes”, “2 dos 3
são iguais” ou “3 números iguais”.

Entrada: 1 2 3      Saída: 3 números diferentes
Entrada: 1 2 2      Saída: 2 dos 3 são iguais
Entrada: 2 1 2      Saída: 2 dos 3 são iguais
Entrada: 2 2 1      Saída: 2 dos 3 são iguais
Entrada: 3 3 3      Saída: 3 números iguais
"""

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 == n2 == n3:
    print("3 números iguais.")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("2 dos 3 números são iguais.")
else:
    print("3 números diferentes.")


"""
PROBLEMA 16: Dado o salário de uma pessoa, sexo (1 para Masculino e 2 para Feminino) e idade, verificar a tabela
abaixo e calcular a devida cobrança de convênio médico sobre o salário informado:

Idade                       Masculino       Feminino
Até 20 anos                 5,34%           3,56%
Acima de 20 até 40 anos     8,44%           6,43%
Acima dos 40 anos           10,12%          8,02%

Entrada: 1500.00 1 45       Saída: Valor do convenio: R$ 80.10
Entrada: 1600.00 2 42       Saída: Valor do convenio: R$ 56.96
Entrada: 2123.43 1 19       Saída: Valor do convenio: R$ 113.39
Entrada: 2600.00 2 18       Saída: Valor do convenio: R$ 92.96
Entrada: 2000.00 1 30       Saída: Valor do convenio: R$ 168.80
Entrada: 2000.00 2 29       Saída: Valor do convenio: R$ 128.60
"""

sal = float(input("Digite o seu salário: "))
sex = int(input("Masculino[1] ou Feminino[2]: "))
age = int(input("Digite sua idade: "))

if age < 20:
    if sex == 1:
        con = sal * 5.34 / 100
    else:
        con = sal * 3.56 / 100
elif 20 <= age < 40:
    if sex == 1:
        con = sal * 8.44 / 100
    else:
        con = sal * 6.43 / 100
else:
    if sex == 1:
        con = sal * 10.12 / 100
    else:
        con = sal * 8.02 / 100

print(f"Valor do convênio: R${con:.2f}")

"""
PROBLEMA 17: Um professor usa Provas e Atividades para compor a nota AV1. Ele usa 2 provas e 4 atividades (os
valores são digitados nesta ordem). A média das provas vale 60% da AV1 enquanto que as
atividades valem 0 ou 1 ponto cada. Considerando que a media é 6,0 faça um algoritmo que calcule
a AV1 e mostre a mensagem: “AV1 = X.X, você está acima da média.”, “AV1 = 6.0, você está na
média.” ou “AV1 = X.X, você está abaixo da média.”.

Entrada: 4.0 5.0     1 1 1 0     Saída: AV1 = 5.7, você está abaixo da média.
Entrada: 6.0 4.0     0 1 1 1     Saída: AV1 = 6.0, você está na média.
Entrada: 7.0 5.0     1 1 1 1     Saída: AV1 = 7.6, você está acima da média.
"""

p1 = float(input("Digite o valor da prova 1: "))
p2 = float(input("Digite o valor da prova 2: "))
a1 = int(input("Digite o valor da atividade 1: "))
a2 = int(input("Digite o valor da atividade 2: "))
a3 = int(input("Digite o valor da atividade 3: "))
a4 = int(input("Digite o valor da atividade 4: "))

media = (p1 + p2) / 2
av1 = (media * 60 / 100) + a1 + a2 + a3 + a4

if av1 < 6:
    print(f"Avaliação 1 = {av1}\nVocê está abaixo da média.")
elif av1 == 6:
    print(f"Avaliação 1 = {av1}\nVocê está na média.")
else:
    print(f"Avaliação 1 = {av1}\nVocê está acima da média.")


"""
PROBLEMA 18: Dados 3 numero pelo usuário, verificar se são diferentes, se forem, exibir o número com valor
intermediário, senão (se houver 2 ou 3 números iguais) exibir a mensagem “Os números não são
diferentes”.

Entrada: 4 9 7      Saída: 7
Entrada: 14 7 7     Saída: Os números não são diferentes
Entrada: 12 2 30    Saída: 12
Entrada: 3 3 3      Saída: Os números não são diferentes
Entrada: 45 67 76   Saída: 67
"""

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 == n2 or n2 == n3 or n1 == n3:
    print("Os números não são diferentes.")
elif n2 > n1 > n3 or n3 > n1 > n2:
    print(f"Número intermediário: {n1}")
elif n1 > n2 > n3 or n3 > n2 > n1:
    print(f"Número intermediário: {n2}")
else:
    print(f"Número intermediário: {n3}")


"""
PROBLEMA 19: Dados 3 valores numéricos correspondentes a eventuais lados de triângulo, verificar se esses
valores formam um triângulo (para cada lado, a soma dos outros dois lados deve ser maior do que
ele). Se formar, exibir a mensagem “Forma um triângulo”, senão “Não forma um triângulo”.

Entrada: 10 11 12   Saída: Forma um triângulo
Entrada: 2 7 10     Saída: Não forma um triângulo
Entrada: 4 7 7      Saída: Forma um triângulo
Entrada: 34 10 14   Saída: Não forma um triângulo
Entrada: 15 15 15   Saída: Forma um triângulo
"""

l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print("Esses lados formam um triângulo.")
else:
    print("Esses valores não formam um triângulo.")


"""
PROBLEMA 20: Dados 3 valores numéricos correspondentes a eventuais lados de triângulo, verificar se esses
valores formam um triângulo (para cada lado, a soma dos outros dois lados deve ser maior do que
ele). Em caso afirmativo, informar ao usuário se o triângulo é equilátero (três lados iguais),
isósceles (dois lados iguais) ou escaleno (três lados diferentes). Em caso negativo, exibir “Não forma
um triângulo”.

Entrada: 10 11 12   Saída: Triângulo Escaleno
Entrada: 2 7 10     Saída: Não forma um triângulo
Entrada: 4 7 7      Saída: Triângulo Isósceles
Entrada: 34 10 14   Saída: Não forma um triângulo
Entrada: 15 15 15   Saída: Triângulo Equilátero
"""

l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    if l1 == l2 == l3:
        print("Esses lados formam um Triângulo Equilátero.")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("Esses lados formam um Triângulo Escaleno.")
    else:       #elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Esses lados formam um Triângulo Isósceles.")
else:
    print("Esses valores não formam um triângulo.")

"""
PROBLEMA 21: Dado o ano pelo usuário, verificar se o ano é bissexto exibindo a mensagem “Ano bissexto” ou
“Não é ano bissexto”. Sabe-se que o ano bissexto é aquele que é múltiplo de 4, exceto os múltiplos
de 100 que não sejam múltiplos de 400. Por exemplo: 1996, 2004, 2008, 2012, 1600, 2000 e 2400
(são bissextos); 1700, 1800, 1900 e 2100 (não são bissextos).

Entrada: 2013       Saída: Não é ano bissexto
Entrada: 2008       Saída: É ano bissexto
Entrada: 1881       Saída: Não é ano bissexto
Entrada: 2012       Saída: É ano bissexto
"""

ano = int(input("Digite o ano: "))

if ano % 4 != 0 or ano % 100 == 0 and ano % 400 != 0:
    print(f"O ano {ano} não é bissexto.")
else:
    print(f"O ano {ano} é bissexto.")
