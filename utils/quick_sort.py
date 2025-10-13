import math
from utils.heap_sort import HeapSort


class QuickSort:
    def __init__(self, max_depth=None) -> None:
        self.max_depth = max_depth
        self.count = 0

    def _partition(self, list, low, high):
        median = (low + high) // 2
        list[low], list[median] = list[median], list[low]
        pivot = list[low]

        i, j = low, high + 1

        while True:
            i += 1
            while i <= high and list[i] < pivot:
                i += 1

            j -= 1
            while j >= low and list[j] > pivot:
                j -= 1

            if i >= j:
                break
            list[i], list[j] = list[j], list[i]

        list[low], list[j] = list[j], list[low]
        return j

    def sort(self, list):
        if self.max_depth is None:
            self.max_depth = int(2 * math.log2(len(list)))
        self._sort(list, 0, len(list) - 1, 0)

    def _sort(self, list, low, high, depth):
        if high <= low:
            return

        if depth >= self.max_depth:
            print("Shiften to heap_sort")
            heap_sort = HeapSort(list[low : high + 1])
            heap_sort.sort()
            list[low : high + 1] = heap_sort.height[1:]
            return

        self.count += 1

        j = self._partition(list, low, high)
        self._sort(list, low, j - 1, depth + 1)
        self._sort(list, j + 1, high, depth + 1)
