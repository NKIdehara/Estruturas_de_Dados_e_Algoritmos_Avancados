import random
import time

def calcular_distancia(cidade1, cidade2):
    x1, y1 = cidade1
    x2, y2 = cidade2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Algoritmo de Held-Karp
def held_karp(cidades):
    n = len(cidades)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = calcular_distancia(cidades[i], cidades[j])
    memo = {}
    caminho_melhor = {}
    def tsp(mask, pos):
        if mask == (1 << n) - 1:
            return dist[pos][0]
        if (mask, pos) in memo:
            return memo[(mask, pos)]
        res = float('inf')
        melhor_prox = None
        for proxima_pos in range(n):
            if mask & (1 << proxima_pos) == 0:
                nova_res = dist[pos][proxima_pos] + tsp(mask | (1 << proxima_pos), proxima_pos)
                if nova_res < res:
                    res = nova_res
                    melhor_prox = proxima_pos
        memo[(mask, pos)] = res
        caminho_melhor[(mask, pos)] = melhor_prox
        return res
    melhor_distancia = tsp(1, 0)
    mask, pos = 1, 0
    caminho = [0]
    while len(caminho) < n:
        pos = caminho_melhor[(mask, pos)]
        caminho.append(pos)
        mask |= (1 << pos)
    caminho.append(0)
    return caminho, melhor_distancia

# Heurística do vizinho mais próximo
def tsp_vizinho_mais_proximo(cidades):
    def encontrar_vizinho_mais_proximo(cidade_atual, cidades_nao_visitadas):
        menor_distancia = float('inf')
        cidade_mais_proxima = None
        for cidade in cidades_nao_visitadas:
            distancia = calcular_distancia(cidade_atual, cidade)
            if distancia < menor_distancia:
                menor_distancia = distancia
                cidade_mais_proxima = cidade
        return cidade_mais_proxima, menor_distancia
    cidade_inicial = cidades[0]
    caminho = [cidade_inicial]
    cidades_nao_visitadas = cidades[1:]
    distancia_total = 0
    cidade_atual = cidade_inicial
    while cidades_nao_visitadas:
        proxima_cidade, distancia = encontrar_vizinho_mais_proximo(cidade_atual, cidades_nao_visitadas)
        caminho.append(proxima_cidade)
        cidades_nao_visitadas.remove(proxima_cidade)
        distancia_total += distancia
        cidade_atual = proxima_cidade
    distancia_total += calcular_distancia(cidade_atual, cidade_inicial)
    caminho.append(cidade_inicial)
    return caminho, distancia_total

# (1) (2)
cidades = [(0,0), (91,24), (13,45), (20,23), (96,79)]

print("Algoritmo de Held-Karp")
caminho, distancia = held_karp(cidades)
print("Melhor caminho encontrado:", [cidades[i] for i in caminho])
print("Melhor distância encontrada:", distancia)

print("\nHeurística do vizinho mais próximo")
caminho, distancia = tsp_vizinho_mais_proximo(cidades)
print("Melhor caminho encontrado:", caminho)
print("Distância total percorrida:", distancia)


# (3)
print("\nAlgoritmo de Held-Karp vs Heurística do vizinho mais próximo")
cidades = [(0,0)]
for i in range (1, 20):
    cidades.append((random.randint(1, 99), random.randint(1, 99)))
    t_1 = time.time()
    caminho_held_karp, distancia_held_karp = held_karp(cidades)
    t_2 = time.time()
    caminho_vizinho_mais_proximo, distancia_vizinho_mais_proximo = tsp_vizinho_mais_proximo(cidades)
    t_3 = time.time()
    print(f"Número de cidades: {len(cidades)}\tTempo (Held-Karp): {(t_2 - t_1):.2f}\tTempo (vizinho mais próximo): {(t_3 - t_2):.2f}\tDistância (Held-Karp): {distancia_held_karp}\tDistância (vizinho mais próximo): {distancia_vizinho_mais_proximo}")