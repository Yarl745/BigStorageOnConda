import random
# ----------------------------------------------------------------------------------------------------------------------
def get_max(arr):
    if len(arr) == 1: return arr[0]
    next_elem = get_max(arr[1:])
    if arr[0] > next_elem:
        return arr[0]
    else:
        return next_elem
# ----------------------------------------------------------------------------------------------------------------------
arr = [random.randint(1, 100) for i in range(10)]
print(arr)
print(get_max(arr))
