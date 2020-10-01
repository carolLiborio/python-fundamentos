"""
Dicionários Aninhados (Nested Dictionaries): são dicionários em que as chaves tem como
valor outros dicionários. 
"""

#criando o dicionário dos contatos
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

#esse for passará por todos os items do dicionário contatos, com a variável "contato" contendo as chaves desses items e o objeto formas contendo os valores, que são os dicionários de formas de contatos
for contato, formas in contatos.items():
    #para cada item encontrado no dicionário anterior, que estão contidos no dicionário "formas", vamos recuperar as chaves "celular" e "email" e seus valores
    for celular, email in formas.items():
        #exibimos aqui o nome do contato e as suas formas de contato
        print("O contato {} pode ser encontrado no {} {}".format(contato, celular, email))