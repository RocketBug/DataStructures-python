#Fenwick tree also known as Binary Indexed Tree

#Motivation for the Fenwick tree:
#   Given an array of integer values comput the range sum between index [i, j). 

class FenwickTree:
    tree = []

    def __lsb(self, i: int) -> int:
        return i & -i

    def __init__(self, values: list) -> None:
        self.tree = values.copy()

        for i in range(1, len(self.tree)):
            parent = i + self.__lsb(i=i)
            if parent < len(self.tree):
                self.tree[parent] = self.tree[parent] + self.tree[i]

    # [1, i]
    def prefixSum(self, i:int) -> int:
        total = 0
        while i != 0:
            total = total + self.tree[i]
            i -= self.__lsb(i=i)

            # i = i - (i & -i)
            # i = i & ~(i & -i)

        return total

    # [i, j]
    def rangeSum(self, i:int, j:int) -> int:
        return self.prefixSum(j) - self.prefixSum(i-1)

    def add(self, i:int, x:int):
        while i<len(self.tree):
            self.tree[i] = self.tree[i] + x
            i = i + self.__lsb(i=i)


    def printTree(self):
        print(self.tree)

# This Fenwick Tree implementation works with a 1 based array
values = [0,3,4,-2,7,3,2,2,5,-8,-9,2,4,-8]
ft = FenwickTree(values=values)
#ft.add(i=4, x=3)
ft.printTree()
print(ft.prefixSum(i=5))
print(ft.rangeSum(i=1, j=5))

