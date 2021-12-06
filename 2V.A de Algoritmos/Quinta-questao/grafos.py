""" 

**Parte teorica**

Um grafo é uma rede de vértices que são conectados dois a dois por arestas ou arcos
podendo ser direcionado ou não direcionado, sendo o grafo direcionado aquele que leva
em consideração o sentido (ou direção) da aresta ou arco para a construção da relação de conexão entre
os vértices e o não direcionado une ambos os vértices com uma unica aresta sem direção.

 """
class graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.graph[u-1].append(v)

    def remove_aresta(self, u, v):
        self.graph[u-1].remove(v)

    def adiciona_ver(self, i):
        for u in range(i):
            self.vertices = self.vertices+1
            self.graph += [[]]

    def remove_ver(self, v):
        for i in range(self.vertices):
            if(v in self.graph[i-1]):
                self.graph[i-1].remove(v)

        self.vertices = self.vertices-1
        self.graph[v-1].pop(v-1)
        self.graph.pop(v-1)

    def mostra_gra(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.graph[i]:
                print(f'-> {j}', end='  ')
            print('')


g = graph(4)

g.adiciona_aresta(1, 2)
g.adiciona_aresta(1, 4)
g.adiciona_aresta(2, 4)
g.adiciona_aresta(2, 3)
g.adiciona_aresta(4, 1)
g.mostra_gra()

print('')

g.remove_aresta(1, 2)
g.adiciona_ver(1)
g.adiciona_aresta(2, 5)
g.adiciona_aresta(5, 3)
g.adiciona_aresta(2, 1)
g.adiciona_aresta(3, 1)

g.mostra_gra()
print('')


g.remove_ver(1)
g.mostra_gra()
