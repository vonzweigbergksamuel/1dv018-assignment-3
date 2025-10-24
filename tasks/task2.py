from utils.directed_graph import DirectedGraph
from utils.undirected_graph import UndirectedGraph


def demo_undirected_graph():
    print("\n___ Undirected Graph ___")
    graph = UndirectedGraph()

    nodes = ["A", "B", "C", "D"]
    for node in nodes:
        graph.add_node(node)

    edges = [("A", "B", 2.0), ("B", "C", 1.5), ("C", "D", 3.0), ("A", "D", 1.0)]
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print(f"Nodes: {graph.num_nodes()}, Edges: {graph.num_edges()}")
    print("Edge list: A-B, B-C, C-D, A-D")
    print("Node degrees:", {node: graph.degree(node) for node in nodes})

    graph.remove_edge("B", "C")
    print(f"After removing B-C: {graph.num_edges()} edges")


def demo_directed_graph():
    print("\n___ Directed Graph ___")
    graph = DirectedGraph()

    nodes = ["X", "Y", "Z", "W"]
    for node in nodes:
        graph.add_node(node)

    edges = [
        ("X", "Y", 1.0),
        ("Y", "Z", 2.5),
        ("Z", "W", 0.5),
        ("W", "X", 3.0),
        ("X", "Z", 1.5),
    ]
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)

    print(f"Nodes: {graph.num_nodes()}, Edges: {graph.num_edges()}")
    print("Edge list: X->Y, Y->Z, Z->W, W->X, X->Z")
    print("Outgoing degrees:", {node: graph.degree(node) for node in nodes})

    graph.remove_edge("Y", "Z")
    print(f"After removing Y->Z: {graph.num_edges()} edges")


def demo_graph_comparison():
    print("\n___ Comparing Graph Types ___")

    undirected = UndirectedGraph()
    directed = DirectedGraph()

    nodes = ["P", "Q", "R"]
    edges = [("P", "Q", 1.0), ("Q", "R", 2.0), ("R", "P", 1.5)]

    for node in nodes:
        undirected.add_node(node)
        directed.add_node(node)

    for u, v, weight in edges:
        undirected.add_edge(u, v, weight)
        directed.add_edge(u, v, weight)

    print("Same 3 edges added to both graphs:")
    print(f"  Undirected: {undirected.num_edges()} edges (bidirectional)")
    print(f"  Directed: {directed.num_edges()} edges (one-way)")
    print("Result: Undirected has double the edges because each edge goes both ways")


def demo_graphs():
    demo_undirected_graph()
    demo_directed_graph()
    demo_graph_comparison()
