from utils.undirected_graph import UndirectedGraph
from utils.directed_graph import DirectedGraph
from utils.depth_first_search import DFS
from utils.breadth_first_search import BFS


def demo_dfs_search():
    print("\n___ Depth-First Search ___")

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

    print(
        "Graph structure: A connects to B,C; B connects to D; C connects to E; D,E connect to F"
    )
    print("Starting DFS from node A:")
    dfs = DFS(graph, "A")

    print("Paths discovered by DFS:")
    for node in ["B", "C", "F"]:
        if dfs.has_path_to(node):
            path = list(dfs.path_to(node))
            print(f"  A → {node}: {' → '.join(path)}")


def demo_bfs_search():
    print("\n___ Breadth-First Search ___")

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

    print(
        "Graph structure: X connects to Y,Z; Y connects to W; Z connects to V; W,V connect to U"
    )
    print("Starting BFS from node X:")
    bfs = BFS(graph, "X")

    print("Paths discovered by BFS:")
    for node in ["Y", "Z", "U"]:
        if bfs.has_path_to(node):
            path = list(bfs.path_to(node))
            print(f"  X → {node}: {' → '.join(path)}")


def demo_dfs_vs_bfs():
    print("\n___ DFS vs BFS Comparison ___")

    graph = UndirectedGraph()
    nodes = ["Start", "A", "B", "C", "D", "E", "F", "G", "H", "Goal"]
    edges = [
        ("Start", "A", 1.0),
        ("Start", "B", 1.0),
        ("A", "C", 1.0),
        ("A", "D", 1.0),
        ("B", "E", 1.0),
        ("B", "F", 1.0),
        ("C", "G", 1.0),
        ("D", "G", 1.0),
        ("E", "H", 1.0),
        ("F", "H", 1.0),
        ("G", "Goal", 1.0),
        ("H", "Goal", 1.0),
    ]

    for node in nodes:
        graph.add_node(node)
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print("Large graph with multiple paths:")
    print("  Level 0: Start")
    print("  Level 1: A, B")
    print("  Level 2: C, D, E, F")
    print("  Level 3: G, H")
    print("  Level 4: Goal")
    print("Finding path from Start to Goal:\n")

    dfs = DFS(graph, "Start")
    bfs = BFS(graph, "Start")

    if dfs.has_path_to("Goal"):
        dfs_path = list(dfs.path_to("Goal"))
        print(f"DFS: {' → '.join(dfs_path)}")
        print("(explores deeply: Start→A→C→G or Start→A→D→G, etc.)")

    if bfs.has_path_to("Goal"):
        bfs_path = list(bfs.path_to("Goal"))
        print(f"BFS: {' → '.join(bfs_path)}")
        print("(explores level-by-level: Start→A→C→G or Start→B→E→H, etc.)")


def demo_directed_graph_search():
    print("\n___ Search in Directed Graphs ___")

    graph = DirectedGraph()
    nodes = ["Source", "A", "B", "C", "D", "E", "Target", "Dead", "End"]
    edges = [
        ("Source", "A", 1.0),
        ("Source", "B", 1.0),
        ("A", "C", 1.0),
        ("A", "Dead", 1.0),
        ("B", "D", 1.0),
        ("B", "E", 1.0),
        ("C", "Target", 1.0),
        ("D", "E", 1.0),
        ("E", "Target", 1.0),
        ("Dead", "End", 1.0),
    ]

    for node in nodes:
        graph.add_node(node)
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print("Directed graph:")
    print("  Source→A→C→Target (valid path)")
    print("  Source→A→Dead→End (dead end)")
    print("  Source→B→D→E→Target (longer valid path)\n")

    dfs = DFS(graph, "Source")
    bfs = BFS(graph, "Source")

    print("DFS from Source:")
    if dfs.has_path_to("Target"):
        path = list(dfs.path_to("Target"))
        print(f"  Can reach Target: {' → '.join(path)}")
    else:
        print("  Cannot reach Target")

    if dfs.has_path_to("Dead"):
        print(f"  Can reach Dead: {' → '.join(list(dfs.path_to('Dead')))}")
    else:
        print("  Cannot reach Dead")

    print("\nBFS from Source:")
    if bfs.has_path_to("Target"):
        path = list(bfs.path_to("Target"))
        print(f"  Can reach Target: {' → '.join(path)}")
    else:
        print("  Cannot reach Target")

    if bfs.has_path_to("Dead"):
        print(f"  Can reach Dead: {' → '.join(list(bfs.path_to('Dead')))}")
    else:
        print("  Cannot reach Dead")


def demo_search_algorithms():
    demo_dfs_search()
    demo_bfs_search()
    demo_dfs_vs_bfs()
    demo_directed_graph_search()
