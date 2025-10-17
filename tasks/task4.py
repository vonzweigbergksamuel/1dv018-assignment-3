from utils.directed_graph import DirectedGraph
from utils.dijkstras import Dijkstras


def demo_dijkstras_basic():
    print("\n=== Dijkstra's Algorithm Demo ===")

    # Create directed graph with weighted edges
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

    print(f"Graph created with {graph.num_nodes()} nodes and {graph.num_edges()} edges")
    print("Sample edges: 0->1(5), 0->3(8), 1->3(4), etc.")

    print("\nRunning Dijkstra's from node 0:")
    dijkstra = Dijkstras(graph, 0)

    print("\nShortest distances from node 0:")
    for node in sorted(dijkstra.dist.keys()):
        dist = dijkstra.dist[node]
        if dist == float("inf"):
            print(f"  Node {node}: unreachable")
        else:
            print(f"  Node {node}: {dist}")

    print("\nShortest paths:")
    target_nodes = [7, 4, 5]
    for target in target_nodes:
        if dijkstra.dist[target] != float("inf"):
            path = _reconstruct_path(dijkstra, 0, target)
            print(
                f"  0 -> {target}: {' -> '.join(map(str, path))} (cost: {dijkstra.dist[target]})"
            )


def demo_dijkstras_multiple_sources():
    print("\n=== Dijkstra's from Different Sources ===")

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

    sources = [0, 3, 6]
    target = 7

    print(f"Finding shortest paths to node {target} from different sources:")
    for source in sources:
        dijkstra = Dijkstras(graph, source)
        if dijkstra.dist[target] != float("inf"):
            path = _reconstruct_path(dijkstra, source, target)
            print(
                f"  From {source}: {' -> '.join(map(str, path))} (cost: {dijkstra.dist[target]})"
            )
        else:
            print(f"  From {source}: unreachable")


def demo_dijkstras_all_pairs():
    print("\n=== Dijkstra's All Shortest Paths ===")

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

    print("Distance matrix (distances from each node):")
    all_distances = {}

    for source in sorted(graph._adjacency.keys()):
        dijkstra = Dijkstras(graph, source)
        all_distances[source] = dijkstra.dist

    # Show distances to node 7 from all sources
    print("Distances to node 7 from all nodes:")
    for source in sorted(all_distances.keys()):
        dist = all_distances[source][7]
        if dist == float("inf"):
            print(f"  From {source}: ∞ (unreachable)")
        else:
            print(f"  From {source}: {dist}")


def _reconstruct_path(dijkstra, start, end):
    """Reconstruct path from start to end using prev pointers."""
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = dijkstra.prev[current]

    path.reverse()
    return path if path[0] == start else []


def demo_dijkstras_algorithms():
    demo_dijkstras_basic()
    demo_dijkstras_multiple_sources()
    demo_dijkstras_all_pairs()
