class Node:
    def __init__(self):
        self.next  = None
        self.data = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data
    
    def setNext(self, newNode):
        self.next = newNode

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        node = Node()
        node.setData(data)
        node.setNext(self.head)
        self.head = node
    
    def printLinkedList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()


sll = LinkedList()
sll.addNode(10)
sll.addNode(20)
sll.addNode(30)
print(sll.head.data)
sll.printLinkedList()


        
