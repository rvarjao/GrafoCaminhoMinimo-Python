# Fundamentos Matemáticos para a Ciência da Computacao
# 3a edicao
# Judith L Gersting
# p. 286

# procedure CaminhoMínimo(A: matriz n X n; x, y: vértices);
# (Algoritmo de Dijkstra — A é a matriz de adjacências modificada de um grafo simples conexo com pesos positivos;
# x e y são vértices do grafo;
# a procedure apresenta o menor caminho de x a y e a distância deste caminho)
import sys

inf = sys.maxsize

def caminho_minimo(A, x, y):
    n = len(A)

    # print("Analisando caminho: {} -> {}".format(x, y))
    IN = [x]    # conjunto de vértices; {menor caminho conhecido a partir de x}

    d = [inf]*n #vetor de inteiros; distancia a partir de x usando os vértices de.IN}
    d[x] = 0

    s = [inf]*n  #vetor de vértices; vertice anterior no caminho mínimo}
    distAnterior = inf #distancia a ser comparada

    # inicia o conjunto IN e os vetores d e s
    for z in range(n):
        if z != x:
            d[z] = A[x][z]
            s[z] = x

#   processa os vértices de IN
    while (IN.__contains__(y) == False):
    #{inclui o vértice de distância mínima que ainda não está em IN}
    # p : = vértice z que não pertença a IN com d[z] mínima;
            p = -1
            minD = inf
            for z in range(n):
                if (IN.__contains__(z) == False):
                    if (minD > d[z]):
                        minD = d[z]
                        p = z
            IN.append(p)

        #         { recalcula d para vértices que não pertençam a IN, ajusta s se necessário }
        # for todos os vértices z que não pertençam a IN do
            for z in range(n):
                if (IN.__contains__(z) == False):
                    distAnterior = d[z]
                    d[z] = min(d[z], d[p] + A[p][z])

                    if (d[z] != distAnterior):
                        s[z] = p
                    # print("d: ", end=" ")
                    # imprimir_array(d)
                    # print("IN: ", end=" ")
                    # imprimir_array(IN)
                    # print("s: ", end=" ")
                    # imprimir_array(s)
                    # print("-----")

    caminho = []
    caminho.append(y)
    z = y
    while (z != x):
        z = s[z]
        caminho.insert(0, z)
    print("menor caminho entre {} e {}: ".format(x,y), end=" ")
    imprimir_array(caminho)


def get_min_value(self, table):
    min_values = []
    for i in range(len(table)):
        min_value = min(table[i])
        min_values.append(min_value)

    return min(min_values)



def imprimir_matriz(a):
    for i in a:
        for j in i:
            print(j, end=" ")
        print("")

def imprimir_array(a):
    for i in a:
        print(i, end=" ")
    print("")



# Matriz de adjacencias modificada
# representando o grafo
A = [[inf, 3, 8, 4, inf, 10],
     [3, inf, inf, 6, inf, inf],
     [8, inf, inf, inf, 7, inf],
     [4, 6, inf, inf, 1, 3],
     [inf, inf, 7, 1, inf, 1],
     [10, inf, inf, 3, 1, inf]]

# vertices selecionados
# x = 0
# y = 5

caminho_minimo(A, 0, 5)

print("---===demais caminhos===---")
for i in range(0,6):
    for j in range(i+1,6):
        caminho_minimo(A, i, j)