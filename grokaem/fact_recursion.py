def factorial(numb):
    if numb == 1:
        return 1
    else:
        return numb * factorial(numb - 1)
# ----------------------------------------------------------------------------------------------------------------------
print(factorial(4))
