class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, valor):
        self.heap.append(valor)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        pai = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[pai]:
            self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
            index = pai
            pai = (index - 1) // 2

    def _heapify_down(self, index):
        max = index
        esquerda = 2 * index + 1
        direita = 2 * index + 2

        if esquerda < len(self.heap) and self.heap[esquerda] > self.heap[max]:
            max = esquerda
        if direita < len(self.heap) and self.heap[direita] > self.heap[max]:
            max = direita

        if max != index:
            self.heap[index], self.heap[max] = self.heap[max], self.heap[index]
            self._heapify_down(max)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def print(self):
        print(self.heap)

lista = [50, 30, 40, 10, 20, 35]
heap = MaxHeap()
for _ in lista:
    heap.insert(_)

heap.print()
heap.insert(45)
heap.print()

while len(heap.heap) > 0:
    print(heap.pop())
