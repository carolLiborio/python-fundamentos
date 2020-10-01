#USANDO A FUNÇÃO OPEN() PARA SALVAR ARQUIVOS

#Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?" + "\n"

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\Users\\carol\\Documents\\Documentos\\tiworkspace\\python-fundamentos\\manipulaçao-arquivos\\novo_arquivo.txt", "a")

#forma de arquivo "w" = criar um novo arquivo sobrescrevendo o conteúdo do anterior
#forma de arquivo "a" = anexa o conteúdo ao final do conteúdo já existente no arquivo (a = append)

#Escrevendo o conteúdo da variável conteudo dentro do arquivo
arquivo.write(conteudo)

#fechando o arquivo
arquivo.close()