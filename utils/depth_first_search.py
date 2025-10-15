from utils.search import Search


class DFS(Search):
    def _search(self, node):
        self.marked[node] = True
        for neighbor in self.graph.neighbors(node):
            if not self.marked.get(neighbor, False):
                self.edge_to[neighbor] = node
                self._search(neighbor)
