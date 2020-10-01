#criando um dicionario vazio
dicionario = {}
#exibindo o tipo da estrutura
print("O objeto dicionario é do tipo {}".format(type(dicionario)))

#criando um dicionario com dados
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}

#exibindo o valor associado a uma chave específica
print(dicionario["Yoda"])


"""#exibindo todos os valores em um dicionario
for valor in dicionario.values():
    print(valor)"""

"""#exibindo todas as chaves em um dicionario
for chave in dicionario.keys():
    print(chave)"""

"""#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))"""


#criando um dicionario com dados
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
#removendo todos os itens do dicionário
dicionario.clear()
#exibindo o dicionário completo após a remoção
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))


