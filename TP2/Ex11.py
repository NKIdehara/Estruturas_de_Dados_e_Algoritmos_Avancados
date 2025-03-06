class Grafo:
    def __init__(self):
        self.lista = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista:
            self.lista[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista and vertice2 in self.lista:
            self.lista[vertice1].append(vertice2)
            self.lista[vertice2].append(vertice1)

    def dfs_recursivo(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()
        print(vertice, end=" ")
        visitados.add(vertice)
        for vizinho in self.lista[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)

grafo = Grafo()
vertices = ["A", "B", "C", "D", "E"]
for vertice in vertices:
    grafo.adicionar_vertice(vertice)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E")]
for aresta1, aresta2 in arestas:
    grafo.adicionar_aresta(aresta1, aresta2)

aresta = "A"
print(f"DFS a partir de {aresta}: ", end="")
grafo.dfs_recursivo(aresta)
