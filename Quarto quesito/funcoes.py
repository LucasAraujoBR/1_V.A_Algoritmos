from classes import *


def insere_no_inicio(lista, novo_dado):
    # 1) Cria um novo nodo com o dado a ser armazenado.
    novo_nodo = NodoLista(novo_dado)

    # 2) Faz com que o novo nodo seja a cabeça da lista.
    novo_nodo.proximo = lista.cabeca

    # 3) Faz com que a cabeça da lista referencie o novo nodo.
    lista.cabeca = novo_nodo


def busca(lista, valor):
    corrente = lista.cabeca
    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
    return corrente


def remove(self, valor):
    assert self.cabeca, "Impossível remover valor de lista vazia."

    # Nodo a ser removido é a cabeça da lista.
    if self.cabeca.dado == valor:
        self.cabeca = self.cabeca.proximo
    else:
        # Encontra a posição do elemento a ser removido.
        anterior = None
        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        # O nodo corrente é o nodo a ser removido.
        if corrente:
            anterior.proximo = corrente.proximo
        else:
            # O nodo corrente é a cauda da lista.
            anterior.proximo = None


def imprime_lista(self):
    a = self.dado
    print(a)


def imprimeInicio(Self):

    if(Self == None):
        print("Lista está vazia")
    else:
        aux = Self.cabeca
        print(aux)


def imprima(node):
    if(node == None):
        return
    else:
        return '%s' '-> %s' % (imprima(node.proximo), node.dado)


def imprimeFim(node):
    if(node == None):
        print("Lista está vazia")
    else:
        aux = node.cabeca
        print(imprima(aux))
