import json
#módulo python que gera dados em formato json

#criando um dicionário 
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

#convertendo o dicionário para uma string o formato json
final = json.dumps(contatos, indent=4)

"""#exibindo a string convertida
print(final)"""

#GRAVANDO UM ARQUIVO JSON

#criando um arquivo
arquivo = open("C:\\Users\\carol\\Documents\\Documentos\\tiworkspace\\python-fundamentos\\manipulaçao-arquivos\\agenda.json", "w")

#escrevendo o JSON dentro do arquivo
arquivo.write(final)

#fechando o arquivo
arquivo.close()