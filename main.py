import random
from utils.quick_sort import QuickSort


def main():
    list = []
    for _ in range(100):
        list.append(random.randint(0, 1000))

    print("Unsorted list", list)

    quick_sort = QuickSort()
    quick_sort.sort(list)

    print("Sorted function calls", quick_sort.count)
    print("Sorted list", list)


if __name__ == "__main__":
    main()
