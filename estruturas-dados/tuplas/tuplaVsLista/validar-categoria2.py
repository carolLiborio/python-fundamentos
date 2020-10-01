#********COMPARANDO TUPLAS E LISTAS **********
#importando o módulo que lida com as habilitacoes
import habilitacoes2
#pedindo que o usuário a categoria
categoria_digitada = input("Digite a categoria de habilitação")
"""#incluindo uma nova categoria falsa em tempo de execução 
habilitacoes2.categorias.append("ESPECIAL")"""
#utilizando o método validar_categoria para verificar se o que foi digitado é válido
habilitacoes2.validar_categoria(categoria_digitada)

""" a tupla não permite a inserção de dados no módulo"""