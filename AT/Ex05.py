class Grafo:
    def __init__(self):
        self.lista = {}

    def adicionar_estacao(self, estacao):
        if estacao not in self.lista:
            self.lista[estacao] = []

    def adicionar_trilho(self, estacao1, estacao2):
        if estacao1 in self.lista:
            self.lista[estacao1].append(estacao2)

    def bfs(self, inicio):
        visitados = set()
        fila = [inicio]
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=" ")
                visitados.add(vertice)
                fila.extend(self.lista[vertice])

    def dfs_recursivo(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()
        print(vertice, end=" ")
        visitados.add(vertice)
        for vizinho in self.lista[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)

rede_metro = Grafo()
estacoes = ["A", "B", "C", "D", "E", "F"]
for estacao in estacoes:
    rede_metro.adicionar_estacao(estacao)

trilhos = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("D", "E"), ("E", "F")]
for estacao1, estacao2 in trilhos:
    rede_metro.adicionar_trilho(estacao1, estacao2)

estacao_inicio = "A"
print(f"DFS a partir de {estacao_inicio}: ", end="")
rede_metro.dfs_recursivo(estacao_inicio)
print()
print(f"BFS a partir de {estacao_inicio}: ", end="")
rede_metro.bfs(estacao_inicio)
