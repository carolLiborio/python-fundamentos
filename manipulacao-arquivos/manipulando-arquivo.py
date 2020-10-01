#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\Users\\carol\\Documents\\Documentos\\tiworkspace\\python-fundamentos\\manipulaçao-arquivos\\arquivo_texto.txt")

#verificando o tipo do objeto arquivo
print(type(arquivo))

#lendo o conteúdo do objeto arquivo
#print(arquivo)
print(arquivo.readline())

#Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)


#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\Users\\carol\\Documents\\Documentos\\tiworkspace\\python-fundamentos\\manipulaçao-arquivos\\arquivo_texto.txt")

#Passando o conteúdo do arquivo para uma lista
linhas_do_arquivo = arquivo.readlines()

#comprovando o tipo do objeto linhas_do_arquivo
print("Ei! Eu consegui transformar meu arquivo em uma {} ".format(type(linhas_do_arquivo)))

#colocando a lista em ordem alfabética
linhas_do_arquivo.sort()

#Exibindo nossa lista, agora em ordem alfabética
print(linhas_do_arquivo)

arquivo.close()