equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos)):  #len = até onde a variável vai
    print(f"""\n
    Equipamento..: {indice + 1}
    Nome.........: {equipamentos[indice]}
    Valor........: {valores[indice]}
    Serial.......: {seriais[indice]}
    Departamento.: {departamentos[indice]}
    """)
