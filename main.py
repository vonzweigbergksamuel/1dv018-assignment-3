import random
from pathlib import Path

from utils.quick_sort import QuickSort
from tasks.task1 import PATTERN_RUNS, benchmark_pattern, plot_quick_vs_heap


def main():
    # list = []
    # for _ in range(100):
    #     list.append(random.randint(0, 1000))

    # print("Unsorted list", list)

    # quick_sort = QuickSort()
    # quick_sort.sort(list)

    # print("Sorted function calls", quick_sort.count)
    # print("Sorted list", list)

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
