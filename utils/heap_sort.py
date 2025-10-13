class HeapSort:
    def __init__(self, length) -> None:
        self.height = [None] + length
        self.size = len(self.height) - 1

    def _sink(self, k):
        while 2 * k <= self.size:
            j = 2 * k
            if j < self.size and self.height[j] < self.height[j + 1]:
                j += 1

            if not self.height[k] < self.height[j]:
                break

            self.height[k], self.height[j] = self.height[j], self.height[k]

            k = j

    def sort(self):
        k = self.size // 2

        while k >= 1:
            self._sink(k)
            k -= 1

        while self.size > 1:
            self.height[1], self.height[self.size] = (
                self.height[self.size],
                self.height[1],
            )
            self.size -= 1
            self._sink(1)
