"""
PROBLEMA 1: Dada a quilometragem parcial de um carro e a quantidade de litros gastos para percorrer esta quilometragem,
faça um algoritmo que calcule quantos km/L o carro percorreu.
Entrada: 345.6 | 25.4   Saída: 13.6
Entrada: 556.1 | 59.7   Saída: 9.31
"""

km = float(input("Digite a quilometragem: "))
litros = float(input("Digite os litros gastos: "))

relacao = km / litros

print(f"O carro percorreu {relacao}km/L.")


"""
PROBLEMA 2: Dado o preço do maço de cigarros, a quantidade de maços consumidos por dia e o tempo em anos que a pessoa
fuma, calcule o quanto esta pessoa já gastou fumando.
Entrada: 10 | 1 | 3     Saída: 10950
Entrada: 11.5 | 2 | 5   Saída: 41975
"""

preco = float(input("Digite o preço do maço de cigarros: "))
macos = int(input("Digite quantos maços são consumidos por dia: "))
tempo = float(input("Digite o tempo em anos que a pessoa fuma: "))

custo_por_dia = preco * macos
tempo_em_dias = tempo * 365

print(f"Essa pessoa já gastou R${custo_por_dia * tempo_em_dias} fumando durante esse tempo.")


"""
PROBLEMA 3: Um caixa eletrônico dispensa cédulas de 50, 20 e 10 reais. Considerando que a quantia seja múltiplo de 10,
faça um algoritmo que exiba um relatório com quantas cédulas de cada cédula são necessárias para compor essa quantia.
Entrada: 130    Saída: 50=2 | 20=1 | 10=1
Entrada: 270    Saída: 50=5 | 20=1 | 10=0
"""

quantia = int(input("Digite a quantia desejada: "))

ced_50 = quantia // 50
sobra_50 = quantia % 50
ced_20 = sobra_50 // 20
sobra_20 = sobra_50 % 20
ced_10 = sobra_20 // 10

print(f"Essa quantia é composta por {ced_50} nota(s) de 50, {ced_20} nota(s) de 20, e {ced_10} nota(s) de 10.")
