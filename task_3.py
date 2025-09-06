# Завдання 3: Порівняння алгоритмів сортування
import random
import timeit

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# Тестування алгоритмів
def benchmark():
    sizes = [100, 1000, 5000]  # різні розміри масивів
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        print(f"\nТест для масиву з {size} елементів:")

        # Перевіряємо час виконання кожного алгоритму
        for name, func in [("Insertion Sort", insertion_sort),
                           ("Merge Sort", merge_sort),
                           ("Timsort (sorted)", sorted)]:
            # number=3 для стабільнішого результату
            t = timeit.timeit(lambda: func(arr.copy()), number=3)
            print(f"{name}: {t:.6f} секунд")

if __name__ == "__main__":
    benchmark()
