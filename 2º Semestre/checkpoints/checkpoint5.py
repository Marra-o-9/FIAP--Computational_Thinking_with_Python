# Henrique Marra Barbosa - 97672


# SUB ALGORITMOS


def preenche_registro(t, reg):
    print("PREENCHENDO O REGISTRO")
    reg['instagram'] = input("Instagram...: ")
    reg['nome'] = input("Nome........: ")
    reg['celular'] = input("Celular.....: ")
    t.append(reg.copy())


def exibe_registro(t, i):
    print(f"REGISTRO {i}:")
    print("Instagram...:"+t[i]['instagram'])
    print("Nome........:"+t[i]['nome'])
    print("Celular.....:"+t[i]['celular'])
    print()


def exibe_tabela(t):
    qtd_registros = len(t)
    for indice in range(qtd_registros):
        exibe_registro(t, indice)


# EXERCÍCIO 3


def preencha_registros(t, reg):
    while True:
        print("PREENCHENDO O REGISTRO")
        reg['instagram'] = input("Instagram...: ")
        if reg['instagram'] == ".":
            break
        reg['nome'] = input("Nome........: ")
        reg['celular'] = input("Celular.....: ")
        t.append(reg.copy())


# EXERCÍCIO 4


def consulta_registro(t, reg):
    busca = input("Digite o Instagram do usuário: @")
    for i in t:
        if busca == i["instagram"]:
            print(f"REGISTRO {i}:")
            print("Instagram...:" + reg["instagram"])
            print("Nome........:" + reg["nome"])
            print("Celular.....:" + reg["celular"])
            break
    else:
        print("Instagram não existente!")


# EXERCÍCIO 5


def cadastro_registro_consulta(t, reg):
    print("PREENCHENDO O REGISTRO")
    busca = input("Instagram...: ")
    for i in t:
        if busca == i["instagram"]:
            print("Instagram já cadastrado!")
            break
    else:
        reg['instagram'] = busca
        reg['nome'] = input("Nome........: ")
        reg['celular'] = input("Celular.....: ")
        t.append(reg.copy())


# EXERCÍCIO 6


def edicao_registro_consulta(t):
    busca = input("Digite o Instagram para fazer a edição: ")
    for i in range(len(t)):
        if busca == t[i]["instagram"]:
            t[i]['instagram'] = input("Instagram...: ")
            t[i]['nome'] = input("Nome........: ")
            t[i]['celular'] = input("Celular.....: ")
            break
    else:
        print("Instagram não existente!")


# PROGRAMA PRINCIPAL


tabela = list()
contato = dict()

while True:
    print("""0 - SAIR
1 - CADASTRAR UM CONTATO
2 - EXIBIR OS CONTATOS CADASTRADOS
3 - PREENCHA REGISTROS
4 - CONSULTA REGISTRO
5 - CADASTRAR UM CONTATO COM CONSULTA
6 - EDIÇÃO COM CONSULTA
""")
    opcao = int(input("Digite uma opção desejada...: "))
    match opcao:
        case 0:
            break
        case 1:
            preenche_registro(tabela, contato)
        case 2:
            exibe_tabela(tabela)
        case 3:
            preencha_registros(tabela, contato)
        case 4:
            consulta_registro(tabela, contato)
        case 5:
            cadastro_registro_consulta(tabela, contato)
        case 6:
            edicao_registro_consulta(tabela)
        case _:
            print("Opção inválida!")
