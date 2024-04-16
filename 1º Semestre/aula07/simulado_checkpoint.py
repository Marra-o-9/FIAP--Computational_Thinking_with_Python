"""
FAZER UM PROGRAMA QUE CALCULE O PROCESSO AVALIATIVO RELACIONADO A NOTAS DE UM ALUNO DA FIAP.

PRIMEIRO SEMESTRE (SEM1)
-----------------------
CHECKPOINT: Pegar 3 notas do usuário e excluir a menor para fazer a media simples
por dois.
CP1 * 1 = 10 - 5
CP2 * 1 = 10 - 9
CP3          - 7
mediaCPs = (9 + 7) / 2 -> 8

Os CPs tem peso de 20% na média.

SPRINT (CHALLENGE): Pegar duas notas do usuário e Calcular a média simples por 2.
SP1 * 1 -> 9
SP2 * 1 -> 5
mediaSPs = (9 + 5) / 2 -> 7

Os SPs tem peso de 20% na média.

GLOBAL SOLUTION: Pegar a nota do usuário. Tem peso de 60%.
GS * 6 -> 10

MEDIA SEMESTRAL (SEM1) = CPs * 0.2 + SPs * 2 + GS * 6
                          8  * 0.2 + 7 * 0.2 + 10 * 0.6
                          1.6      + 1.4     + 6
                          9.0

SEGUNDO SEMESTRE (SEM1)
-----------------------
CHECKPOINT: Pegar 3 notas do usuário e excluir a menor para fazer a media simples
por dois.
CP1 * 1 = 10
CP2 * 1 = 10
CP3 X
Os CPs tem peso de 20% na média.

SPRINT (CHALLENGE): Pegar duas notas do usuário e Calcular a média simples por 2.
SP3 * 1 = 10
SP4 * 1 = 10
Os SPs tem peso de 20% na média.

GLOBAL SOLUTION: Pegar a nota do usuário. Tem peso de 60%.
GS * 6 = 10

MEDIA SEMESTRAL (SEM2) = CPs * 2 + SPs * 2 + GS * 6


----------------------------------
MEDIA FINAL = SEM1 * 0.4 + SEM2 * 0.6
               9 * 0.4   + 6 * 0.6
               3.6       +  3.6
               5.2

APROVADO? de 6 para cima
EXAME? Quem tirou entre 4 e 5.9
    Pedir a nota de exame e verificar se ele foi aprovado ou nao
    Exame: 7
    Calculo (5.2 + 7) / 2
             13.2 / 2
             6.6
             Aprovado em exame

REPROVADO? Quem tirou abaixo de 4

"""

#Primeiro semestre
cp1 = float(input("SEM1 - Digite a nota do primeiro checkpoint: "))
cp2 = float(input("SEM1 - Digite a nota do segundo checkpoint: "))
cp3 = float(input("SEM1 - Digite a nota do terceiro checkpoint: "))

if cp1 <= cp2 and cp1 <= cp3:
    mediacp = (cp2 + cp3) / 2
elif cp2 <= cp1 and cp2 <= cp3:
    mediacp = (cp1 + cp3) / 2
else:
    mediacp = (cp1 + cp2) / 2

sp1 = float(input("SEM1 - Digite a nota do primeiro sprint: "))
sp2 = float(input("SEM1 - Digite a nota do segundo sprint: "))

mediasp = (sp1 + sp2) / 2

gs = float(input("SEM1 - Digite a nota da global solutions: "))

sem1 = (mediacp * 0.2) + (mediasp * 0.2) + (gs * 0.6)

#Segundo semestre
cp1 = float(input("SEM2 - Digite a nota do primeiro checkpoint: "))
cp2 = float(input("SEM2 - Digite a nota do segundo checkpoint: "))
cp3 = float(input("SEM2 - Digite a nota do terceiro checkpoint: "))

if cp1 <= cp2 and cp1 <= cp3:
    mediacp = (cp2 + cp3) / 2
elif cp2 <= cp1 and cp2 <= cp3:
    mediacp = (cp1 + cp3) / 2
else:
    mediacp = (cp1 + cp2) / 2

sp1 = float(input("SEM2 - Digite a nota do primeiro sprint: "))
sp2 = float(input("SEM2 - Digite a nota do segundo sprint: "))

mediasp = (sp1 + sp2) / 2

gs = float(input("SEM2 - Digite a nota da global solutions: "))

sem2 = (mediacp * 0.2) + (mediasp * 0.2) + (gs * 0.6)

#Media final e exame
mediasem = (sem1 * 0.4) + (sem2 * 0.6)

if mediasem >= 6:
    print(f"Você está aprovado com a média final: {mediasem}.")
elif mediasem < 4:
    print(f"Você está reprovado com a média final: {mediasem}.")
else:
    exame = float(input("Digite a nota do exame: "))
    mediaexame = (exame + mediasem) / 2
    if mediaexame >= 6:
        print(f"Você foi aprovado no exame com média final: {mediaexame}.")
    else:
        print(f"Você foi reprovado no exame com média final: {mediaexame}.")
