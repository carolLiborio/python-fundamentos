'''
Crie um programa que receba do usuário os minutos atuais e exiba na tela
a senha necessária para desbloqueio.
A senha é composta da palavra “LIBERDADE” seguida do fatorial dos minutos
que a máquina estiver marcando no momento da digitação da senha (se a máquina
estiver marcando 5 minutos, a senha será LIBERDADE120).
ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial.
        Ele deve obrigatoriamente utilizar loop
'''

#entrada
fatoresFatorial= int(input("Insira os minutos que estão marcados na máquina neste momento: "))

#processamento
produtoFatorial = 1
contador = 1

while contador <= fatoresFatorial:
    produtoFatorial *= contador
    #igual a escrever fator = fator * outrofator
    contador += 1
    #igual a escrever fator = fator + outrofator

print()
print(f"A senha é LIBERDADE{produtoFatorial}")

""" Usar o f antes da string permite editar a variável na própria
string, não necessitando usar .format (a partir do Python 3.6).
"""





