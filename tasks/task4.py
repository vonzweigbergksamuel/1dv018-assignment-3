from utils.directed_graph import DirectedGraph
from utils.dijkstras import Dijkstras


def demo_dijkstras_basic():
    print("\n___ Dijkstra's Algorithm: Single Source ___")

    graph = DirectedGraph()
    edges = [
        (0, 1, 5),
        (0, 3, 8),
        (0, 6, 9),
        (1, 2, 15),
        (1, 3, 4),
        (1, 4, 12),
        (2, 7, 9),
        (3, 4, 7),
        (3, 5, 6),
        (4, 2, 3),
        (4, 7, 11),
        (5, 4, 1),
        (5, 7, 13),
        (6, 3, 5),
        (6, 5, 4),
        (6, 7, 20),
    ]

    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print(f"Graph: {graph.num_nodes()} nodes, {graph.num_edges()} edges")
    print("Running Dijkstra's algorithm from node 0:\n")
    dijkstra = Dijkstras(graph, 0)

    print("Shortest distances from node 0 to all nodes:")
    for node in sorted(dijkstra.dist.keys()):
        dist = dijkstra.dist[node]
        if dist == float("inf"):
            print(f"  Node {node}: unreachable")
        else:
            print(f"  Node {node}: {dist}")


def demo_dijkstras_multiple_sources():
    print("\n___ Dijkstra's Algorithm: Multiple Sources ___")

    graph = DirectedGraph()
    edges = [
        (0, 1, 5),
        (0, 3, 8),
        (0, 6, 9),
        (1, 2, 15),
        (1, 3, 4),
        (1, 4, 12),
        (2, 7, 9),
        (3, 4, 7),
        (3, 5, 6),
        (4, 2, 3),
        (4, 7, 11),
        (5, 4, 1),
        (5, 7, 13),
        (6, 3, 5),
        (6, 5, 4),
        (6, 7, 20),
    ]

    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print("Finding shortest paths to node 7 from different starting points:\n")
    for source in [0, 3, 6]:
        dijkstra = Dijkstras(graph, source)
        if dijkstra.dist[7] != float("inf"):
            path = _reconstruct_path(dijkstra, source, 7)
            print(
                f"From {source}: {' → '.join(map(str, path))} (cost: {dijkstra.dist[7]})"
            )
        else:
            print(f"From {source}: unreachable")


def demo_dijkstras_all_pairs():
    print("\n___ Dijkstra's Algorithm: All Shortest Paths ___")

    graph = DirectedGraph()
    edges = [
        (0, 1, 5),
        (0, 3, 8),
        (0, 6, 9),
        (1, 2, 15),
        (1, 3, 4),
        (1, 4, 12),
        (2, 7, 9),
        (3, 4, 7),
        (3, 5, 6),
        (4, 2, 3),
        (4, 7, 11),
        (5, 4, 1),
        (5, 7, 13),
        (6, 3, 5),
        (6, 5, 4),
        (6, 7, 20),
    ]

    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print("Shortest distances from all nodes to node 7:\n")
    for source in sorted(graph._adjacency.keys()):
        dijkstra = Dijkstras(graph, source)
        dist = dijkstra.dist[7]
        if dist == float("inf"):
            print(f"From {source}: ∞ (unreachable)")
        else:
            print(f"From {source}: {dist}")


def _reconstruct_path(dijkstra, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = dijkstra.prev[current]
    path.reverse()
    return path if path and path[0] == start else []


def demo_dijkstras_algorithms():
    demo_dijkstras_basic()
    demo_dijkstras_multiple_sources()
    demo_dijkstras_all_pairs()
