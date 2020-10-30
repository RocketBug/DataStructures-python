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

    def __get_size(self) -> int:
        return self.size

    def __add_size(self):
        self.size += 1

    def __get_threshold(self) -> int:
        return round(self.DEFAULT_LOADFACTOR * self.defaultSize)

    @staticmethod
    def __probing(x: int) -> int:
        return ((x ** 2) + x) // 2

    def __is_free(self, index: int) -> bool:
        return False if self.hashTable[index] is not None else True

    def __open_address(self, entry: Entry) -> int:
        hashkey = entry.hashKey
        for i in range(self.defaultSize):
            index = (hashkey + self.__probing(x=i)) % self.defaultSize
            if self.__is_free(index=index):
                return index

    def __add_power(self):
        self.power += 1

    def __get_power(self) -> int:
        return self.power

    def __increase_deafult_size(self):
        self.defaultSize = 2 ** self.__get_power()

    def __resize(self):
        self.__add_power()
        self.__increase_deafult_size()

        temp_hashtable = self.hashTable.copy()
        self.hashTable = [None for _ in range(2 ** self.__get_power())]

        for e in temp_hashtable:
            if e:
                open_address = self.__open_address(entry=e)
                self.hashTable[open_address] = e

        temp_hashtable.clear()

    def insert(self, key: int, value: str):
        new_entry = Entry(key=key, value=value)
        open_address = self.__open_address(entry=new_entry)
        self.hashTable[open_address] = new_entry
        self.__add_size()

        if self.__get_size() >= self.__get_threshold():
            self.__resize()

    def __get_entry(self, index: int) -> Entry:
        return self.hashTable[index]

    def __get(self, key: int) -> Entry:
        keyhash = hash(key)

        x = 0
        index = (keyhash + self.__probing(x=x)) % self.defaultSize

        while self.__get_entry(index=index).key != key:
            x += 1
            index = (keyhash + self.__probing(x=x)) % self.defaultSize

        return self.__get_entry(index=index)

    def get_entry(self, key: int) -> Entry:
        return self.__get(key=key)

    def get_value(self, key: int) -> str:
        return self.__get(key=key).value

    def update_value(self, key: int, value: str):
        entry = self.get_entry(key=key)
        entry.value = value

    def print_hashtable(self):
        for e, j in enumerate(self.hashTable):
            if j:
                print(e, j.value)

            else:
                print(e, j)


ht = HashTableQuadraticProbing()

ht.insert(key=0, value='kevin')
ht.insert(key=1, value='matt')
ht.insert(key=2, value='mark')
ht.update_value(key=2, value='john')
ht.insert(key=3, value='james')
ht.print_hashtable()
