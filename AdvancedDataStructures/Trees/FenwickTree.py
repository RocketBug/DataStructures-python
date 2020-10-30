# Fenwick tree also known as Binary Indexed Tree

# Motivation for the Fenwick tree:
#   Given an array of integer values compute the range sum between index [i, j).

def _lsb(i: int) -> int:
    return i & -i


class FenwickTree:
    tree = []

    def __init__(self, values: list) -> None:
        self.tree = values.copy()

        for i in range(1, len(self.tree)):
            parent = i + _lsb(i=i)
            if parent < len(self.tree):
                self.tree[parent] = self.tree[parent] + self.tree[i]

    # [1, i]
    def prefix_sum(self, i: int) -> int:
        total = 0
        while i != 0:
            total = total + self.tree[i]
            i -= _lsb(i=i)

            # i = i - (i & -i)
            # i = i & ~(i & -i)

        return total

    # [i, j]
    def range_sum(self, i: int, j: int) -> int:
        return self.prefix_sum(j) - self.prefix_sum(i - 1)

    def add(self, i: int, x: int):
        while i < len(self.tree):
            self.tree[i] = self.tree[i] + x
            i = i + _lsb(i=i)

    def print_tree(self):
        print(self.tree)


# This Fenwick Tree implementation works with a 1 based array
values_array = [0, 3, 4, -2, 7, 3, 2, 2, 5, -8, -9, 2, 4, -8]
ft = FenwickTree(values=values_array)
# ft.add(i=4, x=3)
ft.print_tree()
print(ft.prefix_sum(i=5))
print(ft.range_sum(i=1, j=5))
