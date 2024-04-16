print("Agora estou usando uma IDE")

#Tipos de variáveis
nome = "Marra"      #Texto é str() no Python
idade = 19          #Inteiro é int() no Python
altura = 1.85       #Real é float() no Python
maioridade = True   #Lógico é bool() no Python

print(nome, idade, altura, maioridade)


#Verificando o tipo das variáveis
valor = "45"
print(valor, type(valor))
valor = 45
print(valor, type(valor))
valor = 45.1
print(valor, type(valor))
valor = True
print(valor, type(valor))


#Soma de números em string e soma de números em int (resultados diferentes)
valor1 = "10"
valor2 = "20"
resposta = valor1 + valor2
print(resposta)

valor1 = 10
valor2 = 20
resposta = valor1 + valor2
print("Resultado:", resposta)


#Mudar o tipo da variável - Casting
valor1 = "10"
valor1 = int(valor1)
valor2 = "20"
valor2 = int(valor2)
resposta = valor1 + valor2
print("Resultado:", resposta)

valor1 = "10"
valor2 = "20"
resposta = int(valor1) + int(valor2)


#Várias maneiras de formatação - Format
print("Resultado:", resposta)
print("Resultado:", valor1, " + ", valor2, " = ", resposta)
#print("Resultado:" + valor1 + " + " + valor2 + " = " + resposta)                     #o + só soma strings
print("Resultado: {} + {} = {}".format(valor1, valor2, resposta))                     #coloca as variáveis nas chaves
print("Resultado: {1} + {0} = {2}".format(valor1, valor2, resposta))                  #índices respectivos de cada valor
print("Resultado: {v1} + {v2} = {r}".format(v1=valor1, v2=valor2, r=resposta))        #mudar nome do índice
print("Resultado: {v1} + {v2} = {r:.2f}".format(v1=valor1, v2=valor2, r=resposta))    # :.2f = casas decimais
print("Resultado: {v1} + {v2} = {r:10.3f}".format(v1=valor1, v2=valor2, r=resposta))  # :10 = bytes de espaço

a = 56.7
b = 3456.789
c = 2.0
print("R$ {:10.2f}".format(a))
print("R$ {:10.2f}".format(b))
print("R$ {:10.2f}".format(c))

a = 56.7
b = 3456.789
c = 2.0
print(f"Valor de a + {a} \nValor de b = {b} \nValor de c = {c}")        #\n = pula de linha
print(f"Valor de a + {a} \nValor de b = {b} \nValor de c = {c:10.2f}")
#f = possibilita colocar variáveis numéricas em strings

x = 23
print(f"Valor de x = {x}")
print(f"Valor de x = {x:6}")
print(f"Valor de x = {x:06}")  #colocar 0, preenche os espaços anteriores com zeros
