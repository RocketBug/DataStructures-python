from AdvancedDataStructures.UnionFind import UnionFind


def _get_graph_size(graph: list) -> int:
    largest_edge = graph[0][0] if graph[0][0] > graph[0][1] else graph[0][1]
    for i in graph[1:]:
        if i[0] > largest_edge:
            largest_edge = i[0]
        elif i[1] > largest_edge:
            largest_edge = i[1]

    return largest_edge


def _sort_edges(graph: list) -> list:
    sorted_graph = sorted(graph, key=lambda x: x[2])
    return sorted_graph


class MinSpanTree:
    __weight = 0

    def __init__(self) -> None:
        self.__weight = 0

    def __add_weight(self, weight: int):
        self.__weight += weight

    def __get_weight(self) -> int:
        return self.__weight

    def __unify_edges(self, edge: tuple, uf: UnionFind):
        if not uf.connected(p=edge[0], q=edge[1]):
            uf.unify(p=edge[0], q=edge[1])
            self.__add_weight(weight=edge[2])

    def weight_minimum_spanning_tree(self, graph: list) -> int:

        graph_size = _get_graph_size(graph=graph) + 1
        sorted_graph = _sort_edges(graph=graph)

        uf = UnionFind(size=graph_size)

        for i in sorted_graph:
            if uf.components() > 1:
                self.__unify_edges(edge=i, uf=uf)

        return self.__get_weight()


mst = MinSpanTree()
mst_graph = [
    (0, 1, 1),
    (0, 4, 1),
    (0, 3, 2),
    (3, 4, 2),
    (3, 2, 3),
    (2, 4, 3),
    (2, 1, 4),
    (1, 4, 4),
]
wt = mst.weight_minimum_spanning_tree(graph=mst_graph)
print(wt)


# graph = [
#     (0, 1, 5),
#     (0, 3, 4),
#     (0, 4, 1),
#     (1, 3, 2),
#     (1, 2, 4),
#     (2, 7, 4),
#     (2, 8, 1),
#     (2, 9, 2),
#     (3, 4, 2),
#     (3, 5, 5),
#     (3, 6, 11),
#     (3, 7, 2),
#     (4, 5, 1),
#     (5, 6, 7),
#     (6, 7, 1),
#     (6, 8, 4),
#     (7, 8, 6),
#     (8, 9, 0),
# ]
