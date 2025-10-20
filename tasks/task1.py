import random
import time
from pathlib import Path
from statistics import mean
from typing import List, Sequence

import matplotlib.pyplot as plt

from utils.heap_sort import HeapSort
from utils.quick_sort import QuickSort, FirstElementPivotQuickSort


IMAGES_DIR = Path(__file__).resolve().parent.parent / "images"
PATTERN_RUNS = {
    "random": 5,
    "sorted": 3,
    "reverse": 3,
    "duplicates": 5,
}


def _generate_sample(size: int, pattern: str) -> List[int]:
    if pattern == "random":
        return random.sample(range(size * 10), size)
    if pattern == "sorted":
        return list(range(size))
    if pattern == "reverse":
        return list(range(size, 0, -1))
    if pattern == "duplicates":
        bucket = max(1, size // 10)
        return [random.randrange(bucket) for _ in range(size)]
    raise ValueError(f"Unknown pattern: {pattern}")


def _time_quick_sort(values: List[int]) -> float:
    sorter = QuickSort()
    sample = values.copy()
    start = time.perf_counter()
    sorter.sort(sample)
    return time.perf_counter() - start


def _time_heap_sort(values: List[int]) -> float:
    sample = values.copy()
    start = time.perf_counter()
    sorter = HeapSort(sample)
    sorter.sort()
    return time.perf_counter() - start


def _time_first_element_pivot_quick_sort(values: List[int]) -> float:
    sorter = FirstElementPivotQuickSort()
    sample = values.copy()
    start = time.perf_counter()
    try:
        sorter.sort(sample)
    except RecursionError:
        return float("inf")
    return time.perf_counter() - start


def _average_times_three_ways(
    size: int, runs: int, pattern: str
) -> tuple[float, float, float]:
    quick_results = []
    heap_results = []
    first_pivot_results = []

    for _ in range(runs):
        sample = _generate_sample(size, pattern)
        quick_results.append(_time_quick_sort(sample))
        heap_results.append(_time_heap_sort(sample))
        first_pivot_results.append(_time_first_element_pivot_quick_sort(sample))

    return mean(quick_results), mean(heap_results), mean(first_pivot_results)


def benchmark_pattern(
    sizes: Sequence[int], runs: int, pattern: str
) -> tuple[List[float], List[float], List[float]]:
    quick_times = []
    heap_times = []
    first_pivot_times = []

    for size in sizes:
        quick_avg, heap_avg, first_pivot_avg = _average_times_three_ways(
            size, runs, pattern
        )
        quick_times.append(quick_avg)
        heap_times.append(heap_avg)
        first_pivot_times.append(first_pivot_avg)

    return quick_times, heap_times, first_pivot_times


def plot_quick_vs_heap(
    sizes: List[int],
    runs: int = 5,
    *,
    pattern: str = "random",
    show: bool = False,
) -> Path:
    quick_times: List[float]
    heap_times: List[float]
    first_pivot_times: List[float]

    quick_times, heap_times, first_pivot_times = benchmark_pattern(sizes, runs, pattern)

    differences = [abs(q - h) for q, h in zip(quick_times, heap_times)]
    crossover_index = differences.index(min(differences))
    crossover_size = sizes[crossover_index]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, quick_times, marker="o", label="QuickSort")
    plt.plot(sizes, heap_times, marker="s", label="HeapSort")

    # Cap infinite values for first pivot times for better visualization
    display_first_pivot = []
    for i, t in enumerate(first_pivot_times):
        if t == float("inf"):
            # Cap at 1.5x the max of the other two at this size
            display_first_pivot.append(max(quick_times[i], heap_times[i]) * 1.5)
        else:
            display_first_pivot.append(t)

    plt.plot(
        sizes,
        display_first_pivot,
        marker="^",
        label="QuickSort (First Element Pivot)",
        color="red",
    )
    plt.axvline(crossover_size, color="gray", linestyle="--", alpha=0.4)
    plt.text(
        crossover_size,
        max(quick_times[crossover_index], heap_times[crossover_index]) * 1.02,
        f"Crossover ≈ {crossover_size}",
        rotation=90,
        va="bottom",
        ha="center",
        fontsize=9,
        color="gray",
    )
    plt.title(f"QuickSort vs HeapSort Performance ({pattern})")
    plt.xlabel("Input size")
    plt.ylabel("Average time (seconds)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.tight_layout()

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    output_path = IMAGES_DIR / f"quick_vs_heap_{pattern}.png"
    plt.savefig(output_path)

    if show:
        plt.show()

    plt.close()

    return output_path
