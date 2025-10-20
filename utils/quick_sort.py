class QuickSort:
    def __init__(self) -> None:
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
        self._sort(list, 0, len(list) - 1)

    def _sort(self, list, low, high):
        if high <= low:
            return

        self.count += 1

        j = self._partition(list, low, high)
        self._sort(list, low, j - 1)
        self._sort(list, j + 1, high)


class FirstElementPivotQuickSort:
    def __init__(self) -> None:
        self.count = 0

    def _partition(self, list, low, high):
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
        self._sort(list, 0, len(list) - 1)

    def _sort(self, list, low, high):
        if high <= low:
            return

        self.count += 1

        j = self._partition(list, low, high)
        self._sort(list, low, j - 1)
        self._sort(list, j + 1, high)
