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

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista:
            print(f"Vizinhos de {vertice}: {self.lista[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def bfs(self, inicio, fim):
        visitados = set()
        fila = [[inicio]]
        while fila:
            caminho = fila.pop(0)
            vertice = caminho[-1]
            if vertice  == fim:
                return caminho
            if vertice not in visitados:
                visitados.add(vertice)
                for vizinho in self.lista[vertice]:
                    novo_caminho = list(caminho)
                    novo_caminho.append(vizinho)
                    fila.append(novo_caminho)
        return

# (1)
grafo = Grafo()
centros = ["A", "B", "C", "D", "E"]
for centro in centros:
    grafo.adicionar_vertice(centro)
conexoes = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "E")]
for c1, c2 in conexoes:
    grafo.adicionar_aresta(c1, c2)

# (2)
for centro in centros:
    grafo.mostrar_vizinhos(centro)

# (4)
inicio = "A"
fim = "D"
print(f"\nCaminho mais curto de {inicio} para {fim}: {grafo.bfs(inicio, fim)}")
