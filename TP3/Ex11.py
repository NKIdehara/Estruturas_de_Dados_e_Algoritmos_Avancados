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

infraestrutura  = GrafoAlgoritmoPrim(6)
torres_comunicacao = [
    (0, 1, 737.82),
    (0, 2, 577.11),
    (1, 2, 389.21),
    (1, 3, 316.90),
    (2, 3, 773.36),
    (2, 4, 618.80),
    (3, 4, 327.57),
    (3, 5, 508.18),
    (4, 5, 493.69)
]

for torre1, torre2, custo in torres_comunicacao:
    infraestrutura .adicionar_aresta(torre1, torre2, custo)

infraestrutura .prim()
