class GrafoAlgoritmoPrim:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0] * vertices for _ in range(vertices)]

    def adicionar_aresta(self, u, v, peso):
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def prim(self):
        infinito = float('inf')
        selecionado = [False] * self.V
        chave = [infinito] * self.V
        pai = [-1] * self.V
        chave[0] = 0
        for _ in range(self.V):
            minimo = infinito
            u = -1
            for v in range(self.V):
                if not selecionado[v] and chave[v] < minimo:
                    minimo = chave[v]
                    u = v
            selecionado[u] = True
            for v in range(self.V):
                if 0 < self.grafo[u][v] < chave[v] and not selecionado[v]:
                    chave[v] = self.grafo[u][v]
                    pai[v] = u
        print("\nArestas da Árvore Geradora Mínima:")
        custo_total = 0
        for i in range(1, self.V):
            print(f"{pai[i]} - {i} (Custo: {self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Custo total da rede: {custo_total:.2f}")

sistema_abastecimento = GrafoAlgoritmoPrim(6)
tubulacoes = [
    (0, 1, 619.64),
    (0, 2, 844.19),
    (1, 2, 251.23),
    (1, 3, 410.50),
    (2, 3, 865.57),
    (2, 4, 626.19),
    (3, 4, 748.37),
    (3, 5, 657.64),
    (4, 5, 812.42)
]

for bairro1, bairro2, custo in tubulacoes:
    sistema_abastecimento.adicionar_aresta(bairro1, bairro2, custo)

sistema_abastecimento.prim()
