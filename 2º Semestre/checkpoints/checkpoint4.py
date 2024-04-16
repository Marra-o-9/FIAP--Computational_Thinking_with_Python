#Henrique Marra Barbosa - 97672


#--------------------------------------- SUB ALGORITMOS ---------------------------------------


def menu():
    print(f"""
MENU

0 - SAIR
1 - Digite um nome completo
2 - Exibe separado o Nome do Sobrenome
3 - Conta quantas palavras há no nome completo
4 - Exibir em formato de bibliografia
""")


def nome_completo():
    while True:
        nome = input("Digite um nome completo: ")
        if nome.isnumeric() == True:
            print(f"ERRO: Digite somente letras!")
            continue
        print(f"Nome completo: {nome}")
        return nome


def exibir_separado(nome):
    separado = nome.split()
    print(f"Nome: ", end="")
    print(f"{separado[0]}")
    print(f"Sobrenome: ", end="")
    for i in range(1, len(separado)):
        print(f"{separado[i]}", end=" ")


def contar_palavras(nome):
    separado = nome.split()
    print(f"O nome {nome} possui {len(separado)} palavras.")


def nome_bibliografia(nome):
    separado = nome.split()
    print(f"{separado[len(separado) - 1].upper()},", end=" ")
    for i in range(0, len(separado) - 1):
        print(f"{separado[i]}", end=" ")


#------------------------------------- PROGRAMA PRINCIPAL -------------------------------------


conferir_nome = False
while True:
    menu()
    escolha = input("Opção: ")    
    match escolha:
        case "1":
            nome_user = nome_completo()
            conferir_nome = True
        case "2":
            if conferir_nome == False:
                print("ERRO: Primeiramente, digite um nome na opção 1!")
                continue
            exibir_separado(nome_user)
        case "3":
            if conferir_nome == False:
                print("ERRO: Primeiramente, digite um nome na opção 1!")
                continue
            contar_palavras(nome_user)
        case "4":
            if conferir_nome == False:
                print("ERRO: Primeiramente, digite um nome na opção 1!")
                continue
            nome_bibliografia(nome_user)
        case "0":
            break
        case _:
            print("ERRO: Escolha uma opção válida!")
            