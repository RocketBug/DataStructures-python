import random
class minHeap:
    def __init__(self, currentHeap):
        self.minheap = currentHeap

    def insert(self, data):
        self.minheap.append(data)

    def get_left_child_pos(self, current_pos):
        return (2*current_pos)+1

    def get_right_child_pos(self, current_pos):
        return (2*current_pos)+2

    def get_parent_pos(self, current_pos):
        return int((current_pos-1)/2)

    def get_size(self):
        return len(self.minheap)

    
    def isLeaf(self, current_pos):
        if current_pos >= (self.get_size() // 2) and current_pos <= self.get_size():
            return True
        
        return False

    def swap(self, fpos, spos):
        temp = self.minheap[fpos]
        self.minheap[fpos] = self.minheap[spos]
        self.minheap[spos] = temp 

    def heapify(self, pos):
        if not self.isLeaf(pos):
            
            if self.minheap[pos] > self.minheap[self.get_left_child_pos(pos)] or self.minheap[pos] > self.minheap[self.get_right_child_pos(pos)]:
                
                if self.minheap[self.get_left_child_pos(pos)] < self.minheap[self.get_right_child_pos(pos)]:
                    
                    self.swap(pos, self.get_left_child_pos(pos))
                    self.heapify(self.get_left_child_pos(pos))
                
                else:
                    self.swap(pos, self.get_right_child_pos(pos))
                    self.heapify(self.get_right_child_pos(pos))


    def min_heap(self):
        for i in range(self.get_size()//2, -1, -1):
            self.heapify(i)


    def printHeap(self):
        print("The smallest element in the heap is : {}".format(self.minheap[0]))


userHeap = []
def createRandList():
    for _ in range(31):
        userHeap.append(random.randint(1, 101))

createRandList()
minheap = minHeap(userHeap)
minheap.min_heap()
print(userHeap)
minheap.printHeap()