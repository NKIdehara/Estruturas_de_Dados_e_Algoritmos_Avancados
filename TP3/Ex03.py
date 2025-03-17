class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_aeroporto(self, aeroporto):
        if aeroporto not in self.vertices:
            self.vertices[aeroporto] = {}

    def adicionar_rota(self, rota1, rota2, distancia):
        self.vertices[rota1][rota2] = distancia
        self.vertices[rota2][rota1] = distancia

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


malha_aerea = GrafoPoderado()
aeroportos = ["GIG", "CNF", "BSB", "GRU", "SLZ", "BEL", "REC"]
for aeroporto in aeroportos:
    malha_aerea.adicionar_aeroporto(aeroporto)
malha_aerea.adicionar_rota("GIG", "CNF", 361)
malha_aerea.adicionar_rota("GIG", "BSB", 911)
malha_aerea.adicionar_rota("CNF", "BSB", 590)
malha_aerea.adicionar_rota("CNF", "GRU", 495)
malha_aerea.adicionar_rota("BSB", "SLZ", 1524)
malha_aerea.adicionar_rota("GRU", "SLZ", 2319)
malha_aerea.adicionar_rota("GRU", "BEL", 2450)
malha_aerea.adicionar_rota("SLZ", "BEL", 490)
malha_aerea.adicionar_rota("BEL", "REC", 1678)

for origem in aeroportos:
    for destino in aeroportos:
        if origem == destino:
            continue
        rota, distancia = malha_aerea.dijkstra(origem, destino)
        print(f"Melhor rota de {origem} para {destino}: {' => '.join(rota)} / Distância total: {distancia} km")
