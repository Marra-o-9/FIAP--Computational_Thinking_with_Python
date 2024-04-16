"""
Operadores Aritméticos
PRIORIDADE  MATEMÁTICA  PYTHON  SIGNIFICADO
3           +           +       Adição         (com strings ele concatena)
3           -           -       Subtração
2           /           /       Divisão
2           x ou .      *       Multiplicação
1           EXP.        **      Exponenciação
2           ?           //      Divisão Inteira
2           ?           %       Módulo
"""

valor1 = 10
valor2 = 4
print("Valores:", valor1, "e", valor2)

conta = valor1 + valor2
print("Soma: ", conta)

conta = valor1 - valor2
print("Subtração: ", conta)

conta = valor1 / valor2
print("Divisão: ", conta)

conta = valor1 * valor2
print("Multiplicação: ", conta)

conta = valor1 ** valor2
print("Exponenciação: ", conta)

conta = valor1 // valor2
conta2 = valor1 / valor2
print("Divisão inteira ", conta, conta2)

valor1 = 10
valor2 = 3
conta = valor1 // valor2
conta2 = valor1 % valor2
print("Divisão inteira ", conta)
print("Módulo: ", conta2)
