class Entry:
    key = int
    value = str
    hashKey = int

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        self.hashKey = hash(key)


class HashTableLinearProbing:
    __size = 0
    DEFAULT_CAPACITY = 12
    MAX_LOAD_FACTOR = 0.667

    __hashTable = []

    def __init__(self):
        for i in range(self.DEFAULT_CAPACITY):
            self.__hashTable.append(None)

    def __get_size(self) -> int:
        return self.__size

    def __add_size(self):
        self.__size += 1

    def __get_threshold(self) -> float:
        return round(self.DEFAULT_CAPACITY * self.MAX_LOAD_FACTOR)

    @staticmethod
    def __probing(x: int) -> int:
        a = 1
        return a * x

    def __lookup(self, index: int) -> Entry:
        return self.__hashTable[index]

    def __key_index(self, key: int, x: int) -> int:
        index = (hash(key) + self.__probing(x=x)) % self.DEFAULT_CAPACITY
        return index

    def __free_index(self, key: int) -> int:
        for i in range(self.DEFAULT_CAPACITY):
            index = (hash(key) + self.__probing(x=i)) % self.DEFAULT_CAPACITY
            if self.__lookup(index=index) is None:
                return index

    def __increase_size(self):
        self.__hashTable = [None for _ in range(self.DEFAULT_CAPACITY)]

    def __resize(self):
        self.DEFAULT_CAPACITY = self.DEFAULT_CAPACITY * 2
        hashtable_copy = list.copy(self.__hashTable)
        self.__increase_size()
        for entry in hashtable_copy:
            if entry:
                index = self.__free_index(key=entry.key)
                self.__hashTable[index] = entry

    def insert(self, key: int, value: str):
        new_entry = Entry(key=key, value=value)
        index = self.__free_index(key=new_entry.key)
        self.__hashTable[index] = new_entry
        self.__add_size()

        if self.__get_size() >= self.__get_threshold():
            self.__resize()

    def __get(self, key: int, x: int) -> Entry:
        index = self.__key_index(key=key, x=x)
        entry = self.__lookup(index=index)
        return entry

    def get(self, key: int, value: str) -> Entry:
        x = 0
        entry = self.__get(key=key, x=x)

        while entry.value != value:
            x += 1
            entry = self.__get(key=key, x=x)

        return entry

    def print_hashtable(self):
        for i, j in enumerate(self.__hashTable):
            print(i, j)

        print('size = {}'.format(self.__get_size()))


ht = HashTableLinearProbing()
ht.insert(key=0, value='kevin')
ht.insert(key=1, value='matt')
ht.insert(key=2, value='mark')
ht.insert(key=3, value='luke')
ht.insert(key=4, value='john')
ht.insert(key=5, value='peter')
ht.insert(key=6, value='paul')
ht.insert(key=1, value='bob')

entry_obj = ht.get(key=1, value='matt')
print(entry_obj.value)

ht.print_hashtable()
