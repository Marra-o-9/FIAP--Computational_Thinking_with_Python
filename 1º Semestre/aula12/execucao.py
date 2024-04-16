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