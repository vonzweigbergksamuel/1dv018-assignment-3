class Graph:
    def __init__(self) -> None:
        self._adjacency = {}

    def add_node(self, node):
        if node not in self._adjacency:
            self._adjacency[node] = {}

    def num_nodes(self):
        return len(self._adjacency)

    def num_edges(self):
        raise NotImplementedError

    def degree(self, node):
        return len(self._adjacency.get(node, {}))

    def nodes(self):
        return iter(self._adjacency.keys())

    def edges(self):
        for u in self._adjacency:
            for v, w in self._adjacency[u].items():
                yield (u, v, w)

    def neighbors(self, node):
        return iter(self._adjacency.get(node, {}).keys())
