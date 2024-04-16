#Problema: Fazer um algoritmo que pegue dois valores do usuário e calcule a média
#Narrativa (os passos do algoritmo):

#Digitar o primeiro número (entrada de dados):
n1 = input("Digite o primeiro número: ")
n1 = float(n1)

#Digitar o segundo número (entrada de dados):
n2 = float(input("Digite o segundo número: "))

#Calcular a média dos dois números (processamento de dados):
med = (n1 + n2) / 2

#Exibir o resultado (saída de dados):
print(f"Resultado:", med)


#Casting() - Mudar o tipo da variável
"""
Inteiro - int()
Real    - float()
Texto   - str()
Lógico  - bool()

O input só captura dados string

valor = input("Digite um valor: ")
print(valor, type(valor))
valor = float(valor)
print(valor, type(valor))
"""

"""
? 10.5 % 1.2

1.2
1.2 2.4
1.2 3.6
1.2 4.8
1.2 6.0
1.2 7.2
1.2 8.4
1.2 9.6
1.2 10.8 -> excedeu o limite
"""
print(10.5 % 1.2)
