from pathlib import Path

from tasks.task1 import PATTERN_RUNS, plot_quick_vs_heap
from tasks.task2 import demo_graphs
from tasks.task3 import demo_search_algorithms
from tasks.task4 import demo_dijkstras_algorithms


def main():
    print("Running Graph Demonstrations...")
    demo_graphs()

    print("\n" + "=" * 60)
    print("Running Search Algorithm Demonstrations...")
    demo_search_algorithms()

    print("\n" + "=" * 60)
    print("Running Dijkstra's Algorithm Demonstrations...")
    demo_dijkstras_algorithms()

    print("\n" + "=" * 60)
    print("Running Sorting Algorithm Benchmarks...")

    sizes = [
        1_000,
        3_000,
        5_000,
        10_000,
        30_000,
        50_000,
        100_000,
    ]
    for pattern, runs in PATTERN_RUNS.items():
        pattern_sizes = sizes
        path = plot_quick_vs_heap(pattern_sizes, runs, pattern=pattern)
        print(f"Saved {pattern} plot to {Path(path).name}")


if __name__ == "__main__":
    main()
