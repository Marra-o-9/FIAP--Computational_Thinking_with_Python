"""
Prioridades:
1) Not     - Negação
2) And     - Conjunção
3) Or      - Disjunção

Not True = False
Not False = True

Expressão lógica:

True or False and not False
True or False and True
True or False
True
"""

# if encadeado "raiz"
num = int(input("Digite um número: "))

if num > 0:
    print("O número é positivo!")
else:
    if num < 0:
        print("O número é negativo!")
    else:
        print("O número é nulo!")

# if encadeado "elif"
num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo!")
elif num < 0:
    print("O número é negativo!")
else:
    print("O número é nulo!")

"""
Dado o salário de um funcionário, verificar quanto ele paga de INSS segundo a tabela:
No final, exibir o salário bruto, o desconto do INSS e o salário líquido. Teto 1052:
-----------------------
Salário: 1000 
Salário Bruto: 1000
INSS: 75
Salário Líquido: 925
"""

sal = float(input("Digite o seu salário: R$"))
inss1 = sal * 7.5 / 100
inss2 = sal * 9 / 100
inss3 = sal * 12 / 100
inss4 = sal * 14 / 100
inssmax = 1052

if inss1 > 1052:
    inss1 = 1052
elif inss2 > 1052:
    inss2 = 1052
elif inss3 > 1052:
    inss3 = 1052
elif inss4 > 1052:
    inss4 = 1052

if sal < 0:
    print("Salário negativo inválido!")
elif 0 < sal <= 1302:
    sal_liq = sal - inss1
    print(f"Salário bruto: R${sal}\nDesconto do INSS: R${inss1}\nSalário líquido: R${sal_liq}")
elif 1302 < sal <= 2571.29:
    sal_liq = sal - inss2
    print(f"Salário bruto: R${sal}\nDesconto do INSS: R${inss2}\nSalário líquido: R${sal_liq}")
elif 2571.29 < sal <= 3856.94:
    sal_liq = sal - inss3
    print(f"Salário bruto: R${sal}\nDesconto do INSS: R${inss3}\nSalário líquido: R${sal_liq}")
elif 3856.94 < sal <= 7507.49:
    sal_liq = sal - inss4
    print(f"Salário bruto: R${sal}\nDesconto do INSS: R${inss4}\nSalário líquido: R${sal_liq}")
else:
    sal_liq = sal - inssmax
    print(f"Salário bruto: R${sal}\nDesconto do INSS: R${inssmax}\nSalário líquido: R${sal_liq}")

"""
FORMA 1 - Correção do exercício INSS:     (   MUITO MAIS SIMPLES   )
"""

#Digitação do salário
sal = float(input("Digite seu salário: R$"))

#Análise do cálculo
if sal <= 1302:
    inss = sal * 0.07
elif sal <= 2571.29:     #como < 1302 já foi verificado, não há necessidade de colocar o valor novamente
    inss = sal * 0.09
elif sal <= 3856.94:
    inss = sal * 0.12
elif sal <= 7507.49:
    inss = sal * 0.14
else:
    inss = 1051.05

#Cálculo do salário líquido
sal_liq = sal - inss

#Exibição das informações
print(f"""
    Salário....: R${sal:8.2f}
    INSS.......: R${inss:8.2f}
    Salário Liq: R${sal_liq:8.2f}
""")

"""
FORMA 2 - Correção do exercício INSS:   (Utilizando somente o if simples)   (JEITO COCÔ)
"""

#Digitação do salário
sal = float(input("Digite seu salário: R$"))

#Análise do cálculo
if sal > 0 and sal <= 1302:
    inss = sal * 0.07

if sal > 1302 and sal <= 2571.29:
    inss = sal * 0.09

if sal > 2571.29 and sal <= 3856.94:
    inss = sal * 0.12

if sal > 3856.94 and sal <= 7507.49:
    inss = sal * 0.14

if sal > 7507.49:
    inss = 1051.05

#Cálculo do salário líquido
sal_liq = sal - inss

#Exibição das informações
print(f"""
    Salário....: R${sal:8.2f}
    INSS.......: R${inss:8.2f}
    Salário Liq: R${sal_liq:8.2f}
""")
