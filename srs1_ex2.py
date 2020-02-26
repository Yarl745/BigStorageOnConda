import random
# 0
arr = [1, 2, 3, 4, 5]
tup = (arr[i] for i in range(len(arr)) if i % 2 == 0)
print(tuple(tup))

# 1
tup = (4.0, 3.2, 8.1, 3.14, 4.5)
arr = random.sample(tup, 2)
print(arr)

# 2
name = 'Yaroslav'
print('length: {};  last letter: {}'.format(len(name), name[-1:]))

# 3
name = 'Yaroslav'
upg_name = name[1:-1]
print(upg_name)

# 4
name = 'Yaroslav'
print(name[-1:])
