#calculo de bonus sobre faturamento

assinatura = input("Insira o nível da sua assinatura (basic, silver, gold ou platinum): ")
faturamento = float(input("Insira seu faturamento anual (R$): "))

"""
determinar o valor de bonus a ser pago de acordo com
o nivel de assinatura e faturamento
"""

if assinatura.lower() == "basic":
    bonus = faturamento * 0.30
    print("O valor de bônus a pagar é {:.2f}".format(bonus))
elif assinatura.lower() == "silver":
    bonus = faturamento * 0.20
    print("O valor de bônus a pagar é {:.2f}".format(bonus))
elif assinatura.lower() == "gold":
    bonus = faturamento * 0.10
    print("O valor de bônus a pagar é {:.2f}".format(bonus))
else:
    bonus = faturamento * 0.05
    print("O valor de bonus a pagar é {:.2f}".format(bonus))