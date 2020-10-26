class Entry:

    def __init__(self, key:int, value:str):
        self.key = key
        self.value = value
        self.hashKey = hash(key)

    
class HashTableDoubleHashing:
    size = 0
    hashTable = []
    defaultSize = 7
    DEFAULT_LOADFACTOR = 0.71

    def __init__(self):
        self.hashTable = [None for i in range(self.defaultSize)]

    def __getSize(self) -> int:
        return self.size

    def __addSize(self):
        self.size += 1

    def __getThreshold(self) -> int:
        return round(self.DEFAULT_LOADFACTOR * self.defaultSize) 

    def __probing(self, key:int, x:int) -> int:
        delta = x * hash(key)
        return delta

    def __isFree(self, index:int) -> bool:
        return False if self.hashTable[index] != None else True

    def __openAddress(self, entry:Entry) -> int:
        hashkey = entry.hashKey
        for i in range(self.defaultSize):
            index = (hashkey + self.__probing(key=entry.key, x=i)) % self.defaultSize
            if self.__isFree(index=index):
                return index

    def __isPrime(self, x:int) -> int:
        flag = False
        for i in range(2, x//2):
            if x % i == 0:
                flag = False
                return flag

        flag = True
        return flag


    def __increaseDefaultSize(self):
        x = self.defaultSize + 1
        
        while not self.__isPrime(x=x):
            x += 1

        self.defaultSize = x


    def __resize(self):
        self.__increaseDefaultSize()

        tempHashTable = self.hashTable.copy()
        self.hashTable = [None for i in range(self.defaultSize)]
        for e in tempHashTable:
            if e:
                openAddress = self.__openAddress(entry=e)
                self.hashTable[openAddress] = e

        tempHashTable.clear()
        

    def insert(self, key:int, value:str):
        newEntry = Entry(key=key, value=value)
        openAddress = self.__openAddress(entry=newEntry)
        self.hashTable[openAddress] = newEntry
        self.__addSize()

        if self.__getSize() >= self.__getThreshold():
            self.__resize()

    def printHashTable(self):
        for e,j in enumerate(self.hashTable):
            if j:
                print(e, j.value)

            else:
                print(e, j)


ht = HashTableDoubleHashing()
ht.insert(key=100, value='kevin')
ht.insert(key=101, value='kevin')
ht.insert(key=102, value='kevin')
ht.insert(key=103, value='kevin')
ht.insert(key=104, value='kevin')

ht.printHashTable()
