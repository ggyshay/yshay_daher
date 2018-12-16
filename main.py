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


def valor_aresta(d, fi):
    return 1.178175 * d / fi


def calcula_arestas():
    for i in range(len(custo_arestas)):
        for j in range(len(custo_arestas[0])):
            custo_arestas[i][j] = valor_aresta(
                dist(nos[i], nos[j]), fi_arestas[i][j])


def dist(nodeA, nodeB):
    return 10

def calcula_fi():
    return 10

def dijkstra():
    return 10

def main():
    print("ta rolante")
    for i in range(10):
        calcula_arestas()
        dijkstra()
        calcula_fi()
    return True


main()
