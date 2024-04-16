tabuada = int(input("Digite um número para exibir a tabuada: "))
print(f"Tabuada do número {tabuada}:")
for valor in range(1, 11, 1):   #(valor inicial, valor limite, o passo que ele dá)
    print(f"\t{tabuada} x {valor} = {tabuada * valor}")

#for é usado para definir uma variável passo a passo
