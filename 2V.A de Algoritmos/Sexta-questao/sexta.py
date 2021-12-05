class graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.graph[u-1].append(v)
        self.graph[v-1].append(u)

    def remove_aresta(self, u, v):
        self.graph[u-1].remove(v)

    def adiciona_ver(self, i):
        for u in range(i):
            self.vertices = self.vertices+1
            self.graph += [[]]

    def remove_ver(self, v):
        for i in range(self.vertices):
            if v in self.graph[i-1]:
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


def busca(graph, vertice):
    visitados = set()

    def busca_rec(graph, vertice):
        visitados.add(vertice)
        for vizinho in graph.graph[vertice-1]:

            print(vizinho)
            if vizinho not in visitados:
                busca_rec(graph, vizinho)

    busca_rec(graph, vertice)


g = graph(6)

g.adiciona_aresta(1, 5)
g.adiciona_aresta(1, 2)
g.adiciona_aresta(2, 5)
g.adiciona_aresta(2, 3)
g.adiciona_aresta(5, 4)
g.adiciona_aresta(3, 4)
g.adiciona_aresta(4, 6)

g.mostra_gra()

print('')


busca(g, 6)
