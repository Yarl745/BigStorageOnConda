def binary_s(arr, searched_el):
    first, last = 0, len(arr) - 1
    while first <= last:
        middle = (first + last) // 2
        if searched_el > arr[middle]:
            first = middle + 1
        elif searched_el < arr[middle]:
            last = middle - 1
        else:
            return middle
    return 'Not such element in the current list!'


arr = [1, 6, 3, 6, 73, 5, 76, 5]
print(binary_s(sorted(arr), 1))
