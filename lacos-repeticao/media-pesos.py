#variavel para armazenar o peso total das caixas
peso_total = 0.0
#loop para repetir por 10 vezes a solicitação de peso
for x in range(1,11):
    #para cada volta do loop, solicitar o peso da caixa
    peso_atual = float(input("Informe o peso da caixa atual:"))
    #para cada peso solicitado, somar ao peso total
    peso_total = peso_total + peso_atual
#ao final do loop, calcular a média aritmética
media = peso_total/10
#exibição dos resultados
print("As caixas tem o peso total de {}kg. A média de peso é {}kg".format(peso_total, media))