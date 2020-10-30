class Entry:

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        self.hashkey = hash(key)


class HashTableDoubleHashing:
    size = 0
    hashtable = []
    defaultSize = 7
    DEFAULT_LOADFACTOR = 0.71

    def __init__(self):
        self.hashtable = [None for _ in range(self.defaultSize)]

    @staticmethod
    def __probing(key: int, x: int) -> int:
        delta = x * hash(key)
        return delta

    @staticmethod
    def __is_prime(x: int) -> int:
        flag = False
        for i in range(2, x // 2):
            if x % i == 0:
                flag = False
                return flag

        flag = True
        return flag

    def __get_size(self) -> int:
        return self.size

    def __adds_size(self):
        self.size += 1

    def __get_threshold(self) -> int:
        return round(self.DEFAULT_LOADFACTOR * self.defaultSize)

    def __is_free(self, index: int) -> bool:
        return False if self.hashtable[index] is not None else True

    def __get_index(self, key: int, x: int) -> int:
        return (hash(key) + self.__probing(key=key, x=x)) % self.defaultSize

    def __open_address(self, entry: Entry) -> int:
        for i in range(self.defaultSize):
            index = self.__get_index(key=entry.key, x=i)
            if self.__is_free(index=index):
                return index

    def __increase_default_size(self):
        x = self.defaultSize + 1

        while not self.__is_prime(x=x):
            x += 1

        self.defaultSize = x

    def __resize(self):
        self.__increase_default_size()

        temp_hashtable = self.hashtable.copy()
        self.hashtable = [None for _ in range(self.defaultSize)]
        for e in temp_hashtable:
            if e:
                open_address = self.__open_address(entry=e)
                self.hashtable[open_address] = e

        temp_hashtable.clear()

    def insert(self, key: int, value: str):
        new_entry = Entry(key=key, value=value)
        open_address = self.__open_address(entry=new_entry)
        self.hashtable[open_address] = new_entry
        self.__adds_size()

        if self.__get_size() >= self.__get_threshold():
            self.__resize()

    def __get_entry(self, index: int) -> Entry:
        return self.hashtable[index]

    def __get(self, key: int) -> Entry:
        x = 0
        index = self.__get_index(key=key, x=x)
        while self.__get_entry(index=index).key != key:
            x += 1
            index = self.__get_index(key=key, x=x)

        return self.__get_entry(index=index)

    def get_entry(self, key: int) -> Entry:
        return self.__get(key=key)

    def get_value(self, key: int) -> str:
        return self.__get(key=key).value

    def update_value(self, key: int, value: str):
        entry = self.get_entry(key=key)
        entry.value = value

    def print_hash_table(self):
        for e, j in enumerate(self.hashtable):
            if j:
                print(e, j.value)

            else:
                print(e, j)


ht = HashTableDoubleHashing()
ht.insert(key=100, value='kevin')
ht.insert(key=101, value='matt')
ht.insert(key=102, value='mark')
ht.insert(key=103, value='luke')
ht.insert(key=104, value='john')

ht.print_hash_table()

print(ht.get_value(key=101))
