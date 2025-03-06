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

    def mostrar_grafo(self):
        for vertice in self.lista:
            print(f"{vertice} -> {self.lista[vertice]}")

    def bfs(self, inicio, fim):
        visitados = set()
        fila = [[inicio]]
        print(f"Percorrendo caminho de {inicio} até {fim}")
        while fila:
            caminho = fila.pop(0)
            vertice = caminho[-1]
            print(f"{caminho}")
            if vertice  == fim:
                return caminho
            if vertice not in visitados:
                visitados.add(vertice)
                for vizinho in self.lista[vertice]:
                    novo_caminho = list(caminho)
                    novo_caminho.append(vizinho)
                    fila.append(novo_caminho)
        return

grafo = Grafo()
bairros = ["A", "B", "C", "D", "E", "F"]
for bairro in bairros:
    grafo.adicionar_vertice(bairro)

ruas = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "E"), ("E", "D"), ("E", "F"), ("D", "F")]
for r1, r2 in ruas:
    grafo.adicionar_aresta(r1, r2)

print("Lista de Adjacência:")
grafo.mostrar_grafo()
print()

inicio = "A"
fim = "F"
print(f"\nCaminho mais curto de {inicio} para {fim}: {grafo.bfs(inicio, fim)}")
