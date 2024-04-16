print("""
    1 - Cadastro
    2 - Consulta
    3 - Alteração
    4 - Exclusão
""")

#ou
"""
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    print("Efetuando o cadastro.")
elif opcao == 2:
    print("Efetuando a consulta.")
elif opcao == 3:
    print("Efetuando a alteração.")
elif opcao == 4:
    print("Efetuando a exclusão.")
else:
    print("Opção inválida, digite uma opção entre 1 e 4.")
"""

#ou
"""
opcao = input("Digite a opção desejada: ")

    match opcao:
        case "1":     
            print("Efetuando o cadastro.")
        case "2":
            print("Efetuando a consulta.")
        case "3":
            print("Efetuando a alteração.")
        case "4":
            print("Efetuando a exclusão.")
        case _:     #o _ serve como um else para o match, else não funciona aqui
            print("Opção inválida, digite uma opção entre 1 e 4.")
"""

"""
opcao = int(input("Digite a opção desejada: ")) #privilegiar números no match ao invés de strings

match opcao:    
    case 1:     
        print("Efetuando o cadastro.")
    case 2:
        print("Efetuando a consulta.")
    case 3:
        print("Efetuando a alteração.")
    case 4:
        print("Efetuando a exclusão.")
    case _:     
        print("Opção inválida, digite uma opção entre 1 e 4.")
"""

opcao = input("Digite a opção desejada: ")

if opcao.isdigit():  #isdigit = só se o valor digitado for um número ele prossegue com o código
    opcao = int(opcao)
    match opcao:     #serve para escolher entre valores digitados pelo usuário
        case 1:      #não compara com sinal de maior ou menor, só equivalência
            print("Efetuando o cadastro.")
        case 2:
            print("Efetuando a consulta.")
        case 3:
            print("Efetuando a alteração.")
        case 4:
            print("Efetuando a exclusão.")
        case _:      #o _ serve como um else para o match, else não funciona aqui
            print("Opção inválida, digite uma opção entre 1 e 4.")
else:
    print("Erro, digite um número.")

#Correção da prova e aplicação do isdigit

'''
Reajuste
SM 1302
• até dois salários-mínimos, terá o reajuste de 6,45%.
• cinco salários-mínimos, terá o reajuste de 4,55% .
• mais de cinco salários-mínimos, o reajuste será de 2,89%.

Bonus*
1000 Reais
Para quem não teve faltas

Requisitos:
• Se for digitado um salário negativo, exibir a mensagem: “ERRO! Digite um salário positivo!” e o programa deve
terminar.
• Caso seja digitado um número negativo na quantidade de faltas, considerar que não tem filhos e prosseguir com os
cálculos e exibições.

**1 Verificar se a qtd de faltas é numerica ou nao
se numerica, calcula
senao mensagem de erro e termina o programa
**2 Verificar se o salario é numerico
se numerico, calcula
senao mensagem de erro e termina o programa
'''

sal = input("Salario: ")
if sal.isdigit():
    sal = float(sal)

    if sal < 0:
        print("ERRO! Digite um salário positivo!")
    else:
        qtd_faltas = input("Faltas: ")

        if qtd_faltas.isdigit():
            qtd_faltas = int(qtd_faltas)
            sal_min = 1302

            if sal <= sal_min * 2:
                reajuste = sal * 0.0645
            elif sal <= sal_min * 5:
                reajuste = sal * 0.0455
            else:
                reajuste = sal * 0.0289

            sal_reajustado = sal + reajuste

            if qtd_faltas <= 0:
                bonus = 1000
                faltas = 0
            else:
                bonus = 0
            print(f"""
                Faltas: {qtd_faltas}
    
                Salário..............: R$ {sal:9.2f}
                Salário reajustado...: R$ {sal_reajustado:9.2f}
                Bônus................: R$ {bonus:9.2f}
                """)
        else:
            print("ERRO! Digite um número!")
else:
    print("ERRO! Digite um número!")

#prova feia, prof tirou 2 no meu conceito
