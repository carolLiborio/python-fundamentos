#tipos de variáveis
"""
ano = 1989
nome = "Luke Skywalker"
saldo = 50.30
print("O tipo da variável ano é {}".format(type(ano)))
print("O tipo da variável nome é {}".format(type(nome)))
print("O tipo da variável saldo é {}".format(type(saldo)))
"""

#if simples 
"""
rm = input("Insira seu RM: ")
idade = input("Insira sua idade: ")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno  RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
"""

#if composto
"""
rm = input("Insira seu RM: ")
idade = input("Insira sua idade: ")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else: print("Aluno RM {}, sua participação não foi permitida. Apenas maiores de 18 anos podem participar!".format(rm))
"""

#if encadeado 
"""
rm = input("Insira seu RM: ")
idade = input("Insira sua idade: ")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else:
    autorizado = input("Você possui autorização dos responsáveis? S-SIM ou N-NÃO")
    if autorizado.lower() == 's':
        print("Sua participação foi autorizada, aluno RM {}!".format(rm))
        print("Mais informações serão enviadas para o email dos responsáveis!")
    else:
        print("Aluno RM {}, você precisa de autorização dos responsáveis para participar! Sua participação não foi autorizada por enquanto.".format(rm))
"""

#elif
pontuacao = input("Insira a pontuação do cliente: ")
pontuacao = int(pontuacao)
if pontuacao >= 1000:
    print("O cliente tem direito a receber mais 3gb na sua franquia de internet!")
elif pontuacao >=500:
     print("O cliente tem direito a receber mais 1,5gb na sua franquia de internet!")
elif pontuacao >=200:
     print("O cliente tem direito a receber mais 500mb na sua franquia de internet!")
else:
     print("O cliente não receberá bônus.")