def find_element_index(array):
    for i in range(len(array)):
        if array[i] == 1:
            return i
    return -1

array = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
element_index = find_element_index(array)
if element_index != -1:
    print(f"Место разделения: индекс {element_index}")
else:
    print("Разделение не найдено.")
