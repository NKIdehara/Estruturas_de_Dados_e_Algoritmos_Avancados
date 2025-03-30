import time

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(f"{num:2}" for num in linha))

def knight_tour(n):
    def movimento_valido(x, y, tabuleiro):
        return 0 <= x < n and 0 <= y < n and tabuleiro[x][y] == -1
    def _movimentar(n, tabuleiro, atual_x, atual_y, mov_x, mov_y, pos):
        if(pos == n**2):
            return True
        # Verificar movimetações
        for i in range(8):
            novo_x = atual_x + mov_x[i]
            novo_y = atual_y + mov_y[i]
            if(movimento_valido(novo_x, novo_y, tabuleiro)):
                tabuleiro[novo_x][novo_y] = pos
                if(_movimentar(n, tabuleiro, novo_x, novo_y, mov_x, mov_y, pos+1)):
                    return True
                tabuleiro[novo_x][novo_y] = -1 # movimento não permitido
        return False
    # cria tabuleiro
    tabuleiro = [[-1 for i in range(n)]for i in range(n)]
    # movimentos posíveis
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
    tabuleiro[0][0] = 0 # posição inicial
    pos = 1
    if(not _movimentar(n, tabuleiro, 0, 0, mov_x, mov_y, pos)):
        print("Solução não existe!")
    else:
        return tabuleiro

def passeio_do_cavalo(N, inicio_x=0, inicio_y=0):
    movimentos = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    def dentro_tabuleiro(x, y, N):
        return 0 <= x < N and 0 <= y < N
    def movimentos_possiveis(tabuleiro, x, y, N):
        moves = []
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if dentro_tabuleiro(nx, ny, N) and tabuleiro[nx][ny] == -1:
                moves.append((nx, ny))
        return moves
    def proximo_movimento(tabuleiro, x, y, N):
        moves = movimentos_possiveis(tabuleiro, x, y, N)
        if not moves:
            return None
        moves.sort(key=lambda move: len(movimentos_possiveis(tabuleiro, move[0], move[1], N)))
        return moves[0]  # Retorna o movimento com menos opções futuras
    tabuleiro = [[-1] * N for _ in range(N)]
    x, y = inicio_x, inicio_y
    tabuleiro[x][y] = 0  # Posição inicial do cavalo
    for i in range(1, N * N):
        movimento = proximo_movimento(tabuleiro, x, y, N)
        if not movimento:
            print("Falha: Caminho interrompido!")
            return None
        x, y = movimento
        tabuleiro[x][y] = i  # Marca o movimento no tabuleiro
    return tabuleiro

for n in range(5, 10):
    t_1 = time.time()
    tabuleiro = knight_tour(n)
    t_2 = time.time()
    tabuleiro = passeio_do_cavalo(n)
    t_3 = time.time()
    # mostrar_tabuleiro(tabuleiro)
    print(f"Tabuleiro: {n}x{n}\tTempo (força bruta): {(t_2 - t_1):.2f}\tTempo (Heurística de Warnsdorff): {(t_3 - t_2):.2f}")
