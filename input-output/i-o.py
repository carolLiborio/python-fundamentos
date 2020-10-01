"""
#Exibir nome e sobrenome
print("Esse programa exibirá seu nome completo. ")
nome = input("Digite seu primeiro nome, por favor: ")
sobrenome = input("Digite seu sobrenome, por favor: ")
nome_completo = nome + " " + sobrenome
print(nome_completo) 
"""

"""
# Realizar soma de dois valores
valor1 = input("Por favor, digite o primeiro valor: ")
valor2 = input("Por favor, digite o segundo valor: ")
soma = float(valor1) + float(valor2)
print("A soma entre os valores é {}".format(soma))
"""

"""
# Calcular a velocidade média de um veículo 
print("Esse programa calcula a velocidade média de um patinete")
distancia = input("Qual foi a distância em metros percorrida pelo patinete? ")
tempo = input("Quantos minutos o patinete demorou para percorrer essa distância? ")
velocidade_media = float(distancia) / float(tempo)
print("O patinete atingiu uma velocidade de {0:.2f} m/min".format(velocidade_media))
"""

# Inverter o conteúdo de duas variáveis 
print("Esse programa inverte os conteúdos de duas variáveis")
A = input("Digite o conteúdo da variável 1: ")
B = input("Digite o conteúdo da variável 2: ")
troca = A
A = B
B = troca
print("Agora que trocamos, a variável A contém {} e a variável B contém {}".format(A, B))

