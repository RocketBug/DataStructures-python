class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

    def insertNode(self, data):
        if self.key:
            if data < self.key:
                if self.left == None:
                    node = Node(data)
                    self.left = node
                else:
                    self.left.insertNode(data)
                
            else:
                if self.right == None:
                    node = Node(data)
                    self.right = node
                else:
                    self.right.insertNode(data)
        
        else:
            self.key = data

    def printPreOrder(self):
        if self:
            print(self.key)
            Node.printPreOrder(self.left)
            Node.printPreOrder(self.right)

    def printInOrder(self):
        if self:
            Node.printInOrder(self.left)
            print(self.key)
            Node.printInOrder(self.right)

    def printPostOrder(self):
        if self:
            Node.printPostOrder(self.left)
            Node.printPostOrder(self.right)
            print(self.key)




rootNode = Node('t')
rootNode.insertNode('b')
rootNode.insertNode('b')
rootNode.insertNode('c')
rootNode.insertNode('s')
rootNode.insertNode('d')

print("Pre")
rootNode.printPreOrder()
print("In")
rootNode.printInOrder()
print("Post")
rootNode.printPostOrder()