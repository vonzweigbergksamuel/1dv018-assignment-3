from pathlib import Path

from tasks.task1 import PATTERN_RUNS, benchmark_pattern, plot_quick_vs_heap
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
        # 300_000,
        # 500_000,
        # 1_000_000,
    ]
    for pattern, runs in PATTERN_RUNS.items():
        pattern_sizes = sizes if pattern == "quick_worst" else sizes
        path = plot_quick_vs_heap(pattern_sizes, runs, pattern=pattern)
        print(f"Saved {pattern} plot to {Path(path).name}")

        if pattern == "quick_worst":
            quick_times, heap_times = benchmark_pattern(pattern_sizes, runs, pattern)
            ratios = [
                q / h if h else float("inf") for q, h in zip(quick_times, heap_times)
            ]
            idx = max(range(len(pattern_sizes)), key=lambda i: ratios[i])
            print(
                "QuickSort worst case:",
                f"n={pattern_sizes[idx]} => QuickSort {ratios[idx]:.1f}x slower than HeapSort",
            )


if __name__ == "__main__":
    main()
