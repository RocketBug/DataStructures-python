class BinarySearchTree:
    __nodeCount = 0
    root = None

    class _Node:
        def __init__(self, elem: int, left, right) -> None:
            self.data = elem
            self.left = left
            self.right = right

    def size(self) -> int:
        return self.__nodeCount

    def is_empty(self) -> bool:
        return self.size() == 0

    def __contains(self, node, elem) -> bool:
        if node is None:
            return False

        if elem < node.data:
            return self.__contains(node=node.left, elem=elem)

        elif elem > node.data:
            return self.__contains(node=node.right, elem=elem)

        else:
            return True

    def contains(self, elem: int) -> bool:
        return self.__contains(node=self.root, elem=elem)

    def __add(self, node: _Node, elem: int) -> _Node:
        if node is None:
            node = self._Node(elem=elem, left=None, right=None)

        else:
            if elem < node.data:
                node.left = self.__add(node=node.left, elem=elem)

            elif elem > node.data:
                node.right = self.__add(node=node.right, elem=elem)

        return node

    def add(self, elem: int) -> bool:
        if self.contains(elem=elem):
            return False

        else:
            self.root = self.__add(node=self.root, elem=elem)
            self.__nodeCount += 1
            return True

    @staticmethod
    def __dig_left(node: _Node) -> _Node:
        curr = node
        while curr.left is not None:
            curr = curr.left

        return curr

    def __remove(self, node: _Node, elem: int) -> _Node:
        if node is None:
            return None

        if elem < node.data:
            node.left = self.__remove(node=node.left, elem=elem)

        elif elem > node.data:
            node.right = self.__remove(node=node.right, elem=elem)

        else:
            if node.left is None:
                right_child = node.right
                node.data = None
                node = None

                return right_child

            elif node.right is None:
                left_child = node.left
                node.data = None
                node = None

                return left_child

            else:
                tmp = self.__dig_left(node=node.right)
                node.data = tmp.data
                node.right = self.__remove(node=node.right, elem=tmp.data)

        return node

    def remove(self, elem: int):
        if self.contains(elem):
            self.root = self.__remove(node=self.root, elem=elem)

    def preorder_traversal(self, node: _Node):
        if node is not None:
            self.preorder_traversal(node=node.left)
            print(node.data)
            self.preorder_traversal(node=node.right)


bst = BinarySearchTree()
bst.add(elem=8)
bst.add(elem=3)
bst.add(elem=10)
bst.add(elem=1)
bst.add(elem=6)
bst.add(elem=14)
bst.add(elem=4)
bst.add(elem=7)
bst.preorder_traversal(node=bst.root)
bst.remove(elem=6)
bst.preorder_traversal(node=bst.root)
