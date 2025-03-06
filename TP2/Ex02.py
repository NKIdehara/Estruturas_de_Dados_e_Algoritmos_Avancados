class Grafo:
    def __init__(self):
        self.lista = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista:
            self.lista[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista and vertice2 in self.lista:
            self.lista[vertice1].append(vertice2)
            self.lista[vertice2].append(vertice1)

    def mostrar_grafo(self):
        for vertice in self.lista:
            print(f"{vertice} -> {self.lista[vertice]}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista:
            print(f"Vizinhos de {vertice}: {self.lista[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

grafo = Grafo()
bairros = ["Copacabana", "Ipanema", "Leblon", "Lagoa", "Humaita", "Botafogo"]
for bairro in bairros:
    grafo.adicionar_vertice(bairro)

ruas = [("Leblon", "Ipanema"), ("Leblon", "Lagoa"), ("Lagoa", "Ipanema"), ("Copacabana", "Ipanema"), ("Lagoa", "Humaita"), ("Humaita", "Botafogo"), ("Humaita", "Copacabana"), ("Copacabana", "Botafogo"), ]
for r1, r2 in ruas:
    grafo.adicionar_aresta(r1, r2)

print("Lista de Adjacência:")
grafo.mostrar_grafo()
grafo.mostrar_vizinhos("Copacabana")
