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

tarefas = [(7, 'Assistir Netflix'), (2, 'Estudar Estrutura de Dados'), (4, 'Jantar'), (9, 'Limpar a casa'), (3, 'Estudar Redes')]
heap = MinHeap()
for _ in tarefas:
    heap.insert(_)

while len(heap.heap) > 0:
    print(heap.pop())
