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

entrega = GrafoPoderado()
bairros = ["Centro de Distribuição", "Copacabana", "Botafogo", "Méier", "Tijuca", "Jacarepaguá", "Bangu"]
for bairro in bairros:
    entrega.adicionar_bairro(bairro)
entrega.adicionar_rota("Centro de Distribuição", "Copacabana", 7)
entrega.adicionar_rota("Centro de Distribuição", "Botafogo", 4)
entrega.adicionar_rota("Copacabana", "Botafogo", 6)
entrega.adicionar_rota("Copacabana", "Méier", 3)
entrega.adicionar_rota("Botafogo", "Tijuca", 9)
entrega.adicionar_rota("Méier", "Tijuca", 7)
entrega.adicionar_rota("Méier", "Jacarepaguá", 2)
entrega.adicionar_rota("Tijuca", "Jacarepaguá", 5)
entrega.adicionar_rota("Jacarepaguá", "Bangu", 2)

origem = "Centro de Distribuição"
for destino in bairros:
    rota, distancia = entrega.dijkstra(origem, destino)
    print(f"Melhor rota de {origem} para {destino}: {' => '.join(rota)} / Distância total: {distancia} km")
