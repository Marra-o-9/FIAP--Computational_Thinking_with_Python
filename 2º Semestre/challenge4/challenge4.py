"""
1TIAF - GRUPO:

97672 - Henrique Marra Barbosa
551882 - Arthur Hieda Cunha
552162 - Lucas Bueno Taets Gustavo
99018 - Julia Cristina Ferreira Silva
552188 - Fabricio Yukio Yamashiro
550700 - Leonardo Vaidotas de Araujo
"""


def fazer_questionario(usuario):
    print("Bem-vindo ao questionário de planejamento do plantio de soja!")
    print("Responda as perguntas abaixo para obter informações úteis.")

    sugestao3 = ""
    sugestao4 = ""

    while True:
        try:
            resposta_periodo = int(input("Escreva o número do mês em que você gostaria de iniciar seu plantio: "))

            if resposta_periodo < 1 or resposta_periodo > 12:
                print("Digite um número válido.")
            else:
                if 9 <= resposta_periodo <= 11:
                    sugestao1 = "o período escolhido é a melhor época para o início do plantio de soja"
                elif resposta_periodo == 8 or resposta_periodo == 12:
                    sugestao1 = "o período escolhido é uma boa época para o início do plantio de soja"
                else:
                    sugestao1 = "não é recomendável que o início de seu plantio seja nesse mês, e sim algo próximo de setembro a novembro"
                break
        except ValueError:
            print("Digite um número válido.")

    while True:
        temperatura = float(input("Qual é a faixa de temperatura da sua região? "))

        try:
            if 20 <= temperatura <= 30:
                sugestao2 = "é muito favorável para o plantio da soja,"
                break
            elif 17 <= temperatura <= 19 or 31 <= temperatura <= 33:
                sugestao2 = "mostra que não está dentro da faixa ideal para o plantio, porém a soja ainda se adaptará ao clima,"
                break
            else:
                sugestao2 = "mostra que não é recomendado que o plantio seja feito nesse clima,"
                break
        except ValueError:
            print("Digite um valor numérico válido.")

    while True:
        resposta_soloargila = input("Seu solo é argiloso? [s]im ou [n]ão? ")

        if resposta_soloargila.lower() == "s":
            sugestao3 = "por se tratar de um solo argiloso, terá bons nutrientes para seu produto, a água será bem retida e também será menos provável uma compactação excessiva do solo"
            break
        elif resposta_soloargila.lower() == "n":
            while True:
                resposta_soloagua = input("Seu solo possui boa retenção de água? [s]im ou [n]ão? ")
                if resposta_soloagua.lower() == "s":
                    sugestao3 = "deverá focar nos nutrientes que beneficiarão seu produto"
                    break
                elif resposta_soloagua.lower() == "n":
                    sugestao3 = ""
                    break
                else:
                    print("Digite uma resposta válida (s ou n).")
            break
        else:
            print("Digite uma resposta válida (s ou n).")

    if resposta_soloargila.lower() != "s":
        while True:
            resposta_solorelevo = input("Seu solo possui um relevo plano? [s]im ou [n]ão? ")
            if resposta_solorelevo.lower() == "s":
                sugestao4 = "e o relevo de seu solo é perfeito para o plantio da soja."
                break
            elif resposta_solorelevo.lower() == "n":
                sugestao4 = "e o relevo de seu solo não é favorável para o plantio da soja."
                break
            else:
                print("Digite uma resposta válida (s ou n).")

    sugestao = f"Com base nas suas respostas, {sugestao1}, a faixa de temperatura de sua região {sugestao2} {sugestao3} {sugestao4}"

    usuario["sugestao"] = sugestao

    print("\nSugestão:")
    print(sugestao)


def conferir_email():
    while True:
        email = input("E-mail.......: ").lower()

        if not email[0].isalpha():
            print("E-mail inválido. Deve começar com uma letra.")
            continue
        
        contador_ponto_sobrenome = 0
        verificar = True
        try:
            nome, sobrenome = email.split("@")

            for i in nome and sobrenome:
                if i.isnumeric() == False and i.isalpha() == False and i != ".":
                    verificar = False

                if i == "." in sobrenome:
                    contador_ponto_sobrenome += 1

            if verificar == False:
                print("E-mail inválido. Não deve conter caracteres especiais além do '@'.")
                continue
            
        except ValueError:
            print("E-mail inválido. Deve conter '@' e caracteres antes e depois dele.")
            continue

        if contador_ponto_sobrenome > 2 and contador_ponto_sobrenome == 0:
            print("E-mail inválido. Deve conter entre 1 e 2 '.' no final.")
            continue

        contador_arroba = 0
        contador_ponto = 0
        for i in email:
            if i == "@":
                contador_arroba += 1
            if i == ".":
                contador_ponto += 1
        
        if contador_arroba != 1:
            print("E-mail inválido. Deve conter exatamente um '@'.")
            continue
        
        if contador_ponto < 1: 
            print("E-mail inválido. Deve conter pelo menos um '.'.")
            continue

        if "@." in email:
            print("E-mail inválido. O ponto não pode estar na sequência do arroba.")
            continue

        if ".." in email:
            print("E-mail inválido. Não pode haver pontos duplicados.")
            continue

        if email[-1] == ".":
            print("E-mail inválido. O ponto não pode estar no final.")
            continue

        return email


def cadastro_usuario(t, d, conferir):
    while True:
        try:
            d["celular"] = int(input("Celular......: "))
            break
        except ValueError:
            print("Digite somente números!")
            
    if conferir == True:
        for i in t:
            if d["celular"] == i["celular"]:
                print("Celular já cadastrado!")
                return
    while True:
        d["nome_completo"] = input("Nome.........: ").upper()
        if d["nome_completo"].replace(" ", "").isalpha():
            break
        print("Digite somente letras!")

    d["email"] = conferir_email()
    t.append(d.copy())

    with open("usuarios.txt", "a") as arq:
        arq.write(f"\n{d['celular']}, {d['nome_completo']}, {d['email']}")
    print("Cadastro realizado com sucesso!")


def login_usuario(t):
    while True:
        try:
            celular = int(input("Digite seu celular para fazer login: "))
            break
        except ValueError:
            print("Digite somente números!")

    for usuario in t:
        if usuario["celular"] == celular:
            print("Login bem-sucedido!")
            return usuario
    print("Usuário inexistente.")


def editar_usuario(usuario):
    print("\nEditar perfil:")

    while True:    
        usuario["nome_completo"] = input("Nome.........: ")
        if usuario["nome_completo"].replace(" ", "").isalpha():
            break
        print("Digite somente letras!")

    usuario["email"] = conferir_email()
    print("Perfil atualizado com sucesso!")

    with open("usuarios.txt", "r") as file:
        lines = file.readlines()

    with open("usuarios.txt", "w") as file:
        for line in lines:
            if str(usuario["celular"]) in line:
                file.write(f"{usuario['celular']}, {usuario['nome_completo']}, {usuario['email']}\n")
            else:
                file.write(line)


def verificar_sugestao(usuario):
    if "sugestao" in usuario:
        print("\nSugestão de plantio:")
        print(usuario["sugestao"])
    else:
        print("Você ainda não completou o questionário.")


tabela = []
dicionario = {}


def menu():
    sair = False
    conferir_usuario = False
    usuario_logado = None

    while usuario_logado is None:
        print("""\nMenu:
1. Cadastrar usuário
2. Logar usuário
0. Sair""")
        
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastro_usuario(tabela, dicionario, conferir_usuario)
                conferir_usuario = True

            case "2":
                if conferir_usuario:
                    usuario_logado = login_usuario(tabela)
                else:
                    print("ERRO: Você precisa cadastrar um usuário antes.")

            case "0":
                print("Saindo do programa. Até logo!")
                sair = True
                break

            case _:
                print("Opção inválida. Escolha uma opção válida.")
    
    while True:
        if sair == True:
            break

        print(f"""\nMenu:
1. Cadastrar usuário
2. Trocar login
3. Editar usuário atual
4. Fazer o questionário
5. Conferir resultado
0. Sair""")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastro_usuario(tabela, dicionario, conferir_usuario)
                
            case "2":
                usuario_logado = login_usuario(tabela)

            case "3":
                editar_usuario(usuario_logado)

            case "4":
                fazer_questionario(usuario_logado)

            case "5":
                verificar_sugestao(usuario_logado)

            case "0":
                print("Saindo do programa. Até logo!")
                sair = True

            case _:
                print("Opção inválida. Escolha uma opção válida.")

menu()
