#seleçao do melhor dia da semana para realizar lives

#captar votos por dia da semana
print("Votação para o melhor dia para a realização de lives!")
segunda = int(input("Insira os votos a favor de 2ª feira: "))
terca = int(input("Insira os votos a favor de 3ª feira: "))
quarta = int(input("Insira os votos a favor de 4ª feira: "))
quinta = int(input("Insira os votos a favor de 5ª feira: "))
sexta = int(input("Insira os votos a favor de 6ª feira: "))

#declarar uma variavel "contador"
maisVotado = " "

"""fazer comparação dos valores, sendo que para uma variavel ser a maior,
ela tem que ser maior que todas as demais ao mesmo tempo """
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O melhor dia para as lives é segunda-feira!")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O melhor dia para as lives é terça-feira!")
elif quarta > segunda and quarta > terca and quarta > quinta and quinta > sexta:
    print("O melhor dia para as lives é quarta-feira!")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("O melhor dia para as lives é quinta-feira!")
else:
    print("O melhor dia para as lives é sexta-feira!")



