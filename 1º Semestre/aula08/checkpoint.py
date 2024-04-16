#Henrique Marra Barbosa

sal_fun = float(input("Digite o seu salário: R$"))
sal_min = 1302.00

if sal_fun < 0:
    print(f"""
    ERRO! Digite um salário positivo!
    O salário {sal_fun} não é válido!
    """)
else:
    if sal_fun <= (sal_min * 2):
        reajuste = 6.45 / 100
    elif sal_fun <= (sal_min * 5):
        reajuste = 4.55 / 100
    else:
        reajuste = 2.89 / 100

    faltas = int(input("Digite o número de faltas: "))
    if faltas <= 0:
        bonus = 1000.00
        faltas = 0
    else:
        bonus = 0.00

    sal_reajustado = sal_fun + (sal_fun * reajuste)
    sal_total = sal_reajustado + bonus

    print(f"""
    Salário.............: R${sal_fun:.2f}
    Salário Reajustado..: R${sal_reajustado:.2f}
    Bônus...............: R${bonus:.2f}
    Salário Total.......: R${sal_total:.2f}
    
    Faltas..............: {faltas}
    """)
