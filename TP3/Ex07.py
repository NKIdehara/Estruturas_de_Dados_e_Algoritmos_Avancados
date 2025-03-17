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
        print(f"Custo total da AGM: {custo_total}")

rede_fibra_otica = GrafoAlgoritmoPrim(6)
conexoes = [
    (0, 1, 6),
    (0, 2, 7),
    (1, 2, 3),
    (1, 3, 8),
    (2, 3, 3),
    (2, 4, 8),
    (3, 4, 2),
    (3, 5, 5),
    (4, 5, 1)
]

for bairro1, bairro2, custo in conexoes:
    rede_fibra_otica.adicionar_aresta(bairro1, bairro2, custo)

rede_fibra_otica.prim()
