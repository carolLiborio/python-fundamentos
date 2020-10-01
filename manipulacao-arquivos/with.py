#o with usará o open para abrir o arquivo indicado, dentro do objeto arquivo, e encerrará automaticamente o arquivo assim que sua última instrução for executada
with open("C:\\Users\\carol\\Documents\\Documentos\\tiworkspace\\python-fundamentos\\manipulaçao-arquivos\\arquivo_texto.txt", "r") as arquivo:
    #aqui devemos escrever todos os códigos que usam o arquivo aberto, pois após a última linha de código dentro dessa estrutura, o arquivo será automaticamente encerrado
    print(arquivo.read())

#escrevendo novo conteúdo no arquivo
with open("C:\\Users\\carol\\Documents\\Documentos\\tiworkspace\\python-fundamentos\\manipulaçao-arquivos\\arquivo_texto.txt", "w") as arquivo:
    arquivo.write("May the force be with you")

#verificar o conteúdo do arquivo 
with open("C:\\Users\\carol\\Documents\\Documentos\\tiworkspace\\python-fundamentos\\manipulaçao-arquivos\\arquivo_texto.txt", "r") as arquivo:
    print(arquivo.read())