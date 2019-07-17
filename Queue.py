class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        print(self.items)



def hotPotato(names, num):
    qu = Queue()
    for i in names:
        qu.printQueue()
        qu.enqueue(i)

    qu.printQueue()
    while qu.size() > 1:
        qu.printQueue()
        for i in range(num):
            qu.enqueue(qu.dequeue())

        qu.dequeue()
    return qu.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 3))
