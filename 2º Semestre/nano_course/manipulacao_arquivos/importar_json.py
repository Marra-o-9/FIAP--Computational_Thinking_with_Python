import json

#dicionário do python = .json
with open("numeri.json", "r") as arquivo:
    dicionario = json.load(arquivo)
    for chave, valor in dicionario.items():
        print(f"{chave} : {valor}")