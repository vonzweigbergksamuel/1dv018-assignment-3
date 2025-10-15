from utils.undirected_graph import UndirectedGraph
from utils.directed_graph import DirectedGraph
from utils.depth_first_search import DFS
from utils.breadth_first_search import BFS


def demo_dfs_search():
    print("\n=== Depth-First Search Demo ===")

    graph = UndirectedGraph()
    nodes = ["A", "B", "C", "D", "E", "F"]
    edges = [
        ("A", "B", 1.0),
        ("A", "C", 1.0),
        ("B", "D", 1.0),
        ("C", "E", 1.0),
        ("D", "F", 1.0),
        ("E", "F", 1.0),
    ]

    for node in nodes:
        graph.add_node(node)
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print("Graph: A-B-D-F, A-C-E-F")
    print("DFS from 'A' (explores deep first):")
    dfs = DFS(graph, "A")

    print("Key paths found:")
    for node in ["B", "C", "F"]:
        if dfs.has_path_to(node):
            path = list(dfs.path_to(node))
            print(f"  A -> {node}: {' -> '.join(path)}")


def demo_bfs_search():
    print("\n=== Breadth-First Search Demo ===")

    graph = UndirectedGraph()
    nodes = ["X", "Y", "Z", "W", "V", "U"]
    edges = [
        ("X", "Y", 1.0),
        ("X", "Z", 1.0),
        ("Y", "W", 1.0),
        ("Z", "V", 1.0),
        ("W", "U", 1.0),
        ("V", "U", 1.0),
    ]

    for node in nodes:
        graph.add_node(node)
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print("Graph: X-Y-W-U, X-Z-V-U")
    print("BFS from 'X' (explores level by level):")
    bfs = BFS(graph, "X")

    print("Key paths found:")
    for node in ["Y", "Z", "U"]:
        if bfs.has_path_to(node):
            path = list(bfs.path_to(node))
            print(f"  X -> {node}: {' -> '.join(path)}")


def demo_dfs_vs_bfs():
    print("\n=== DFS vs BFS Comparison ===")

    graph = UndirectedGraph()
    nodes = ["Start", "A", "B", "C", "Goal"]
    edges = [
        ("Start", "A", 1.0),
        ("Start", "B", 1.0),
        ("A", "C", 1.0),
        ("B", "C", 1.0),
        ("C", "Goal", 1.0),
    ]

    for node in nodes:
        graph.add_node(node)
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print("Graph: Start-A-C-Goal, Start-B-C-Goal")
    print("Finding path from 'Start' to 'Goal':")

    dfs = DFS(graph, "Start")
    bfs = BFS(graph, "Start")

    if dfs.has_path_to("Goal"):
        dfs_path = list(dfs.path_to("Goal"))
        print(f"DFS path: {' -> '.join(dfs_path)} (may be longer)")

    if bfs.has_path_to("Goal"):
        bfs_path = list(bfs.path_to("Goal"))
        print(f"BFS path: {' -> '.join(bfs_path)} (shortest path)")

    print("\nKey difference: BFS finds shortest path, DFS may find longer path")


def demo_directed_graph_search():
    print("\n=== Search in Directed Graph ===")

    graph = DirectedGraph()
    nodes = ["Source", "A", "B", "C", "Target"]
    edges = [
        ("Source", "A", 1.0),
        ("Source", "B", 1.0),
        ("A", "C", 1.0),
        ("B", "C", 1.0),
        ("C", "Target", 1.0),
    ]

    for node in nodes:
        graph.add_node(node)
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print("Directed graph: Source->A->C->Target, Source->B->C->Target")

    dfs = DFS(graph, "Source")
    bfs = BFS(graph, "Source")

    print("Both algorithms find same paths in directed graphs:")
    if dfs.has_path_to("Target"):
        path = list(dfs.path_to("Target"))
        print(f"  Source -> Target: {' -> '.join(path)}")


def demo_search_algorithms():
    demo_dfs_search()
    demo_bfs_search()
    demo_dfs_vs_bfs()
    demo_directed_graph_search()
