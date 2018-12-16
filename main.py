from collections import defaultdict

custo_arestas = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

fi_arestas = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

nos = [1, 2, 3, 4]

N = 4

src = [0, 1, 2, 3]
dest = [3, 2, 1, 0]

class Graph:

    def minDistance(self, dist, queue):
        minimum = float("Inf")
        min_index = -1

        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def printPath(self, parent, j, path):

        if parent[j] == -1 :
            path.append(j)
            return path
        self.printPath(parent , parent[j], path)
        path.append(j)

    def printSolution(self, dist, parent, src, dest):
        path = []
        self.printPath(parent,dest, path)
        return path

    def dijkstra(self, graph, src, dest):
        row = len(graph)
        col = len(graph[0])
        dist = [float("Inf")] * row
        parent = [-1] * row
        dist[src] = 0
        queue = []

        for i in range(row):
            queue.append(i)

        while queue:
            u = self.minDistance(dist,queue)
            queue.remove(u)

            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

        path = self.printSolution(dist, parent, src, dest)
        return path


def valor_aresta(d, fi):
    return 1.178175 * d / fi

def calcula_arestas():
    for i in range(len(custo_arestas)):
        for j in range(len(custo_arestas[0])):
            custo_arestas[i][j] = valor_aresta(
                dist(nos[i], nos[j]), fi_arestas[i][j])

def dist(nodeA, nodeB):
    return 10

def calcula_fi(path):
    length = len(path)
    for i in range(length - 1):
        fi_arestas[path[i]][path[i+1]] += 1
        fi_arestas[path[i+1]][path[i]] += 1

def main():
    g = Graph()

    for i in range(10):
        calcula_arestas()

        for j in range(N):
            path = g.dijkstra(custo_arestas, src[j], dest[j])
            calcula_fi(path)

    

main()
