from AdvancedDataStructures.UnionFind import UnionFind


class MinSpanTree:
    def __init__(self) -> None:
        self.weight = 0

    def graph_size(self, graph: list) -> int:
        largest_edge = graph[0][0] if graph[0][0] > graph[0][1] else graph[0][1]
        for i in graph[1:]:
            if i[0] > largest_edge:
                largest_edge = i[0]
            elif i[1] > largest_edge:
                largest_edge = i[1]

        return largest_edge

    def sort_edges(self, graph: list) -> list:
        sorted_graph = sorted(graph, key=lambda x: x[2])
        return sorted_graph

    def add_weight(self, weight: int):
        self.weight += weight

    def get_weight(self) -> int:
        return self.weight

    def unify_edges(self, edge: tuple, uf: UnionFind):
        if not uf.connected(p=edge[0], q=edge[1]):
            uf.unify(p=edge[0], q=edge[1])
            self.add_weight(weight=edge[2])

    def weight_minimum_spanning_tree(self, graph: list) -> int:
        graph_size = self.graph_size(graph=graph) + 1
        sorted_graph = self.sort_edges(graph=graph)

        uf = UnionFind(size=graph_size)

        for i in sorted_graph:
            if uf.components() > 1:
                self.unify_edges(edge=i, uf=uf)

        return self.get_weight()


mst = MinSpanTree()
graph = [
    (0, 1, 1),
    (0, 4, 1),
    (0, 3, 2),
    (3, 4, 2),
    (3, 2, 3),
    (2, 4, 3),
    (2, 1, 4),
    (1, 4, 4),
]
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

wt = mst.weight_minimum_spanning_tree(graph=graph)

print(wt)
