#TRANSFORMANDO JSON EM DICIONÁRIO

import json
#Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\Users\\carol\\Documents\\Documentos\\tiworkspace\\python-fundamentos\\manipulaçao-arquivos\\agenda.json")

#colocando o conteúdo do arquivo em uma variável do tipo string
conteudo_do_arquivo = arquivo.read()

#fechando o arquivo
arquivo.close()

#convertendo uma string no formato json em um dicionário
agenda = json.loads(conteudo_do_arquivo)

#comprovando que o objeto agenda é do tipo dicionário
print("O tipo do objeto agenda é {}".format(type(agenda)))