from decimal import Decimal as dec
import math, random, re
from collections import Counter

"""Завдання №17
Створіть фрагмент програми знаходження суми цифр тризначного числа.
Забезпечте введення числа з клавіатури. Для виводу використовувати
форматування."""
dig = int(input('Input three-digit number: '))
if len(str(dig)) == 3:
    my_sum = sum([int(char) for char in str(dig)])
    print('  Output: {:>5}'.format(my_sum), '\n')
else: print('You should input three-digit number...', '\n')


"""Завдання №18
Створіть фрагмент програми знаходження площі та периметра прямокутного
трикутника по двох заданих катетах. Забезпечте введення довжин катетів з
клавіатури. Для виводу використовувати форматування."""
k1 = dec(input('Катет1 = '))
k2 = dec(input('Катет2 = '))
print('   Square {:^4} {:<5}'.format('=', k1*k2/2))
print('   Perimeter {:^4} {:<5}'.format('=', round(k1+k2+dec(math.sqrt(k1**2 + k2**2)), 3)), '\n')


"""Завдання №19
Створіть фрагмент програми для виводу рівняння прямої, що проходить через
дві задані точки. Забезпечте ввід з клавіатури координат точок. Для виводу
використовувати форматування.
(y1 = kx1 + b
(y2 = kx2 + b
"""
x1 = dec(input('x1 = ')); y1 = dec(input('y1 = '))
x2 = dec(input('x2 = ')); y2 = dec(input('y2 = '))
coef = x1 / x2
b = (y1 - coef*y2) / (1 - coef)
k = (y1 - b) / x1
print(' Answer:  y = {0}x{1:+}'.format(round(k, 2), round(b, 2)), '\n')


"""Завдання №20
Створіть фрагмент програми для генерації випадкових цілого та дійсного
чисел в межах діапазонів, введених користувачем з клавіатури. Для виводу
використовувати форматування. """
min_ = int(input('min = '))
max_ = int(input('max = '))
print('Random integer in range of {}-{}  =  {}'.format(min_, max_, random.randint(min_, max_)))
print('Random float in range of {:}-{:}  =  {}'.format(min_, max_, round(random.uniform(min_, max_), 3)))


"""Завдання №21
Створіть фрагмент програми для знаходження коренів квадратного рівняння.
Забезпечте введення коефіцієнтів при невідомих з клавіатури. """
a = dec(input('a = '))
b = dec(input('b = '))
c = dec(input('c = '))
try:
    d = dec(math.sqrt(b**2 - 4*a*c))
    if a == 0:
        print('Это не квадратное уравнение..'.center(20))
    elif d > 0:
        x1 = (-b + d) / 2*a
        x2 = (-b - d) / 2*a
        print('x1 = {};  x2 = {}'.format(x1, x2).center(20))
    elif d == 0:
        x = -b / 2*a
        print('x = {}'.format(x).center(20))
except ValueError as ve:
    print('Корней не существует!'.center(20))


"""Завдання №22
Створіть фрагмент програми для визначення існування трикутника по трьох
сторонах. Значення довжин сторін вводити з клавіатури. """
sides = [int(side) for side in input('Введите три стороны, через пробел: ').split()]
text = 'Данный треугольник не существует('
for i in range(3):
    side = sides.pop(0)
    if side < sum(sides):
        sides.append(side)
    else: break
else:
    text = 'Данный треугольник существует)'
print(text.center(50))


"""Завдання №23
Створіть фрагмент програми для визначення існування трикутника по трьох
сторонах. Значення довжин сторін введіть з клавіатури. Якщо трикутник не
існує, визначте, яка із сторін порушує умову існування трикутника з виводом
повідомлення про цей факт."""
sides = [int(side) for side in input('Введите три стороны, через пробел: ').split()]
text = ''
for i in range(3):
    side = sides.pop(0)
    if side < sum(sides):
        sides.append(side)
    else:
        text = 'Данный треугольник не существует из-за стороны с длинной {}'.format(side)
        break
else:
    text = 'Данный треугольник существует)'
print(text.center(50))


"""Завдання №24
Створіть фрагмент програми для визначення по координатах точки, у якій
чверті координатної площини вона розміщена. """
x = dec(input('x = ')); y = dec(input('y = '))
if x >= 0:
    if y <= 0:
        print('Точка находится в 4-ой четверти!'.center(50))
    else:
        print('Точка находится в 1-ой четверти!'.center(50))
else:
    if y <= 0:
        print('Точка находится в 3-ой четверти!'.center(50))
    else:
        print('Точка находится в 2-ой четверти!'.center(50))


"""Завдання №25
Створіть фрагмент програми, яка дозволяє обчислити площу прямокутника,
трикутника або круга за вибором користувача. Забезпечте діалог з
користувачем щодо вибору фігури та даних для обчислення її площі."""
print(' SQUARE CALCULATION '.center(60, '='))
print('1-rectangle;  2-triangle;  3-circle'.center(60, '-'))
status = int(input('Figure(input digit from the menu): '))
s = 0
if status == 1:
    side1 = dec(input('Input first side: '))
    side2 = dec(input('Input second side: '))
    s = side1 * side2
elif status == 2:
    side = dec(input('Input side: '))
    h = dec(input('Input height which carried out to the side: '))
    s = side * h * dec(0.5)
elif status == 3:
    r = dec(input('Input radius: '))
    s = dec(math.pi) * r**2
print('Square = {}'.format(s).center(60))


"""Завдання №26
Створіть фрагмент програми для визначення приналежності точки на
координатній площині кругу з центром в початку координат (проекції точки
на осі координат є катетами прямокутного трикутника, гіпотенуза визначає
відстань від точки до початку координат, а отже, якщо довжина гіпотенузи
менша від радіуса круга, то точка належить кругу). """
r = dec(input('Radius = '))
x = dec(input('x = '))
y = dec(input('y = '))
if r >= dec(math.sqrt(x**2 + y**2)):
    print('Точка принадлежит окружности')
else:
    print('Точка не принадлежит окружности')


"""Завдання №27
Створіть фрагмент програми для визначення кількості парних і непарних цифр
у введеному користувачем числі."""
dig_str = input('Input digit: ')
pair_numbers, not_pair_numbers = 0, 0
for char in dig_str:
    dig = int(char)
    if dig % 2 == 0: pair_numbers += 1
    else: not_pair_numbers += 1
print('Pair numbers = {:<7} Not a pair numbers = {} '.format(pair_numbers, not_pair_numbers))


"""Завдання №28
Створіть фрагмент програми для обчислення добутку значущих цифр числа,
введеного користувачем з клавіатури. """
dig_str = input('Input number: ').replace('0', '').replace('.', '')
mult = 1
for dig_char in dig_str:
    mult *= int(dig_char)
print('Product of multiplication = {}'.format(mult))


"""Завдання №29
Створіть фрагмент програми для визначення відсотка великих і малих літер у
рядку, введеному користувачем. """
text = input('Input some text: ')
small = len(re.findall("[a-z]", text))
big = len(re.findall("[A-Z]", text))
perc_big = round(dec(big) / dec(big+small) * 100, 2)
perc_small = 100 - perc_big
print('Big letters: {}%;   Small letters: {}%'.format(perc_big, perc_small))


"""Завдання №30
Створіть фрагмент програми для знаходження найменшого спільного
кратного двох чисел"""
dig1 = int(input('Digit1 = '))
dig2 = int(input('Digit2 = '))


def get_multiplier_arr(dig, mult_arr=[], mult=2):
    if dig == mult:
        mult_arr.append(mult)
        copy_arr = mult_arr[:]
        mult_arr.clear()
        return copy_arr
    elif dig < mult:
        copy_arr = mult_arr[:]
        mult_arr.clear()
        return copy_arr

    while dig % mult == 0:
        dig /= mult
        mult_arr.append(mult)
    else:
        mult += 1
        return get_multiplier_arr(dig, mult_arr, mult)

"""
>>> z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
>>> Counter(z)
Counter({'blue': 3, 'red': 2, 'yellow': 1})
"""
dig1_arr = get_multiplier_arr(dig1)
dig2_arr = get_multiplier_arr(dig2)

dig1_dict = Counter(dig1_arr)
dig2_dict = Counter(dig2_arr)
nsk = 1
for key in dig1_dict.keys():
    if dig1_dict[key] >= dig2_dict[key]:
        nsk *= key ** dig1_dict[key]
    else:
        nsk *= key ** dig2_dict[key]
    if key in dig2_dict: dig2_dict.pop(key)
for key in dig2_dict.keys():
    nsk *= key ** dig2_dict[key]

print('Digit1:{};   Digit2:{}'.format(dig1_arr, dig2_arr))
print('NSK = {}'.format(nsk))