# Explique as diferenças existentes entre Listas, Filas e Pilhas. Que tipo de aplicação computacional
# você vê para cada uma delas? Implemente cada uma das estruturas de dados e suas operações
# (inserir, remover e buscar) dinamicamente.


###############Listas#######################
lista = [1,2,3]
print(lista)
#Inserir
lista.append('Inserindo valor no final da lista')  #Dentro de append escrevemos o que vamos inserir na lista.
lista.insert(0,'inserindo no começo da lista') #Com o insert podemos escolher onde inserir o valor na lista.
print(lista)

#Remover
del(lista[0])   #Com a função del podemos, por meio do indice da lista, remover o valor da mesma.
del(lista[3])   #Com a função del podemos, por meio do indice da lista, remover o valor da mesma.
print(lista)

#Buscar
def busca(lista,elemento):
    for x in range(len(lista)):
        if(lista[x] == elemento):
            return x
    return None

lista_de_busca = [1,'araujo',3,4,5,'Lucas','python']
elemento = 'python'
indice_pesquisado = busca(lista_de_busca,elemento)
if(indice_pesquisado == None):
    print(f'Indice do elemento {elemento} não está na lista.')
else:
    print(f'Indice do elemento {elemento} eh {indice_pesquisado}.')

#A lógica usada para função Buscar pode ser reutilizada com append, para inserir um valor na lista e também para del, afim de deletar um valor da lista.



