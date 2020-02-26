# 0
sum = 0
for dig in range(0, 21, 2): sum += dig*2
print(sum)

# 1
sum = 0
for dig in range(0, -21, -2): sum += dig**2
print(sum)

# 2
name = 'Yaroslav'
s = ''
for i in range(0, len(name), 2): s += name[i]
print(s)

# 3
name = 'Yaroslav'
s = ''
for i in range(1, len(name), 2): s += name[i]
print(s)

# 4
fact = 1
for dig in range(2, 6): fact *= dig
print(fact)
