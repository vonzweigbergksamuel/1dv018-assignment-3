from utils.graph import Graph


class DirectedGraph(Graph):
    def add_edge(self, u, v, weight=1.0):
        self.add_node(u)
        self.add_node(v)
        self._adjacency[u][v] = weight

    def add_edge_default(self, u, v):
        self.add_edge(u, v, 1.0)

    def remove_edge(self, u, v):
        if v in self._adjacency.get(u, {}):
            del self._adjacency[u][v]

    def num_edges(self):
        return sum(len(neighbors) for neighbors in self._adjacency.values())
