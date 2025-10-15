from collections import deque
from utils.search import Search


class BFS(Search):
    def _search(self, node):
        queue = deque([node])
        self.marked[node] = True

        while queue:
            v = queue.popleft()
            for neighbor in self.graph.neighbors(v):
                if not self.marked.get(neighbor, False):
                    self.marked[neighbor] = True
                    self.edge_to[neighbor] = v
                    queue.append(neighbor)
