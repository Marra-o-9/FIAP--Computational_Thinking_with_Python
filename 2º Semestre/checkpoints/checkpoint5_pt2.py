# Henrique Marra Barbosa - 97672

while True:
    email = input("Digite o e-mail: ")

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

    break

with open("RM97672.txt", "w+") as arq:
    arq.write(email)
