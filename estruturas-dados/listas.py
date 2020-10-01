#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
print(jedi)
#exibindo a lista com um print
#print(jedi)

#exibindo um valor específico da lista
#print(jedi[1])

""" para exibir uma lista completa, porém um valor de cada vez"""
"""for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)"""

#incluindo um valor no final da lista
"""jedi.append("Mace Windu")
for nome in jedi:
    print(nome)"""

#incluindo um valor digitado no final da lista
"""jedi.append(input("Digite o nome de um jedi"))
for nome in jedi:
    print(nome)"""

#incluindo um valor em uma posição específica da lista
"""jedi.insert(2, "Luminara")
for nome in jedi:
    print(nome)"""

#incluindo um valor pelo usuário em uma posição específica da lista
"""jedi.insert(2, input("Digite o nome de um Jedi"))
for nome in jedi:
    print(nome)"""

#Removendo o último valor inserido na lista
"""jedi.pop()
for nome in jedi:
    print(nome)"""

#Removendo o valor de uma posição específica
"""jedi.pop(1)
for nome in jedi:
    print(nome)"""

#Removendo um valor específico da lista
jedi.remove("Yoda")
for nome in jedi:
    print(nome)


    