"""
PROBLEMA 1: Dado o salário, calcular o quanto ele paga de IR e INSS
"""

sal_liq = float(input("Digite o seu salário: R$"))

if sal_liq <= 1302:
    inss = sal_liq * 7 / 100
elif sal_liq <= 2571.29:
    inss = sal_liq * 9 / 100
elif sal_liq <= 3856.94:
    inss = sal_liq * 12 / 100
elif sal_liq <= 7507.49:
    inss = sal_liq * 14 / 100
else:
    inss = 1051.05

if 0 <= sal_liq <= 1903.98:
    ir = 0
elif 1903.98 < sal_liq <= 2826.65:
    ir = (sal_liq * 7.5 / 100) - 142.80
elif 2826.65 < sal_liq <= 3751.05:
    ir = (sal_liq * 15 / 100) - 354.80
elif 3751.05 < sal_liq <= 4664.68:
    ir = (sal_liq * 22.5 / 100) - 636.13
else:
    ir = (sal_liq * 27.5 / 100) - 869.36

sal_bruto = sal_liq - ir - inss

print(f"""
    Salário Bruto: R${sal_bruto}
    INSS: R${inss}
    IR: R${ir}
    Salário Líquido: R${sal_liq}
""")


"""
PROBLEMA 2
"""

qtd_empr = int(input("Quantidade de empregos: "))
teto = False

if qtd_empr > 1:
    #há dois empregos
    sal_liq = float(input("Digite o seu salário: R$"))
    if sal_liq <= 1302:
        inss = sal_liq * 7 / 100
    elif sal_liq <= 2571.29:
        inss = sal_liq * 9 / 100
    elif sal_liq <= 3856.94:
        inss = sal_liq * 12 / 100
    elif sal_liq <= 7507.49:
        inss = sal_liq * 14 / 100
    else:
        # paga no teto
        teto = True
        inss = 1051.05

    if teto == True:
        #não cobrar o inss do segundo emprego
        inss2 = 0
        sal_liq2 = float(input("Digite o seu salário: R$"))
    else:
        #cobrar o inss do segundo emprego
        sal_liq2 = float(input("Digite o seu salário: R$"))
        if sal_liq2 <= 1302:
            inss2 = sal_liq2 * 7 / 100
        elif sal_liq2 <= 2571.29:
            inss2 = sal_liq2 * 9 / 100
        elif sal_liq2 <= 3856.94:
            inss2 = sal_liq2 * 12 / 100
        elif sal_liq2 <= 7507.49:
            inss2 = sal_liq2 * 14 / 100
        else:
            inss2 = 1051.05

else:
    sal_liq = float(input("Digite o seu salário: R$"))
    if sal_liq <= 1302:
        inss = sal_liq * 7 / 100
    elif sal_liq <= 2571.29:
        inss = sal_liq * 9 / 100
    elif sal_liq <= 3856.94:
        inss = sal_liq * 12 / 100
    elif sal_liq <= 7507.49:
        inss = sal_liq * 14 / 100
    else:
        #paga no teto
        teto = True
        inss = 1051.05
