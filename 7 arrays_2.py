# Сортировка пузырьком.
# Повторяет проходы по массиву, сравнивая соседние элементы и меняя их местами, если они стоят в неправильном порядке.
# Проста в реализации, но медленная для больших массивов. Хороша для учебных целей и небольших массивов.
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# Сортировка вставками.
# Строит отсортированный массив, вставляя каждый новый элемент на нужное место среди уже отсортированных.
# Эффективна для небольших массивов и почти отсортированных данных. Проста в реализации.
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp

    return array


# Сортировка слиянием
# Рекурсивно делит массив на две части, сортирует каждую из них, а затем объединяет отсортированные части.
# Подходит для сортировки больших массивов. Стабильна и эффективна, но требует дополнительной памяти.
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


# Быстрая сортировка.
# Выбирает опорный элемент (пивот), делит массив на части, где элементы меньше или больше пивота, и рекурсивно сортирует эти части.
# Одна из самых быстрых для общего использования, особенно для больших массивов. Однако её производительность сильно зависит от выбора пивота.
def quick_sort(array, start, end):
    if end - start > 1:
        p = partition(array, start, end)
        quick_sort(array, start, p)
        quick_sort(array, p + 1, end)

    return array

def partition(array, start, end):
    pivot = array[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and array[i] <= pivot):
            i = i + 1
        while (i <= j and array[j] >= pivot):
            j = j - 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            array[start], array[j] = array[j], array[start]
            return j


# Сортировка подсчётом.
# Подходит для массивов с ограниченным диапазоном значений, подсчитывая количество каждого элемента и использует эти данные для сортировки.
# Эффективна для массивов с числами в ограниченном диапазоне. Не подходит для массивов с очень большим диапазоном значений или нецелых чисел.
def counting_sort(array):
    if len(array) == 0:
        return array

    largest = max(array)
    c = [0] * (largest + 1)
    for num in array:
        c[num] += 1

    for i in range(1, largest + 1):
        c[i] += c[i - 1]

    result = [None] * len(array)

    for x in reversed(array):
        result[c[x] - 1] = x
        c[x] -= 1

    return result


# Временные замеры.
# Результаты временных замеров: самая быстрая сортировка – подсчётом (0.0), затем быстрая (≈ 0.001), слиянием (≈ 0.002), вставками (≈ 0.03) и пузырьком (≈ 0.06)
import time

with open("7 arrays_2.txt", "r") as file:
    array_str = file.read()
    array = eval(array_str)

start_time = time.time()
sorted_array = bubble_sort(array.copy())
end_time = time.time()
print("Сортировка пузырьком:", end_time - start_time)
print(sorted_array)
print()

start_time = time.time()
sorted_array = insertion_sort(array.copy())
end_time = time.time()
print("Сортировка вставками:", end_time - start_time)
print(sorted_array)
print()

start_time = time.time()
sorted_array = merge_sort(array.copy())
end_time = time.time()
print("Сортировка слиянием:", end_time - start_time)
print(sorted_array)
print()

start_time = time.time()
sorted_array = quick_sort(array.copy(), 0, len(array))
end_time = time.time()
print("Быстрая сортировка:", end_time - start_time)
print(sorted_array)
print()

start_time = time.time()
sorted_array = counting_sort(array.copy())
end_time = time.time()
print("Сортировка подсчётом:", end_time - start_time)
print(sorted_array)