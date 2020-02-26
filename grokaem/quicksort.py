import random
# ----------------------------------------------------------------------------------------------------------------------
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[random.randint(0, len(arr) - 1)]
        less, greater = [], []
        pivot_elements = 0
        for el in arr:
            if el < pivot: less.append(el)
            elif el > pivot: greater.append(el)
            else: pivot_elements += 1
        return quick_sort(less) + [pivot]*pivot_elements + quick_sort(greater)
# ----------------------------------------------------------------------------------------------------------------------
arr = [random.randint(1, 100) for i in range(1000)]
print(arr)
print(quick_sort(arr))


