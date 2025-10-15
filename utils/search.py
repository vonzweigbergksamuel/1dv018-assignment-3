from utils.graph import Graph


class Search:
    def __init__(self, graph: Graph, start):
        self.graph = graph
        self.start = start
        self.marked = {}
        self.edge_to = {}

        self._search(start)

    def _search(self, node):
        return NotImplementedError

    def has_path_to(self, node):
        return self.marked.get(node, False)

    def path_to(self, node):
        if not self.has_path_to(node):
            return None

        path = []
        current = node
        while current != self.start:
            path.append(current)
            current = self.edge_to[current]

        path.append(self.start)
        path.reverse()

        return iter(path)
