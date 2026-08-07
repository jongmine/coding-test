# 원소의 개수: N
# 트리의 높이: log2(N)


class MaxHeap:
    def __init__(self):
        self.items = [None]


    def insert(self, value):
        self.items.append(value)
        current = len(self.items) - 1

        while current != 1: # O(logN)
            parent = current // 2

            if self.items[current] > self.items[parent]:
                self.items[current], self.items[parent] = self.items[parent], self.items[current]
            else:
                break
            current = parent


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!