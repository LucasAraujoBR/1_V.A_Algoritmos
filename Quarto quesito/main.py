from funcoes import *


# a)Inserção de um dado elemento no início da lista
lista = ListaEncadeada()
print("Lista vazia:", lista)

insere_no_inicio(lista, 5)
print("Lista contém um único elemento:", lista)

insere_no_inicio(lista, 10)
print("Inserindo um novo elemento:", lista)

insere_no_inicio(lista, 15)
print("Inserindo um novo elemento:", lista)

insere_no_inicio(lista, 20)
print("Inserindo um novo elemento:", lista)

insere_no_inicio(lista, 25)
print("Inserindo um novo elemento:", lista)
# B)Remoção de um dado valor da lista

listando = ListaEncadeada()
for i in range(5):
    insere_no_inicio(listando, i)
print("Lista:", listando)

print("Removendo elementos:")
for i in range(5):
    remove(listando, i)
    print("Removendo o elemento {0}: {1}".format(i, listando))

# c)Busca por um dado elemento da lista
lista_encadeada = ListaEncadeada()
for i in range(8):
    insere_no_inicio(lista_encadeada, i)
print("Lista:", lista_encadeada)

for i in range(8, -4, -2):
    elemento = busca(lista_encadeada, i)
    if elemento:
        print("Elemento {0} presente na lista!".format(i))
    else:
        print("Elemento {0} não encontrado.".format(i))


# d)Impressão da lista do início para o fim

print("-------------------------------------")
lista1 = ListaEncadeada()
insere_no_inicio(lista1, 4)
insere_no_inicio(lista1, 5)
insere_no_inicio(lista1, 10)
insere_no_inicio(lista1, 8)
insere_no_inicio(lista1, 6)
imprimeInicio(lista1)


# E)Impressão da lista do fim para o início
print("-------------------------------------")
imprimeFim(lista1)
