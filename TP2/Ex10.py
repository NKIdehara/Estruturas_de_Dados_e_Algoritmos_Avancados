class Grafo:
    def __init__(self):
        self.lista = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista:
            self.lista[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista:
            self.lista[vertice1].append(vertice2)

    def bfs(self, inicio):
        visitados = set()
        fila = [inicio]
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=" ")
                visitados.add(vertice)
                fila.extend(self.lista[vertice])

    def dfs_recursivo(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()
        print(vertice, end=" ")
        visitados.add(vertice)
        for vizinho in self.lista[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)

grafo = Grafo()
vertices = ["1", "2", "3", "4", "5", "6"]
for vertice in vertices:
    grafo.adicionar_vertice(vertice)

arestas = [("1", "2"), ("1", "3"), ("2", "4"), ("3", "5"), ("4", "6"), ("5", "6")]
for aresta1, aresta2 in arestas:
    grafo.adicionar_aresta(aresta1, aresta2)

aresta = "1"
print(f"DFS a partir de {aresta}: ", end="")
grafo.dfs_recursivo(aresta)
print()
print(f"BFS a partir de {aresta}: ", end="")
grafo.bfs(aresta)
