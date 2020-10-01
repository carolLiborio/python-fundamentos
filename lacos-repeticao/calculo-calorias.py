#receber do usuário o número de calorias de cada alimento
#exibir ao final o total de calorias do dia (acumulador)

#entrada
quantidadeAlimentos = int(input("Quantos alimentos você consumiu hoje? "))
caloriasAlimento = float(input("Insira as calorias do alimento: "))

#processamento
alimento = 1
totalCalorias = 0
while alimento < quantidadeAlimentos:
    caloriasAlimento = float(input("Insira as calorias do alimento: "))
    totalCalorias = totalCalorias + caloriasAlimento
    alimento = alimento + 1
print(" Você consumiu {} alimentos hoje, que totalizaram {:.2f} calorias!".format(quantidadeAlimentos, totalCalorias))