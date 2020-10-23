import heapq

class Tree:
    def node(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def printCode(self, root, s):

        if root == None:
            return

        if root[2]:
            
            if root[2].key != '$':
                print("key : {}, value : {}, code : {}".format(root[2].key, root[2].value, s))
            
            self.printCode(root[2].left, s+"0")
            self.printCode(root[2].right, s+"1")
                

    def createTree(self, keysList, valueslist):
        pQueue = []
        rootNode = None
        for i in range(0, len(keysList)):
            node = Tree()
            node.value = valueslist[i]
            node.key = keysList[i]
            node.left = None
            node.right = None
            heapq.heappush(pQueue, [node.value, node.key, node])

        while len(pQueue) > 1:
            x = heapq.heappop(pQueue)
            y = heapq.heappop(pQueue)
            f = Tree()
            f.node('$', (x[0] + y[0]))
            f.left = x
            f.right = y
            rootNode = [f.value, f.key, f]
            heapq.heappush(pQueue, [f.value, f.key, f])
        
        self.printCode(rootNode, "")


value = [5, 9, 12, 13, 16, 45]
keys = ['a', 'b', 'c', 'd', 'e', 'f']
huff = Tree()
huff.createTree(keys, value)