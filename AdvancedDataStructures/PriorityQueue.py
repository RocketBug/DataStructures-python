from typing import List, Set


class PriorityQueue:
    def __init__(self) -> None:
        self.list = []

    def insert(self, value: int) -> None:
        self.list.insert(0, value)
        self.min_heapify(i=0)

    def pull(self) -> int:
        root = 0
        last_pos = len(self.list) - 1
        (self.list[root], self.list[last_pos]) = (self.list[last_pos], self.list[root])
        smallest_val = self.list.pop(last_pos)
        self.min_heapify(i=0)
        return smallest_val

    def min_heapify(self, i: int) -> None:
        left = (i * 2) + 1
        right = (i * 2) + 2
        smallest_pos = i

        if left < len(self.list) and self.list[left] < self.list[smallest_pos]:
            smallest_pos = left

        if right < len(self.list) and self.list[right] < self.list[smallest_pos]:
            smallest_pos = right

        if smallest_pos != i:
            (self.list[i], self.list[smallest_pos]) = (self.list[smallest_pos], self.list[i])
            self.min_heapify(i=smallest_pos)

    def print_heap(self) -> None:
        print(self.list)

    def max_heapify(self, i: int) -> None:
        left = (i * 2) + 1
        right = (i * 2) + 2
        largest_pos = i

        if left < len(self.list) and self.list[left] > self.list[largest_pos]:
            largest_pos = left

        if right < len(self.list) and self.list[right] > self.list[largest_pos]:
            largest_pos = right

        if largest_pos != i:
            (self.list[i], self.list[largest_pos]) = (self.list[largest_pos], self.list[i])
            self.max_heapify(i=largest_pos)


pq = PriorityQueue()
elements = [3, 2, 2, 0]
pq.build_heap(elements)
pq.print_heap()
