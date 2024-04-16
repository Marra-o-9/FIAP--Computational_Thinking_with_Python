inventario = []     #criação de uma lista vazia
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))   #.append = pedir ao usuário para inserir um item na lista "inventario"
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial:")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()
    # .upper() usada para prevenir erros do user no input, corrige o caps lock
    # \ antes das " foi utilizada para o python entender que as aspas precisavam ser exibidas

for elemento in inventario:
    print(elemento)
