class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_rota(self, cidade1, cidade2, custo):
        if cidade1 not in self.vertices:
            self.vertices[cidade1] = {}
        if cidade2 not in self.vertices:
            self.vertices[cidade2] = {}
        self.vertices[cidade1][cidade2] = custo
        self.vertices[cidade2][cidade1] = custo

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


viagem = GrafoPoderado()
viagem.adicionar_rota("Rio de Janeiro", "Belo Horizonte", 448.57)
viagem.adicionar_rota("Rio de Janeiro", "Campinas", 378.24)
viagem.adicionar_rota("Belo Horizonte", "Campinas", 574.12)
viagem.adicionar_rota("Belo Horizonte", "Maceió", 818.37)
viagem.adicionar_rota("Campinas", "Curitiba", 475.15)
viagem.adicionar_rota("Maceió", "Curitiba", 925.86)
viagem.adicionar_rota("Maceió", "Recife", 112.94)
viagem.adicionar_rota("Curitiba", "Recife", 987.65)
viagem.adicionar_rota("Recife", "Brasília", 794.28)

origem = "Rio de Janeiro"
destino = "Recife"
rota, custo = viagem.dijkstra(origem, destino)
print(f"Melhor rota de {origem} para {destino}: {' => '.join(rota)}")
print(f"Custo total: R$ {custo:.2f}")
