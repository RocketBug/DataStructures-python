class Entry:

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        self.hashKey = hash(key)


class HashTableQuadraticProbing:
    power = 3
    size = 0
    hashTable = []
    defaultSize = 8
    DEFAULT_LOADFACTOR = 0.5

    def __init__(self):
        self.hashTable = [None for i in range(self.defaultSize)]

    def __getSize(self) -> int:
        return self.size

    def __addSize(self):
        self.size += 1

    def __getThreshold(self) -> int:
        return self.DEFAULT_LOADFACTOR * self.defaultSize 

    def __probing(self, x:int) -> int:
        return ((x**2)+x) // 2

    def __isFree(self, index:int) -> bool:
        return False if self.hashTable[index] != None else True

    def __openAddress(self, entry:Entry) -> int:
        hashkey = entry.hashKey
        for i in range(self.defaultSize):
            index = (hashkey + self.__probing(x=i)) % self.defaultSize
            if self.__isFree(index=index):
                return index

    def __addPower(self):
        self.power += 1
    
    def __getPower(self) -> int:
        return self.power

    def __increaseDefaultSize(self):
        self.defaultSize = 2**self.__getPower()

    def __resize(self):
        self.__addPower()
        self.__increaseDefaultSize()

        tempHashTable = self.hashTable.copy()
        self.hashTable = [None for i in range(2**self.__getPower())]

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

    def __getEntry(self, index:int) -> Entry:
        return self.hashTable[index]

    def __get(self, key:int) -> Entry:
        keyHash = hash(key)
        
        x = 0
        index = (keyHash + self.__probing(x=x)) % self.defaultSize
        
        while self.__getEntry(index=index).key != key:
            x += 1
            index = (keyHash + self.__probing(x=x)) % self.defaultSize
        
        return self.__getEntry(index=index)

    def getEntry(self, key:int) -> Entry:
        return self.__get(key=key)

    def getValue(self, key:int) -> str:
        return self.__get(key=key).value

    def updateValue(self, key:int, value:str):
        entry = self.getEntry(key=key)
        entry.value = value

    def printHashTable(self):
        for e,j in enumerate(self.hashTable):
            if j:
                print(e, j.value)

            else:
                print(e, j)

ht = HashTableQuadraticProbing()

ht.insert(key=0, value='kevin')
ht.insert(key=1, value='matt')
ht.insert(key=2, value='mark')
ht.updateValue(key=2, value='john')
ht.insert(key=3, value='james')
ht.printHashTable()



