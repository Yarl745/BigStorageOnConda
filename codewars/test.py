# def comp(array1, array2):
# if array1 is not None and array2 is not None:
#     #
#     if array1.__class__ != [].__class__ or array2.__class__ != [].__class__: return False
#     #
#     sum_elem = 0
#     for elem in array2:
#         elem **= 0.5
#         #
#         if elem not in array1: return False
#         sum_elem += elem
#     if sum(array1) != sum_elem: return False
#     return True
# else:
#     return False


# def comp(array1, array2):
#     if array1 is not None and array2 is not None:
#         for elem in array2:
#             elem **= 0.5
#             #
#             if elem in array1:
#                 array1.remove(elem)
#             else:
#                 return False
#         if array1: return False
#         return True
#     else:
#         return False

def openOrSenior(data):
    # ID
    age, handicap = 0, 1
    # OUTPUT LIST
    out = []
    # SEARCH
    for pers in data:
        if pers[age] >= 55 and pers[handicap] > 7:
            out += ['Senior']
        else:
            out += ['Open']
    return out
