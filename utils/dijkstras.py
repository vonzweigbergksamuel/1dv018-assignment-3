import heapq
from utils.graph import Graph


class Dijkstras:
    def __init__(self, graph: Graph, start) -> None:
        self.graph = graph
        self.dist = {node: float("inf") for node in graph._adjacency}
        self.prev = {node: None for node in graph._adjacency}
        self.dist[start] = 0

        self.priority_queue = [(0, start)]
        self._step()

    def _step(self):
        while self.priority_queue:
            current_dist, node = heapq.heappop(self.priority_queue)

            if current_dist > self.dist[node]:
                continue

            for neighbor, weight in self.graph._adjacency[node].items():
                new_dist = current_dist + weight

                if new_dist < self.dist[neighbor]:
                    self.dist[neighbor] = new_dist
                    self.prev[neighbor] = node
                    heapq.heappush(self.priority_queue, (new_dist, neighbor))
