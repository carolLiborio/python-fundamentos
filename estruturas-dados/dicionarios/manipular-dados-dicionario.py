#criando um dicionario vazio
dicionario = {}

#incluindo dados no dicionario
dicionario["Carolina Libório"] = "Aluno"
dicionario["Evelyn Cid"] = "Coordenadora"
dicionario["André David"] = "Professor"
#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))

"""#Pedindo para o usuário incluir dados no dicionário
nova_chave = input("Informe o nome do(a) integrante da FIAP")
novo_valor = input("Informe a função do(a) integrante da FIAP")
dicionario[nova_chave] = novo_valor"""
"""#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))"""

"""#alterando dados no dicionário
dicionario["A"] = "Coordenador"
#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O colaborador {} desempenha andré David função de {}".format(chave, valor))"""

"""#removendo item com chave específica 
dicionario.pop("André David")
#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))"""

"""#removendo último item 
dicionario.popitem()
#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))"""


#removendo todos os itens do dicionário
dicionario.clear()
#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))



