import json

dicionario = {
    "Perspectivas": ["lancada"],
    "Eles me Ouvirao": ["gravada"],
    "Tempo que me Resta": ["gravada"],
    "Cansei de Esperar": ["estudio"]
}

with open("musicas_numeri.json", "w") as arquivo:
    json.dump(dicionario, arquivo)