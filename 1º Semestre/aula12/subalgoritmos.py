#Ambiente de declaração dos subalgoritmos
#Procedimento: Executa um bloco e não retorna valor


def saudacao() -> None:
    print("Bom dia, turma!")


def saudacao_nome(nome: str) -> None:    #o que está entre parênteses é chamado de parâmetro
    print(f"Bom dia, {nome}!")


def saudacao_hora(nome: str, hora: int) -> None:    #declarando as assinaturas das variáveis(não tem diferença prática)
    if hora < 12:
        print(f"Bom dia, {nome}!")
    elif hora < 18:
        print(f"Boa tarde, {nome}!")
    else:
        print(f"Boa noite, {nome}!")


#Função: Executa um bloco e retorna valor


def raiz_quadrada(numero: float) -> float:
#   raiz = numero ** (1 / 2)
#   print(raiz)
    return numero ** (1 / 2)       #retornando o valor para a função


#Programa principal

saudacao()                      #executou a função da área dos subalgoritmos
saudacao_nome("Marra")          #um parâmetro
saudacao_hora("Marra", 14)      #mais de um parâmetro
resposta = raiz_quadrada(25)    #isso é igual a: resposta = 5
print(resposta)                 #não consigo exibir a função sem printar, diferentemente do procedimento
print(raiz_quadrada(100))