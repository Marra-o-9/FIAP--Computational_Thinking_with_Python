"""
PROBLEMA 1: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
"""

nota = float(input("Digite uma nota entre zero e dez: "))

while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Digite uma nota válida: "))

print("Nota válida. Obrigado!")


"""
PROBLEMA 2: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

user = input("Digite o usuário: ")
key = input("Digite a senha: ")

while user == key:
    print("Erro! Usuário e senha não podem ser iguais!")
    user = input("Digite o usuário: ")
    key = input("Digite a senha: ")

print(f"""
Usuário....:   {user}
Senha......:   {key}
""")


"""
PROBLEMA 3: Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Digite um nome: ")
while len(nome) <= 3:
    print("\nNome muito curto!")
    nome = input("Digite um nome com, no mínimo, 3 caracteres: ")

idade = int(input("Digite a idade: "))
while idade < 0 or idade > 150:
    print("\nIdade inválida!")
    idade = int(input("Digite uma idade válida: "))

sal = float(input("Digite um salário: "))
while sal < 0:
    print("\nSalário inválido!")
    sal = float(input("Digite um salário positivo: "))

sexo = input("Digite o sexo [M]asculino ou [F]eminino: ").upper()
while sexo != "M" and sexo != "F":
    print("\nSexo inválido!")
    sexo = input("Digite o sexo [M]asculino ou [F]eminino: ").upper()

ec = input("Digite o estado civil [C]asado, [S]olteiro, [V]iúvo ou [D]ivorciado: ").upper()
while ec != "C" and ec != "S" and ec != "V" and ec != "D":
    print("\nEstado civil inválido")
    ec = input("Digite o estado civil [C]asado, [S]olteiro, [V]iúvo ou [D]ivorciado: ").upper()

if ec == "C":
    ec = "Casado"
elif ec == "S":
    ec = "Solteiro"
elif ec == "V":
    ec = "Viúvo"
else:
    ec = "Divorciado"

print(f"""
Nome: {nome}
Idade: {idade}
Salário: R${sal:.2f}
Sexo: {sexo}
Estado Civil: {ec}
""")


"""
PROBLEMA 4: Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
"""

popA = 80000
popB = 200000
tempo = 0

while popA < popB:
    popA += (popA * 3 / 100)
    popB += (popB * 1.5 / 100)
    tempo += 1
    print(f"{popA:.0f} pessoas e {popB:.0f} pessoas, em {tempo} anos.")

print(f"\nDurou {tempo} anos para a população A atingir a população B.")


"""
PROBLEMA 5: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

popA = int(input("Digite a população do primeiro país: "))
taxaA = float(input("Digite a taxa de crescimento do primeiro país: "))
popB = int(input("Digite a população do segundo país: "))
taxaB = float(input("Digite a taxa de crescimento do segundo país: "))
tempo = 0

while popA < popB:
    popA += (popA * taxaA / 100)
    popB += (popB * taxaB / 100)
    tempo += 1
    print(f"{popA:.0f} pessoas e {popB:.0f} pessoas, em {tempo} anos.")

print(f"\nDurou {tempo} anos para a população A atingir a população B.")
