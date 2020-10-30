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

    def __init__(self, capacity: int, load_factor: float):
        self.capacity = max(capacity, self.DEFAULT_CAPACITY)
        self.maxLoadFactor = max(load_factor, self.DEFAULT_LOAD_FACTOR)

        for i in range(self.capacity):
            self.table.append(None)

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def normalize_index(self, keyhash: int) -> int:
        return (keyhash & 0x7FFFFFFF) % self.capacity

    def clear(self):
        self.table = []
        self.size = 0

    def __bucket_seek_entry(self, bucket_index: int, key: int):
        if key is None:
            return None

        bucket = self.table[bucket_index]
        if bucket is None:
            return None

        for entry in bucket:
            if entry.key == key:
                return entry

        return None

    def __bucket_insert_entry(self, bucket_index: int, entry: Entry):
        bucket = self.table[bucket_index]
        if bucket is None:
            bucket = deque()
            bucket.append(entry)
            self.table[bucket_index] = bucket

        else:
            existent_entry = self.__bucket_seek_entry(bucket_index=bucket_index, key=entry.key)
            if existent_entry is None:
                bucket.append(entry)

            else:
                return None

        self.size = self.size + 1

    def __bucket_remove_entry(self, bucket_index: int, key: int):
        bucket = self.table[bucket_index]
        for entry in bucket:
            if entry.key == key:
                bucket.remove(entry)
                self.size -= 1
                return

    def insert(self, key: int, value: str):
        new_entry = Entry(key=key, value=value)
        bucket_index = self.normalize_index(keyhash=hash(key))
        self.__bucket_insert_entry(bucket_index=bucket_index, entry=new_entry)

    def get(self, key: int):
        bucket_index = self.normalize_index(keyhash=hash(key))
        return self.__bucket_seek_entry(bucket_index=bucket_index, key=key)

    def remove(self, key: int):
        bucket_index = self.normalize_index(keyhash=hash(key))
        self.__bucket_remove_entry(bucket_index=bucket_index, key=key)

    def print_table(self):
        for i in range(self.capacity):
            bucket = self.table[i]
            for entry in bucket:
                print(entry.value)

            print()


ht = HashTableSeparateChaining(capacity=5, load_factor=0.75)

ht.insert(key=1, value='kevin')
ht.insert(key=2, value='matthew')
ht.insert(key=3, value='mark')
ht.insert(key=4, value='luke')
ht.insert(key=5, value='john')
ht.insert(key=6, value='paul')

ht.print_table()

ht.remove(key=1)

ht.print_table()
