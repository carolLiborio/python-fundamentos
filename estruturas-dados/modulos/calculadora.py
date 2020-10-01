#importação do módulo operacoes.py
import operacoes

"""OBS: o uso do módulo deverá ser feito obedecendo à estrutura
    nomedomodulo.nomedafuncao """

#solicitar valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite um valor: ")

#armazenando operação
soma = operacoes.somar(valor1,valor2)
subtracao = operacoes.subtrair(valor1,valor2)
multiplicacao = operacoes.multiplicar(valor1,valor2)
divisao = operacoes.dividir(valor1,valor2)

#exibir a operação
print(f"A soma é {soma}")
print(f"A subtracao é {subtracao}")
print(f"A multiplicao é {multiplicacao}")
print(f"A divisao é {divisao}")
