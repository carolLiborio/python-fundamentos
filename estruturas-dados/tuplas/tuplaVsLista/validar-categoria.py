#********COMPARANDO TUPLAS E LISTAS **********
#importando o módulo que lida com as habilitacoes
import habilitacoes
#pedindo que o usuário a categoria
categoria_digitada = input("Digite a categoria de habilitação")
#incluindo uma nova categoria falsa em tempo de execução 
habilitacoes.categorias.append("ESPECIAL")
#utilizando o método validar_categoria para verificar se o que foi digitado é válido
habilitacoes.validar_categoria(categoria_digitada)

""" lista permite a inserção de dados no tempo de execução, 
o que pode prejudicar gravemente um sistema"""