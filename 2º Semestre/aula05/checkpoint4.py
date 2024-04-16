#Henrique Marra Barbosa - 97672


#---------------------------------------- SUB ALGORITMOS -----------------------------------------


def exibir_dicionario(dicionario):
    print(f"\n**Dicionário**\n")
    for key, value in dicionario.items():
        print(f"{key}: {value}")
    print(f"\n")


def exibir_menu():
    escolha = input("""1 - Inserir um campo no dicionário
2 - Alterar o valor de um campo
3 - Exibir um campo do dicionário
0 - SAIR

Escolha qual operação deseja fazer: """)
    return escolha


def inserir_key(dicionario):
    while True:
        nova_key = input("Insira o nome da key, ou VOLTAR: ")

        if nova_key.upper() == "VOLTAR":
            return
        
        valor = input("Insira o valor desta key: ")

        dicionario[nova_key] = valor
        break


def alterar_valor(key, dicionario):
    if key in dicionario:
        novo_valor = input(f"Digite um novo valor para {key}: ")
        dicionario[key] = novo_valor

    else:
        print("ERRO: Esta key não existe para ser alterada!")
       

def exibir_valor(dicionario):
    escolha = input(f"Digite o nome da key a qual quer exibir, ou VOLTAR: ")
    if escolha.upper() == "VOLTAR":
            return

    if escolha in dicionario:
        valor = dicionario[escolha]
        print(f"""Key: {escolha}
        Valor: {valor}""")

    else:
        print("ERRO: Esta key não existe para ser exibida!")


#-------------------------------------- PROGRAMA PRINCIPAL ---------------------------------------


dic = {}
dic = {
    "Perspectivas": "lançada",
    "Eles me Ouvirão": "gravada",
    "Tempo que me Resta": "gravada",
    "Cansei de Esperar": "finalizada",
    "Filtros": "composição",
    "Trend": "composição",
    "Buraco Negro": "composição"
}

print("""Olá, este é um programa para edição de dicionários!
Como exemplo, aqui está um dicionário sobre o estado das músicas da banda Numeri (a minha banda!)""")

while True:
    exibir_dicionario(dic)
    match exibir_menu():
        case "1":
            inserir_key(dic)
        case "2":
            alterar = input(f"Digite o nome da key a qual quer mudar o valor, ou VOLTAR: ")
            if alterar.upper() == "VOLTAR":
                continue
            alterar_valor(alterar, dic)
        case "3":
            exibir_valor(dic)
        case "0":
            print("Com suas modificações, o dicionário ficou deste jeito:")
            exibir_dicionario(dic)
            break
        case _:
            print("Digite uma operação válida!")
            continue
