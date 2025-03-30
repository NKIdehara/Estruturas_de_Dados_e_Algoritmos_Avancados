class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, valor):
        self.heap.append(valor)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        pai = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[pai][0] :
            self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
            index = pai
            pai = (index - 1) // 2

    def _heapify_down(self, index):
        min = index
        esquerda = 2 * index + 1
        direita = 2 * index + 2

        if esquerda < len(self.heap) and self.heap[esquerda][0]  < self.heap[min][0] :
            min = esquerda
        if direita < len(self.heap) and self.heap[direita][0]  < self.heap[min][0] :
            min = direita

        if min != index:
            self.heap[index], self.heap[min] = self.heap[min], self.heap[index]
            self._heapify_down(min)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def change(self, uid, nova_prioridade):
        for i in range(len(self.heap)):
            if self.heap[i][1] == uid:
                print(f"Pacote {uid} atualizado. Prioridade {self.heap[i][0]} -> {nova_prioridade}\n")
                self.heap[i] = (nova_prioridade, self.heap[i][1], self.heap[i][2])
                self._heapify_up(i)
                self._heapify_down(i)
                return True
        return False

pacotes_rede = [
    (2, "ebed60c0-e3f2-4f7c-97bb-a046e7ca90f1", 246.93),
    (3, "738866dc-957c-4764-89cb-b4eeb56c32ba", 233.83),
    (4, "88c2db52-16c0-4fd7-9c60-3bec408c345b", 296.48),
    (9, "35211feb-d322-4267-9e92-6e3d743ce6c1", 233.74),
    (7, "b134b2e9-d5a0-42b4-b537-7159247f64ca", 149.09),
    (5, "c1834f86-82cf-4402-8729-ecdb754c66db", 298.23)
]
roteador = MinHeap()
for pacote in pacotes_rede:
    roteador.insert(pacote)

roteador.change("35211feb-d322-4267-9e92-6e3d743ce6c1", 0)

while len(roteador.heap) > 0:
    prioridade, uid, tempo = roteador.pop()
    print(f"ID do pacote: {uid}\tTempo de transmissão: {tempo}\tPrioridade: {prioridade}")
