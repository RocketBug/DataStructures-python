class UnionFind:
    __size = 0
    __component_size = []
    __component_id = []
    __numComponents = 0

    def __init__(self, size) -> None:
        self.__size = size
        self.__numComponents = size
        for i in range(size):
            self.__component_id.append(i)
            self.__component_size.append(1)

    def __find(self, p: int) -> int:
        root = p
        while root != self.__component_id[root]:
            root = self.__component_id[root]

        while p != root:
            next_val = self.__component_id[p]
            self.__component_id[p] = root
            p = next_val

        return root

    def __get_component_size(self, p: int) -> int:
        root = self.__find(p)
        return self.__component_size[root]

    def __get_size(self) -> int:
        return self.__size

    def connected(self, p: int, q: int) -> bool:
        return self.__find(p) == self.__find(q)

    def components(self) -> int:
        return self.__numComponents

    def unify(self, p: int, q: int):
        if self.connected(p, q):
            return

        root_p = self.__find(p)
        root_q = self.__find(q)

        if self.__component_size[root_p] < self.__component_size[root_q]:
            self.__component_size[root_q] += self.__component_size[root_p]
            self.__component_id[root_p] = root_q
        
        else:
            self.__component_size[root_p] += self.__component_size[root_q]
            self.__component_id[root_q] = root_p

        self.__numComponents -= 1

    def print_arrays(self):
        print(self.__component_id)
        print(self.__component_size)
        print(self.__numComponents)
