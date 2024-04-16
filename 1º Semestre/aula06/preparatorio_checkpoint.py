"""
PROBLEMA 1: Dadas duas notas, calcular a média das duas notas e verificar se o aluno foi aprovado
"""

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1 + n2) / 2

if media >= 6:
    print(f"Aprovado com média {media}.")
else:
    print(f"Reprovado com média {media}.")

"""
V2.0: Considere o enunciado da versão anterior. Contudo, consistir os dados para que a média não seja
calculada de forma errada.

Nota 1: 4   Nota 2: 5       Saída: Reprovado com média 4.5
Nota 1: 7   Nota 2: 15      SAÍDA: A segunda nota é inválida
Nota 1: -3                  SAÍDA: A primeira nota é inválida
"""

n1 = float(input("Digite a primeira nota: "))

if n1 < 0 or n1 > 10:
    print("Primeira nota inválida!")
else:
    n2 = float(input("Digite a segunda nota: "))
    if n2 < 0 or n2 > 10:
        print("Segunda nota inválida!")
    else:
        media = (n1 + n2) / 2
        if media >= 6:
            print(f"Aprovado com média {media}.")
        else:
            print(f"Reprovado com média {media}.")

"""
V3.0: Considere o enunciado da versão anterior.
Caso o aluno tenha um média entre 4 e 5.9, permitir que ele faça exame.
Para o exame, consistir a nota também
Considerando a média anterior e a nota do exame, calcular uma nova média final.
Se ela for abaixo de 6, exibir "Reprovado em exame", senão "Aprovado em exame".
Em ambos os casos, exibir a média final.Contudo, consistir os dados para que a média não seja
calculada de forma errada.

Nota 1: 4   Nota 2: 5   Exame       nota de exame: 4.5   "Reprovado em exame com média 4.5"
Nota 1: 7   Nota 2: 15      SAÍDA: A segunda nota é inválida
Nota 1: -3                  SAÍDA: A primeira nota é inválida
"""

n1 = float(input("Digite a primeira nota: "))

if n1 < 0 or n1 > 10:
    print("Primeira nota inválida!")
else:
    n2 = float(input("Digite a segunda nota: "))
    if n2 < 0 or n2 > 10:
        print("Segunda nota inválida!")
    else:
        media = (n1 + n2) / 2
        if media >= 6:
            print(f"Aprovado com média {media}.")
        elif 4 <= media <= 5.9:
            exame = float(input("Digite a nota do exame: "))
            if exame < 0 or exame > 10:
                print("Nota do exame inválida!")
            else:
                media_exame = (media + exame) / 2
                if media_exame >= 6:
                    print(f"Aprovado no exame com média {media_exame}.")
                else:
                    print(f"Reprovado no exame com média {media_exame}.")
        else:
            print(f"Reprovado com média {media}.")


