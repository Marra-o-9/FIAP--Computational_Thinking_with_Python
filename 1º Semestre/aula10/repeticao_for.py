#For (laço contador)

"""
Sintaxe:
for <contador> in range(início, fim, intervalos)
    <bloco de repetição>
"""

for contador in range(1, 10 + 1, 1):    #contador pode ser qualquer variável
    print(contador)                     #range busca do valor inicial até o valor final

#ou

inicio = 0
fim = 10
intervalo = 1
for contador in range(inicio, fim + 1, intervalo):    #o valor final é sempre exibido como um anterior
    print(f"{contador} ", end="")                     #end printa tudo junto eu acho
#sempre será de acordo com o intervalo

inicio = 10
fim = 0
intervalo = -1
for contador in range(inicio, fim - 1, intervalo):    #o valor final é sempre exibido como um anterior
    print(f"{contador} ", end="")
#intervalo negativo de acordo com os valores finais e iniciais
#laço contador é útil quando eu sei quantas voltas eu tenho que dar no programa


contador = 0                    #isso aqui = inicio
volta = 1
while volta <= 5:               #isso aqui = fim
    n = int(input("Número: "))
    contador += n
    volta += 1                  #isso aqui = incremento
print(f"Soma: {contador}")

#ou melhor

contador = 0
volta = 1
for volta in range(0, 5, 1):
    n = int(input("Número: "))
    contador += n
print(f"Soma: {contador}")
