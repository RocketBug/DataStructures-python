from collections import deque
class Entry:
    hash_key = int
    key = int
    value = str

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        self.hash_key = hash(key)

    def equals(self, other) -> bool:
        if self.hash_key != other.hash_key:
            return False

        else:
            return True

class HashTableSeparateChaining:
    DEFAULT_CAPACITY = 3
    DEFAULT_LOAD_FACTOR = 0.75

    maxLoadFactor = float
    capacity, threshold, size = 0, 0, 0
    table = []

    def __init__(self, capacity: int, loadFactor: int):
        self.capacity = max(capacity, self.DEFAULT_CAPACITY)
        self.maxLoadFactor = max(loadFactor, self.DEFAULT_LOAD_FACTOR)

        for i in range(self.capacity):
            self.table.append(None)

    
    def get_size(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def normalizeIndex(self, keyHash: int) -> int:
        return (keyHash & 0x7FFFFFFF) % self.capacity

    def clear(self):
        self.table = []
        self.size = 0

    def __bucketSeekEntry(self, bucketIndex: int, key: int):
        if key == None:
            return None

        bucket = self.table[bucketIndex]
        if bucket == None:
            return None

        for entry in bucket:
            if entry.key == key:
                return entry

        return None

    def __bucketInsertEntry(self, bucketIndex:int, entry: Entry):
        bucket = self.table[bucketIndex]
        if bucket == None:
            bucket = deque()
            bucket.append(entry)
            self.table[bucketIndex] = bucket

        else:
            existentEntry = self.__bucketSeekEntry(bucketIndex=bucketIndex, key=entry.key)
            if existentEntry == None:
                bucket.append(entry)

            else:
                return None

        self.size = self.size + 1

    def __bucketRemoveEntry(self, bucketIndex: int, key: int):
        bucket = self.table[bucketIndex]
        for entry in bucket:
            if entry.key == key:
                bucket.remove(entry)
                self.size -= 1
                return 

    def insert(self, key: int, value: str):
        newEntry = Entry(key=key, value=value)
        bucketIndex = self.normalizeIndex(keyHash=hash(key))
        self.__bucketInsertEntry(bucketIndex=bucketIndex, entry=newEntry)

    def get(self, key: int):
        bucketIndex = self.normalizeIndex(keyHash=hash(key))
        return self.__bucketSeekEntry(bucketIndex= bucketIndex, key= key)

    def remove(self, key: int):
        bucketIndex = self.normalizeIndex(keyHash=hash(key))
        self.__bucketRemoveEntry(bucketIndex=bucketIndex, key=key)


    def print_table(self):
        for i in range(self.capacity):
            bucket = self.table[i]
            for entry in bucket:
                print(entry.value)
            
            print()

ht = HashTableSeparateChaining(capacity=5, loadFactor=0.75)

ht.insert(key=1, value='kevin')
ht.insert(key=2, value='matthew')
ht.insert(key=3, value='mark')
ht.insert(key=4, value='luke')
ht.insert(key=5, value='john')
ht.insert(key=6, value='paul')

ht.print_table()

ht.remove(key=1)

ht.print_table()