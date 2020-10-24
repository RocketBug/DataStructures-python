class Entry:
    key = int
    value = str
    hashKey = int
    
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        self.hashKey = hash(key)

class HashTableLinearProbing:
    size = 0
    DEFAULT_CAPACITY = 12
    MAX_LOAD_FACTOR = 0.667
    
    hashTable = []
    
    def __init__(self):
        for i in range(self.DEFAULT_CAPACITY):
            self.hashTable.append(None)

    def __getSize(self) -> int:
        return self.size

    def __addSize(self):
        self.size += 1

    def __getThreshold(self) -> float:
        return round(self.DEFAULT_CAPACITY * self.MAX_LOAD_FACTOR)
    
    def __probing(self, x: int) -> int:
        a = 1
        return a*x 

    def __lookup(self, index: int) -> Entry:
        return self.hashTable[index]

    def bucketIndex(self, key: int) -> int:
        for i in range(self.DEFAULT_CAPACITY) :
            index = (hash(key) + self.__probing(x=i)) % self.DEFAULT_CAPACITY
            if self.__lookup(index=index) == None:
                return index

    def __increaseSize(self):
        self.hashTable = []
        for i in range(self.DEFAULT_CAPACITY):
            self.hashTable.append(None)

    def __resize(self):
        self.DEFAULT_CAPACITY = self.DEFAULT_CAPACITY * 2
        hashTableCopy = list.copy(self.hashTable)
        self.__increaseSize()
        for entry in hashTableCopy:
            if entry:
                index = self.bucketIndex(key=entry.key)
                self.hashTable[index] = entry
            

    def insert(self, key: int, value: str):
        newEntry = Entry(key=key, value=value)
        index = self.bucketIndex(key=newEntry.key)
        self.hashTable[index] = newEntry
        self.__addSize()

        if self.__getSize() >= self.__getThreshold(): 
            self.__resize()
            

    def printHashTable(self):
        for i,j in enumerate(self.hashTable):
            print(i,j)

        print('size = {}'.format(self.__getSize()))


ht = HashTableLinearProbing()
ht.insert(key=0, value='kevin')
ht.insert(key=1, value='matt')
ht.insert(key=2, value='mark')
ht.insert(key=3, value='luke')
ht.insert(key=4, value='john')
ht.insert(key=5, value='peter')
ht.insert(key=6, value='paul')
ht.insert(key=1, value='bob')

entry = ht.get(key=2, value='mark')
print(entry.value)

