class UnionFind:
    size = 0
    component_size = []
    component_id = []
    numComponents = 0

    def __init__(self, size) -> None:
        self.size = size
        self.numComponents = size
        for i in range(size):
            self.component_id.append(i)
            self.component_size.append(1)

    def find(self, p: int) -> int:
        root = p
        while root != self.component_id[root]:
            root = self.component_id[root]

        while p != root:
            next_val = self.component_id[p]
            self.component_id[p] = root
            p = next_val

        return root

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def componentSize(self, p: int) -> int:
        root = self.find(p)
        return self.component_size[root]

    def size(self) -> int:
        return self.size

    def components(self) -> int:
        return self.numComponents

    def unify(self, p: int, q: int):
        if self.connected(p, q):
            return

        rootP = self.find(p)
        rootQ = self.find(q)

        if self.component_size[rootP] < self.component_size[rootQ]:
            self.component_size[rootQ] += self.component_size[rootP]
            self.component_id[rootP] = rootQ
        
        else:
            self.component_size[rootP] += self.component_size[rootQ]
            self.component_id[rootQ] = rootP

        self.numComponents -= 1

    def print_arrays(self):
        print(self.component_id)
        print(self.component_size)
        print(self.numComponents)
    
