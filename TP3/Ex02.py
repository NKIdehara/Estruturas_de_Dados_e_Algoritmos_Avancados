class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.vertices:
            self.vertices[bairro] = {}

    def adicionar_trajeto(self, bairro1, bairro2, tempo_deslocamento):
        self.vertices[bairro1][bairro2] = tempo_deslocamento
        self.vertices[bairro2][bairro1] = tempo_deslocamento

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

cidade = GrafoPoderado()
bairros = ["Centro", "Ipanema", "Laranjeiras", "Urca", "Maracanã", "Vila Isabel", "Campo Grande"]
for bairro in bairros:
    cidade.adicionar_bairro(bairro)
cidade.adicionar_trajeto("Centro", "Ipanema", 3)
cidade.adicionar_trajeto("Centro", "Laranjeiras", 5)
cidade.adicionar_trajeto("Ipanema", "Laranjeiras", 7)
cidade.adicionar_trajeto("Ipanema", "Urca", 3)
cidade.adicionar_trajeto("Laranjeiras", "Maracanã", 5)
cidade.adicionar_trajeto("Urca", "Maracanã", 5)
cidade.adicionar_trajeto("Urca", "Vila Isabel", 9)
cidade.adicionar_trajeto("Maracanã", "Vila Isabel", 7)
cidade.adicionar_trajeto("Vila Isabel", "Campo Grande", 4)

for origem in bairros:
    for destino in bairros:
        if origem == destino:
            continue
        trajeto, tempo = cidade.dijkstra(origem, destino)
        print(f"Menor tempo de {origem} para {destino}: {' => '.join(trajeto)} / Tempo total: {tempo} min")
