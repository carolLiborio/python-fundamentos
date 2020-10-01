"""arquivo = open("primeiro-arquivo.txt","w")
arquivo.write("Hello World! Esse é meu primeiro arquivo em Python! Ai que tudo!")
arquivo.close()"""

""" Abrir arquivos com with: 
    Coloca-se um alias (apelido) ao inves de declarar a variável open; 
    Não necessita usar o .close(), ele fecha o arquivo automaticamente
 """
with open("primeiro-arquivo.txt","a") as arquivo:
    arquivo.write("\n Isso é viver, é aprender... Hakuna Matata!")
