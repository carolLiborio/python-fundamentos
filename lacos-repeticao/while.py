"""
***** 1. laço de repetição simples*****
"""
"""
#criação da variável com um valor inicial
resposta = "0"
#enquanto a resposta não for 42, a repetição ocorre
while (resposta != "42"):
    #para cada uma das repetições, o usuário irá submeter uma resposta
    resposta = input("Qual a resposta para a vida, o universo e tudo mais?")
#quando o laço terminar, a mensagem é exibida
print("Parabéns, você acertou!")
"""


"""
***** 2. laço de repetição com variável contadora *****
"""
#criação da variável com um valor inicial
i = 0
#enquanto a variável contadora não chegar ao limite
while (i<=10):
    #para cada uma das repetições uma mensagem é exibida
    print("Mais uma mensagem, com i valendo: {}".format(i))
    i = i + 1


