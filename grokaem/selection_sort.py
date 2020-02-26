def get_index_of_smallest(arr):
    index_of_smallest = 0
    smallest = arr[index_of_smallest]
    for index in range(1, len(arr)):
        if arr[index] < smallest:
            index_of_smallest = index
            smallest = arr[index]
    return index_of_smallest


def selection_sorted(arr):
    out_arr = []
    for iter in range(len(arr)):
        out_arr.append(arr.pop(get_index_of_smallest(arr)))
    return out_arr


arr = [1, 6, 3, 6, 73, 5, 76, 5]
print(selection_sorted(arr))