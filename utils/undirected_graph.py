from utils.graph import Graph


class UndirectedGraph(Graph):
    def add_edge(self, u, v, weight=1.0):
        self.add_node(u)
        self.add_node(v)
        self._adjacency[u][v] = weight
        self._adjacency[v][u] = weight

    def add_edge_default(self, u, v):
        self.add_edge(u, v, 1.0)

    def remove_edge(self, u, v):
        if v in self._adjacency.get(u, {}):
            del self._adjacency[u][v]
        if u in self._adjacency.get(v, {}):
            del self._adjacency[v][u]

    def num_edges(self):
        return sum(len(neighbors) for neighbors in self._adjacency.values()) // 2
