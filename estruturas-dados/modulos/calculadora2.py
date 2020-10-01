#importação de funções específica do módulo operacoes.py
from operacoes import somar, subtrair
"""Dessa maneira, pode-se chamar a operação sem usar o nome do módulo e
o sinal de ponto """
#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = somar(valor1, valor2)
#exibindo a soma
print("A soma é {}".format(soma))


"""
Importando todas as funções de uma só vez. 
Deve ser usado com cautela, para não deixar o programa lento.

#importação de funções específicas do módulo operacoes.py
from operacoes import *
"""
