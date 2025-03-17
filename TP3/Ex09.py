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

rede_eletrica = GrafoAlgoritmoPrim(6)
linhas_transmissao = [
    (0, 1, 457.24),
    (0, 2, 104.54),
    (1, 2, 187.54),
    (1, 3, 846.47),
    (2, 3, 347.25),
    (2, 4, 457.14),
    (3, 4, 764.25),
    (3, 5, 528.75),
    (4, 5, 157.47)
]

for cidade1, cidade2, custo in linhas_transmissao:
    rede_eletrica.adicionar_aresta(cidade1, cidade2, custo)

rede_eletrica.prim()
