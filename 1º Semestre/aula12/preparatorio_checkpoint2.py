"""
EXERCICIOS (Utilizar laços em todos):
1 - Dado um número e um multiplo, exibir o próximo multiplo a partir do numero
---------------------
Numero: 6
Multiplo: 5
Proximo multiplo: 10
----------------------
"""

numero = 6
multiplo = 5


for i in range(multiplo, numero, 1):
    if numero % 5 != 0:
        numero += 1
    else:
        break


"""
2 - Dado um numero, exibir o seu fatorial: 4! = 4 . 3 . 2 . 1 = 24
---------------------
Numero: 4   
Fatorial: 24
----------------------
"""

numero = int(input("Digite um número: "))

for fatorial in range(numero - 1, 0 - 1, -1):
    print(fatorial, end=" ")
    if fatorial > 0:
        numero *= fatorial

print(f"\n{numero}")


"""
3 - Dada a base e o expoente, exibir a potencia 2 . 2 . 2 . 2 = 16 | Utilizar multiplicações sucessivas 
---------------------
Base: 2   
Expoente: 4
Potencia: 16
----------------------
"""

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))





"""
4 - Dados dois numeros que representam um intervalo, exibir os numeros multiplos de 5 deste intervalo.
---------------------
Inicio: 12   
Fim: 34
Mult 5: 15 20 25 30
----------------------

5 - Dados dois numeros que representam um intervalo, e um numero N que representa o multiplo, exibir os numeros 
multiplos de N deste intervalo
---------------------
Inicio: 10   
Fim: 47
mult: 10
Multiplos: 10 20 30 40
----------------------

6 - Dado um numero, informar se ele é primo ou não (primo é aquele numero divisivel somente por 1 e ele mesmo)
---------------------
Numero: 10   
10 não é Primo
----------------------
---------------------
Numero: 17   
17 é Primo
----------------------

7 - DAdos dois numeros que representeam um intervalo, exibir os numeros primos deste intervalo.
---------------------
Inicio: 2   
Fim: 20
primos: 2 3 5 7 11 17 19
----------------------
"""
