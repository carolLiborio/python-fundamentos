"""
Usar o módulo sys (padrão do python) para verificar o 
tamanho de qualquer objeto, a partir do método getsizeof()
"""
#primeiro importamos o módulo sys
import sys
#depois criamos algumas variáveis de exemplo
nome = "Bruce Wayne"
idade = 30
peso = 92.3
#Vamos exibir em uma mensagem o nome da variável, o tipo (type) e o tamanho (getsizeof)
print("A variável nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("A variável idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("A variável peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))

#criando uma lista e uma tupla vazias, respectivamente
lista_vazia = []
tupla_vazia = ()
#printando o tipo e tamanho de cada estrutura
print("O objeto lista_vazia é do tipo {} e ocupa {} bytes na memória".format(type(lista_vazia), sys.getsizeof(lista_vazia)))
print("O objeto tupla_vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))

"""
A tupla ocupa menos espaço de memória RAM que a lista, porque tem menos funcionalidades e seus dados são imutáveis
"""