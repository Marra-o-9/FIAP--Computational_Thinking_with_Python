#While (laço pré-condicional)

numero = 3
while numero != 8:
    numero += 1

print(numero)


#Exemplo

#Ler o valor inicial
n_atual = int(input("Digite o valor inicial: "))
#Ler o valor final
n_final = int(input("Digite o valor final: "))

while n_atual < n_final:
    #Exibir o número atual ao usuário
    print(n_atual)
    #Somar 1 ao numero atual, atualizando a variável
    n_atual += 1

print(n_atual)


#Loop infinito (não fazer)
"""
while n_atual < n_final:
    if n_atual < 6:
        print(n_atual)
        n_atual += 1
"""


"""
PROBLEMA 1: Dados dois números, exibir os número do intervalo fechado.
Se o primeiro número digitado for maior que o segundo, exibir a mensagem:
"O primeiro número deve ser menor", e encerrar o programa.
"""

n1 = int(input("Digite o valor inicial: "))
n2 = int(input("Digite o valor final: "))

if n1 > n2:
    print("O primeiro número deve ser menor.")
else:
    while n1 != n2:
        print(n1)
        n1 += 1
    print(n1)


#Break e Continue (comandos preguiçosos [e úteis!])

n1 = int(input("Digite o valor inicial: "))
n2 = int(input("Digite o valor final: "))

while n1 != n2:
    print(n1)
    n1 += 1
    if n1 < 6:
        continue  #retorna ao início do laço (continua voltando até uma condição acontecer)
    if n1 > 10:
        break  #sai do laço incondicionalmente (quebra o while e sai dele)
else:  #é executado caso não haja interferência no laço
    print("O laço foi executado normalmente.")


#While True (laço pós-condicional) - simulação, pois não existe comando próprio no Python

n1 = int(input("Digite o valor inicial: "))
n2 = int(input("Digite o valor final: "))

while True:
    print(n1)
    n1 += 1
    print("Executou o bloco de repetição.")
    if n1 > n2:
        break


opcao = "s"
#while opcao == "s" or opcao == "S":
while opcao.upper() == "S":  #deixa o caractere maiúsculo
    n1 = int(input("Digite o valor inicial: "))
    n2 = int(input("Digite o valor final: "))

    while n1 != n2:
        print(n1)
        n1 += 1

    opcao = input("Deseja continuar? [s]im ou [n]ão? ").upper()
    #while opcao.upper() != "S" and opcao.upper() != "N":  -> recurso de função
    while opcao != "S" and opcao != "N":
        print("Erro! Digite [s] ou [n]")

"""
    while opcao not in ["s", "S", "n", "N"]:    #utilizando operador de conjunto(in)
    opcao = input("Deseja continuar? [s]im ou [n]ão? ")
"""