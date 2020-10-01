#calculo de IMC

#solicitar peso e altura do usuario
peso = float(input("Insira seu peso, em kg: "))
altura = float(input("Insira sua altura, em metros: "))

#calcular imc
imc = peso / (altura * altura)
print("Seu IMC é {:.2f}".format(imc))

#informar o nível do imc, de acordo com tabela
if imc < 16.00:
    print("Você está com Baixo Peso Grau III.")
elif imc >= 16.00 and imc <= 16.99:
    print("Você está com Baixo Peso Grau II.")
elif imc >= 17.00 and imc <= 18.49:
    print("Você está com Baixo Peso Grau I.")
elif imc >= 18.50 and imc <= 24.99:
    print("Você está com Peso Ideal.")
elif imc >= 25.00 and imc <= 29.99:
    print("Você está com Sobrepeso.")
elif imc >= 30.00 and imc <= 34.99:
    print("Você está com Obesidade Grau I.")
elif imc >= 35.00 and imc <= 39.99:
    print("Você está com Obesidade Grau II.")
else:
    print("Você está com Obesidade Grau III.")






