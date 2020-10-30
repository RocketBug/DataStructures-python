class PriorityQueue:
    def __init__(self) -> None:
        self.list = []

    def insert(self, value: int) -> None:
        self.list.insert(0, value)
        self.__min_heapify(i=0)
        
    def pull(self) -> int:
        root = 0
        last_pos = len(self.list)-1
        (self.list[root], self.list[last_pos]) = (self.list[last_pos], self.list[root])
        smallest_val = self.list.pop(last_pos)
        self.__min_heapify(i=0)
        return smallest_val

    def __min_heapify(self, i: int) -> None:
        left = (i*2)+1
        right = (i*2)+2
        smallest_pos = i

        if left < len(self.list) and self.list[left] < self.list[smallest_pos]:
            smallest_pos = left

        if right < len(self.list) and self.list[right] < self.list[smallest_pos]:
            smallest_pos = right

        if smallest_pos != i:
            (self.list[i], self.list[smallest_pos]) = (self.list[smallest_pos], self.list[i])
            self.__min_heapify(i=smallest_pos)

    def print_heap(self) -> None:
        print(self.list)

    def __max_heapify(self, i: int) -> None:
        left = (i*2)+1
        right = (i*2)+2
        largest_pos = i

        if left < len(self.list) and self.list[left] > self.list[largest_pos]:
            largest_pos = left

        if right < len(self.list) and self.list[right] > self.list[largest_pos]:
            largest_pos = right

        if largest_pos != i:
            (self.list[i], self.list[largest_pos]) = (self.list[largest_pos], self.list[i])
            self.__max_heapify(i=largest_pos)


pq = PriorityQueue()
pq.insert(value=9)
pq.insert(value=5)
pq.insert(value=1)
pq.insert(value=2)
pq.insert(value=6)
pq.insert(value=3)
pq.insert(value=7)
pq.print_heap()
pq.pull()
pq.print_heap()
