""" 

**Parte teorica**

O algoritmo de dijkstra é um algoritmo que busca menores caminhos 
entre dois vértices desde que exista um caminho possível do vertice de origem.
é muito utilizado nos aplicativos de GPS para buscar o menor caminho entre dois pontos,
ele funciona com uma construção focada em cada escolha tendo o final mais benéfico possivel.

 """
import sys


class Graph():

    def __init__(self, vertx):
        self.V = vertx
        self.graph = [[0 for coluna in range(vertx)]
                      for linha in range(vertx)]

    def minDistancia(self, dist, ind_dis):

        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and ind_dis[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def nos(self, dist):
        print("Distancia")
        for indice in range(self.V):
            print(indice, "->", dist[indice])

    def dijkstra(self, source):

        dist = [sys.maxsize] * self.V
        dist[source] = 0
        ind_dis = [False] * self.V

        for x in range(self.V):

            u = self.minDistancia(dist, ind_dis)

            ind_dis[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0:
                    if ind_dis[v] == False:
                        if dist[v] > dist[u] + self.graph[u][v]:
                            dist[v] = dist[u] + self.graph[u][v]

        self.nos(dist)


# pesos são iguais ao numero do maior vertice do par e a origem o vértice 1
f = Graph(6)
f.graph = [[0, 2, 0, 0, 5, 0],
           [2, 0, 3, 0, 5, 0],
           [0, 3, 0, 4, 0, 0],
           [0, 0, 4, 0, 5, 6],
           [5, 5, 0, 5, 0, 0],
           [0, 0, 0, 6, 0, 0]]

f.dijkstra(0)
