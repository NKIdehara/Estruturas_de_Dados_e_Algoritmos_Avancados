import random
import string
import time

class GrafoAlgoritmoPrim:
    def __init__(self, vertices):
        self.vertices = vertices
        self.V = len(vertices)
        self.grafo = {vertice: {} for vertice in vertices}

    def adicionar_aresta(self, u, v, peso):
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def prim(self):
        infinito = float('inf')
        selecionado = {vertice: False for vertice in self.vertices}
        chave = {vertice: infinito for vertice in self.vertices}
        pai = {vertice: None for vertice in self.vertices}
        chave[self.vertices[0]] = 0
        for _ in range(self.V):
            u = min((v for v in self.vertices if not selecionado[v]), key=lambda v: chave[v], default=None)
            if u is None:
                break
            selecionado[u] = True
            for v, peso in self.grafo[u].items():
                if not selecionado[v] and peso < chave[v]:
                    chave[v] = peso
                    pai[v] = u
        print("\nArestas da Árvore Geradora Mínima:")
        custo_total = 0
        for v in self.vertices[1:]:
            if pai[v] is not None:
                print(f"{pai[v]} - {v} com custo {self.grafo[v][pai[v]]}")
                custo_total += self.grafo[v][pai[v]]
        print(f"-> Custo total da MST: {custo_total}")

    def prim_tempo(self):
        t_ini = time.time()
        infinito = float('inf')
        selecionado = {vertice: False for vertice in self.vertices}
        chave = {vertice: infinito for vertice in self.vertices}
        pai = {vertice: None for vertice in self.vertices}
        chave[self.vertices[0]] = 0
        for _ in range(self.V):
            u = min((v for v in self.vertices if not selecionado[v]), key=lambda v: chave[v], default=None)
            if u is None:
                break
            selecionado[u] = True
            for v, peso in self.grafo[u].items():
                if not selecionado[v] and peso < chave[v]:
                    chave[v] = peso
                    pai[v] = u
        custo_total = 0
        for v in self.vertices[1:]:
            if pai[v] is not None:
                custo_total += self.grafo[v][pai[v]]
        t_fim = time.time()
        print(f"Tamanho do grafo: {len(self.vertices)} vértices\tTempo: {(t_fim - t_ini):.2f}\tCusto total da MST: {custo_total}")

    def imprimir_grafo(self):
        print("Lista de Adjacências:")
        for vertice, adjacentes in self.grafo.items():
            print(f"{vertice}: {', '.join(f'{v}({peso})' for v, peso in adjacentes.items())}")

def criar_vertices(tamanho):
    letras = string.ascii_uppercase
    vertices = []
    for a in letras:
        for b in letras:
            for c in letras:
                for d in letras:
                    vertices.append(a+b+c+d)
                    if len(vertices) >= tamanho:
                        return vertices

print("(1) / (2)")
cidades = [
    "São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza",
    "Belo Horizonte", "Manaus", "Belém", "Recife", "Goiânia"
]
rede_internet = GrafoAlgoritmoPrim(cidades)
rede_internet.adicionar_aresta("São Paulo", "Belo Horizonte", 46)
rede_internet.adicionar_aresta("São Paulo", "Goiânia", 39)
rede_internet.adicionar_aresta("São Paulo", "Rio de Janeiro", 27)
rede_internet.adicionar_aresta("Rio de Janeiro", "Belo Horizonte", 32)
rede_internet.adicionar_aresta("Rio de Janeiro", "Salvador", 70)
rede_internet.adicionar_aresta("Rio de Janeiro", "Brasília", 53)
rede_internet.adicionar_aresta("Brasília", "Salvador", 65)
rede_internet.adicionar_aresta("Salvador", "Belo Horizonte", 61)
rede_internet.adicionar_aresta("Salvador", "Fortaleza", 47)
rede_internet.adicionar_aresta("Recife", "Belo Horizonte", 82)
rede_internet.adicionar_aresta("Recife", "Goiânia", 73)
rede_internet.adicionar_aresta("Recife", "Belém", 56)
rede_internet.adicionar_aresta("Recife", "Fortaleza", 15)
rede_internet.adicionar_aresta("Goiânia", "Belo Horizonte", 44)
rede_internet.adicionar_aresta("Goiânia", "Manaus", 89)
rede_internet.adicionar_aresta("Manaus", "Belém", 41)
rede_internet.adicionar_aresta("Fortaleza", "Belém", 64)
rede_internet.imprimir_grafo()
rede_internet.prim()

print("\n(3)")
for i in range(18):
    vertices = criar_vertices(2**i)
    grafo = GrafoAlgoritmoPrim(vertices)
    for i in vertices:
        vizinhos = random.sample([vizinho for vizinho in vertices if vizinho != i], min(5, len(vertices)-1))
        for j in vizinhos:
            grafo.adicionar_aresta(i, j, random.randint(1, 99))
    grafo.prim_tempo()
