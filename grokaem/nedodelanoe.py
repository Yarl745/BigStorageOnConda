import random
# ----------------------------------------------------------------------------------------------------------------------
def quicksorted(arr, start_index, end_index):
    if end_index - start_index == 0: return
    elif end_index - start_index == 1:
        if arr[start_index] > arr[end_index]:
            arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        return
    #
    pivot_index = (end_index + start_index) // 2
    start_index_c, end_index_c = start_index, end_index
    #
    while start_index_c < pivot_index < end_index_c:
        while arr[start_index_c] < arr[pivot_index]:
            start_index_c += 1
        while arr[end_index_c] >= arr[pivot_index]:
            end_index_c -= 1
        if start_index_c < pivot_index < end_index_c:
            arr[start_index_c], arr[end_index_c] = arr[end_index_c], arr[start_index_c]
    #
    quicksorted(arr, start_index, pivot_index)
    quicksorted(arr, pivot_index + 1, end_index)