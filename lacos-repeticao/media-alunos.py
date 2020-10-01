#obter a nota de 50 alunos, dividos entre pares e impares
#obter a media de cada uma das partes, e exibir qual foi a maior

somaAlunosPares = 0.0
notaPares = 0.0
for x in range(2,50,2):
    print("Você está digitando a nota dos alunos pares.")
    notaPares=  float(input("Por favor, insira a nota do(a) aluno(a) {} ".format(x)))
    somaAlunosPares = somaAlunosPares + notaPares

quantidadeAlunos = 50 / 2
mediaAlunosPares = somaAlunosPares / quantidadeAlunos
print()
print("A media da nota dos alunos pares é {} ".format(mediaAlunosPares))


somaAlunosImpares = 0.0
notaImpares = 0.0
for x in range(1,50,2):
    print("Você está digitando a nota dos alunos ímpares.")
    notaImpares=  float(input("Por favor, insira a nota do(a) aluno(a) {} ".format(x)))
    somaAlunosImpares = somaAlunosImpares + notaImpares

quantidadeAlunos = 50 / 2
mediaAlunosImpares = somaAlunosImpares / quantidadeAlunos
print()
print("A media da nota dos alunos ímpares é {} ".format(mediaAlunosImpares))
print()

if mediaAlunosPares > mediaAlunosImpares:
    print("A maior média é {:.2f}, que corresponde a média dos alunos pares.".format(mediaAlunosPares))
elif mediaAlunosPares == mediaAlunosImpares:
    print("A media dos alunos pares é igual a média dos alunos ímpares.")
elif mediaAlunosPares < mediaAlunosImpares:
    print("A maior média é {:.2f}, que corresponde a média dos alunos ímpares.".format(mediaAlunosImpares))
