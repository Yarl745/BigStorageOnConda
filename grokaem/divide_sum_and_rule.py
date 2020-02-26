def divide_sum(arr):
    middle = len(arr) // 2
    if len(arr) == 1: return arr[0]
    return divide_sum(arr[:middle]) + divide_sum(arr[middle:])
# ----------------------------------------------------------------------------------------------------------------------
arr = [2 for el in range(10)]
# ----------------------------------------------------------------------------------------------------------------------
print(divide_sum(arr))
# ----------------------------------------------------------------------------------------------------------------------

