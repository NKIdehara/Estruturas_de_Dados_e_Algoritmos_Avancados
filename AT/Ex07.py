class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.vertices:
            self.vertices[bairro] = {}

    def adicionar_rua(self, bairro1, barro2, tempo):
        self.vertices[bairro1][barro2] = tempo
        self.vertices[barro2][bairro1] = tempo

    def floyd_warshall(self, origem, destino):
        bairros = list(self.vertices.keys())
        tempo = {i: {j: float('inf') if i != j else 0 for j in bairros} for i in bairros}
        bairro_anterior = {i: {j: None for j in bairros} for i in bairros}
        for bairro, vizinhos in self.vertices.items():
            for vizinho, deslocamento in vizinhos.items():
                tempo[bairro][vizinho] = deslocamento
                bairro_anterior[bairro][vizinho] = vizinho
        for k in bairros:
            for i in bairros:
                for j in bairros:
                    if tempo[i][j] > tempo[i][k] + tempo[k][j]:
                        tempo[i][j] = tempo[i][k] + tempo[k][j]
                        bairro_anterior[i][j] = bairro_anterior[i][k]
        caminho = []
        atual = origem
        while atual != destino:
            if atual is None:
                return None, float("inf")
            caminho.append(atual)
            atual = bairro_anterior[atual][destino]
        caminho.append(destino)
        return caminho, tempo[origem][destino]
    
    def lista_adjacencia(self):
        for bairro, vizinhos in self.vertices.items():
            print(f"{bairro}: {', '.join([f'{v} ({d} min)' for v, d in vizinhos.items()])}")

    def matriz_adjacencia(self):
        bairros = list(self.vertices.keys())
        n = len(bairros)
        matriz = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            matriz[i][i] = 0
            for j in range(n):
                if bairros[j] in self.vertices[bairros[i]]:
                    matriz[i][j] = self.vertices[bairros[i]][bairros[j]]
        print("\t", "\t".join(bairros))
        for i in range(n):
            print(bairros[i], end="\t")
            for j in range(n):
                print(matriz[i][j], end="\t")
            print()


transporte_publico = GrafoPoderado()
bairros = ["A", "B", "C", "D", "E", "F"]
for bairro in bairros:
    transporte_publico.adicionar_bairro(bairro)
transporte_publico.adicionar_rua("A", "B", 5)
transporte_publico.adicionar_rua("A", "C", 10)
transporte_publico.adicionar_rua("B", "C", 3)
transporte_publico.adicionar_rua("B", "D", 8)
transporte_publico.adicionar_rua("C", "D", 2)
transporte_publico.adicionar_rua("C", "E", 7)
transporte_publico.adicionar_rua("D", "E", 4)
transporte_publico.adicionar_rua("D", "F", 6)
transporte_publico.adicionar_rua("E", "F", 5)

print("Lista de Adjacência")
transporte_publico.lista_adjacencia()

print("\nMatriz de Adjacência:")
transporte_publico.matriz_adjacencia()

print()
for origem in bairros:
    for destino in bairros:
        if origem != destino:
            rota, tempo = transporte_publico.floyd_warshall(origem, destino)
            print(f"Melhor rota de {origem} para {destino}: {' => '.join(rota)} / Tempo total: {tempo} min")
