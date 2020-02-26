def divide(side1, side2):
    if side1 > side2:
        printSquare(side2, side1 // side2)
        side1 %= side2
    elif side2 > side1:
        printSquare(side1, side2 // side1)
        side2 %= side1
    if side1 == 0 or side2 == 0:
        if side1 != 0: return side1
        else: return side2
    return divide(side1, side2)


def printSquare(side, amount):
    print('{0}*{0} '.format(side) * amount)


el = divide(1680, 640)
print(1680 * 640 // el**2)
