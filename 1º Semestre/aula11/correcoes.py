huguinho = zezinho = luizinho = nulo = 0

while True:
    voto = int(input(f"""
    1 - Huguinho: {huguinho} voto(s)
    2 - Zezinho: {zezinho} voto(s)
    3 - luizinho: {luizinho} voto(s)
    Digite os votos para, Huguinho[1], Zezinho[2], Luizinho[3], ou saia[0]: 
    """))
    match voto:
        case 0:
            break
        case 1:
            huguinho += 1
        case 2:
            zezinho += 1
        case 3:
            luizinho += 1
        case _:
            nulo += 1
            print("Voto nulo ou inválido!")

total = huguinho + zezinho + luizinho + nulo
hp = (huguinho / total) * 100
zp = (zezinho / total) * 100
lp = (luizinho / total) * 100
np = (nulo / total) * 100

print(f"""
1 - Huguinho: {huguinho} voto(s) - {hp}%
2 - Zezinho: {zezinho} voto(s) - {zp}%
3 - Luizinho: {luizinho} voto(s) - {lp}%

Nulos: {nulo} voto(s) - {np}%
""")
