import re

f = " Як тебе не любити, Києве мій! "
# 0
f_copy = f[:]
f_copy = f_copy.strip(' ')
print('После удаления боковых побыелов: {}'.format(f_copy))
print('Count of the "и" char in the string = {}'.format(f_copy.count('и')))
print(f_copy.split(), '\n')

# 1
f_copy = f.lstrip(" ").title()[-1::-1].split(',')
print(f_copy, '\n')

# 2
f_copy = f.upper().replace('К', '').replace('НЕ ЛЮБИТИ', 'ЛЮБЛЮ').rstrip(' ')
print(f_copy, '\n')

# 3
print('len = {}'.format(len(f)))
f_copy = f.replace('', ' ').strip(' ')[-1::-1]
print(f_copy, '\n')

# 4
str = f.title()
f_copy = ''
for i in range(len(str)):
    if i % 2 == 1 and str[i].islower() and str[i].isalpha():
        f_copy += '-' + str[i]
    else:
        f_copy += str[i]
print(f_copy, '\n')

# 5
arr_char = list(f.replace(' ', ''))
str1 = ''.join([arr_char[i] for i in range(0, len(arr_char), 2)])
str2 = ''.join([arr_char[i] for i in range(1, len(arr_char), 2)])
print(str1, str2, sep='\n')
