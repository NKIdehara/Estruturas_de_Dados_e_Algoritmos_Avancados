class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.vertices:
            self.vertices[bairro] = {}

    def adicionar_rota(self, bairro1, barro2, distancia):
        self.vertices[bairro1][barro2] = distancia
        self.vertices[barro2][bairro1] = distancia

    def dijkstra(self, origem, destino):
        nao_visitados = list(self.vertices.keys())
        pesos = {vertice: float("inf") for vertice in self.vertices}
        pesos[origem] = 0
        predecessores = {}
        while nao_visitados:
            vertice_atual = min(nao_visitados, key=lambda vertice: pesos[vertice])
            if pesos[vertice_atual] == float("inf"):
                break
            for vizinho, peso in self.vertices[vertice_atual].items():
                novo_peso = pesos[vertice_atual] + peso
                if novo_peso < pesos[vizinho]:
                    pesos[vizinho] = novo_peso
                    predecessores[vizinho] = vertice_atual
            nao_visitados.remove(vertice_atual)
        caminho = []
        vertice_atual = destino
        while vertice_atual in predecessores:
            caminho.append(vertice_atual)
            vertice_atual = predecessores[vertice_atual]
        caminho.append(origem)
        caminho.reverse()
        return caminho, pesos[destino]

    def lista_adjacencia(self):
        for bairro, vizinhos in self.vertices.items():
            print(f"{bairro}: {', '.join([f'{v} ({d} km)' for v, d in vizinhos.items()])}")

entrega = GrafoPoderado()
bairros = ["CD", "A", "B", "C", "D", "E", "F"]
for bairro in bairros:
    entrega.adicionar_bairro(bairro)
entrega.adicionar_rota("CD", "A", 4)
entrega.adicionar_rota("CD", "B", 2)
entrega.adicionar_rota("A", "C", 5)
entrega.adicionar_rota("A", "D", 10)
entrega.adicionar_rota("B", "A", 3)
entrega.adicionar_rota("B", "D", 8)
entrega.adicionar_rota("C", "D", 2)
entrega.adicionar_rota("C", "E", 4)
entrega.adicionar_rota("D", "E", 6)
entrega.adicionar_rota("D", "F", 5)
entrega.adicionar_rota("E", "F", 3)

print("Lista de Adjacência")
entrega.lista_adjacencia()

origem = "CD"
destino = "F"
rota, distancia = entrega.dijkstra(origem, destino)
print(f"\nMelhor rota de {origem} para {destino}: {' => '.join(rota)} / Distância total: {distancia} km")
