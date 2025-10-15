from utils.directed_graph import DirectedGraph
from utils.undirected_graph import UndirectedGraph


def demo_undirected_graph():
    print("\n=== Undirected Graph Demo ===")
    graph = UndirectedGraph()

    print("Adding nodes: A, B, C, D")
    graph.add_node("A")
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")

    print(f"Number of nodes: {graph.num_nodes()}")
    print(f"Number of edges: {graph.num_edges()}")

    print("\nAdding edges:")
    print("A -- B (weight: 2.0)")
    graph.add_edge("A", "B", 2.0)
    print("B -- C (weight: 1.5)")
    graph.add_edge("B", "C", 1.5)
    print("C -- D (weight: 3.0)")
    graph.add_edge("C", "D", 3.0)
    print("A -- D (weight: 1.0)")
    graph.add_edge("A", "D", 1.0)

    print(f"\nNumber of nodes: {graph.num_nodes()}")
    print(f"Number of edges: {graph.num_edges()}")

    print("\nNode degrees:")
    for node in graph.nodes():
        print(f"  {node}: {graph.degree(node)}")

    print("\nAll edges:")
    for u, v, weight in graph.edges():
        print(f"  {u} -- {v} (weight: {weight})")

    print("\nNeighbors of each node:")
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        print(f"  {node}: {neighbors}")

    print("\nRemoving edge B -- C")
    graph.remove_edge("B", "C")
    print(f"Number of edges after removal: {graph.num_edges()}")
    print("Remaining edges:")
    for u, v, weight in graph.edges():
        print(f"  {u} -- {v} (weight: {weight})")


def demo_directed_graph():
    print("\n=== Directed Graph Demo ===")
    graph = DirectedGraph()

    print("Adding nodes: X, Y, Z, W")
    graph.add_node("X")
    graph.add_node("Y")
    graph.add_node("Z")
    graph.add_node("W")

    print(f"Number of nodes: {graph.num_nodes()}")
    print(f"Number of edges: {graph.num_edges()}")

    print("\nAdding directed edges:")
    print("X -> Y (weight: 1.0)")
    graph.add_edge("X", "Y", 1.0)
    print("Y -> Z (weight: 2.5)")
    graph.add_edge("Y", "Z", 2.5)
    print("Z -> W (weight: 0.5)")
    graph.add_edge("Z", "W", 0.5)
    print("W -> X (weight: 3.0)")
    graph.add_edge("W", "X", 3.0)
    print("X -> Z (weight: 1.5)")
    graph.add_edge("X", "Z", 1.5)

    print(f"\nNumber of nodes: {graph.num_nodes()}")
    print(f"Number of edges: {graph.num_edges()}")

    print("\nNode degrees (outgoing connections):")
    for node in graph.nodes():
        print(f"  {node}: {graph.degree(node)}")

    print("\nAll edges:")
    for u, v, weight in graph.edges():
        print(f"  {u} -> {v} (weight: {weight})")

    print("\nOutgoing neighbors of each node:")
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        print(f"  {node}: {neighbors}")

    print("\nRemoving edge Y -> Z")
    graph.remove_edge("Y", "Z")
    print(f"Number of edges after removal: {graph.num_edges()}")
    print("Remaining edges:")
    for u, v, weight in graph.edges():
        print(f"  {u} -> {v} (weight: {weight})")


def demo_graph_comparison():
    print("\n=== Graph Comparison Demo ===")

    # Create both graph types with same nodes and edges
    undirected = UndirectedGraph()
    directed = DirectedGraph()

    nodes = ["P", "Q", "R"]
    edges = [("P", "Q", 1.0), ("Q", "R", 2.0), ("R", "P", 1.5)]

    print("Adding same nodes and edges to both graphs:")
    for node in nodes:
        undirected.add_node(node)
        directed.add_node(node)

    for u, v, weight in edges:
        print(f"  {u} -- {v} (weight: {weight})")
        undirected.add_edge(u, v, weight)
        directed.add_edge(u, v, weight)

    print("\nUndirected graph:")
    print(f"  Nodes: {undirected.num_nodes()}")
    print(f"  Edges: {undirected.num_edges()}")
    print(f"  Edge count: {undirected.num_edges()}")

    print("\nDirected graph:")
    print(f"  Nodes: {directed.num_nodes()}")
    print(f"  Edges: {directed.num_edges()}")
    print(f"  Edge count: {directed.num_edges()}")

    print(
        "\nKey difference: Undirected edges are bidirectional, directed edges are one-way"
    )


def demo_graphs():
    demo_undirected_graph()
    demo_directed_graph()
    demo_graph_comparison()
