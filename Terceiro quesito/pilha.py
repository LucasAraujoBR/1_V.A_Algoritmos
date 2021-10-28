# #-----------------------------Pilhas---------------------------------#

def empty(pilha): #verifica se pilha está vazia
    return len(pilha) == 0

def push(pilha,item): #adiciona itens na pilha
    pilha.append(item)

def pop(pilha): #remove itens da pilha
    if empty(pilha):
        print("ATENÇÃO PILHA VAZIA")
    else:
        item=pilha.pop()
        return item

def top(pilha): #retorna item do topo sem remove-lo
    if empty(pilha):
        print("ATENÇÃO PILHA VAZIA")
    else:
        return pilha[len(pilha)-1]

def size(pilha): #retorna tamanho da pilha
    return len(pilha)

#Buscar
def buscar(pilha,elemento):
    for x in range(size(pilha)):
        if(pilha[x] == elemento):
            return x
    return None

p=[] #iniciando pilha
s=[1,2,3] #Passo os dados para pilha

#inserindo elementos na pilha
for i in range(0,len(s),1):
    push(p,s[i])
print(f'total de elementos na pilha = {p}\n')
#buscando elementos da pilha
elemento = 2
indice_pesquisado = buscar(p,elemento)

if(indice_pesquisado == None):
    print(f'Indice do elemento {elemento} não está na pilha.')
else:
    print(f'Indice do elemento {elemento} eh {indice_pesquisado}.')
print(f'total de elementos na pilha = {p}\n')
#removendo elemento da pilha  
for i in range(0,len(s),1):
    print(f'removido:{pop(p)}', end="\n")
print(f'\ntotal de elementos na pilha = {p}')