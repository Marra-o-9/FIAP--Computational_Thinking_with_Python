arquivo = open("primeiro_arquivo.txt", "w") # w = novo arquivo

arquivo.write("Meu primeiro arquivo manipulado.")

arquivo.close()

with open("primeiro_arquivo.txt", "a") as arquivo:  # a = append no arquivo
    arquivo.write(f"\nNumeri Oficial")

with open("primeiro_arquivo.txt", "r") as arquivo:  # r = ler arquivo
    #conteudo = arquivo.read()  lê o arquivo todo
    #print(conteudo)
    conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)