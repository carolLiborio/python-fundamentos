"""#Função que calcula a velocidade média
def calcularVelocidadeMedia():
    #solicitar distância e tempo
    distancia = float(input("Digite a distância percorrida, em km"))
    tempo = float(input("Digite o tempo da viagem, em hrs"))
    
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    
    #exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))
    
#chamada da função 
calcularVelocidadeMedia()"""

""" Não é uma boa prática colocar inputs dentro de uma função,
porque limitamos a inserção de valores a partir da digitação do usuário.
Correto é chamar os inputs fora da função, e passar para ela por meio de argumentos
ou parâmetros"""

#REFATORANDO A FUNÇÃO

"""#Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))

#solicitar inserção de valores para o usuário
dist = float(input("Informe a distância"))
temp = float(input("Informe o tempo"))

""" Há duas possibilidades de se chamar a função passando parâmetros.
    Sâo elas: """
#1. chamando a função com valores definidos pelo usuário
calcularVelocidadeMedia(dist, temp)

#2. chamando a função com valores definidos pelo programador
calcularVelocidadeMedia(15,2)"""


"""******** USANDO RETURN NA FUNÇÃO *******
    O comando return faz com que uma função seja encerra e retorne um determinado
    valor para o local onde ocorreu a chamada da função.
    Necessário para quando o objetivo da função é retornar alguma informação que será
    utilizada por outra função ou estrutura. 
"""
#Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    return velocidade_media
#solicitar informações dos usuários
dist = float(input("Informe a distância"))
temp = float(input("Informe o tempo"))
#chamando a função com valores definidos pelo usuário
print("A velocidade media é {}".format(calcularVelocidadeMedia(dist, temp))