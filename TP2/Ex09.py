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

    def bfs(self, inicio):
        visitados = set()
        fila = [inicio]
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=" ")
                visitados.add(vertice)
                fila.extend(self.lista[vertice])

grafo = Grafo()
vertices = ["A", "B", "C", "D", "E", "F"]
for vertice in vertices:
    grafo.adicionar_vertice(vertice)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "F"), ("E", "F")]
for aresta1, aresta2 in arestas:
    grafo.adicionar_aresta(aresta1, aresta2)

aresta = "A"
print(f"BFS a partir de {aresta}: ", end="")
grafo.bfs(aresta)
