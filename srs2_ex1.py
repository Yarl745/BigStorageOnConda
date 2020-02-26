# 0
a = 121;
b = -34;
c = -0o77;
d = 0xf1
print('%#o' % a)
print('%#o' % b)
print('%#o' % c)
print('%#o' % d)

# 1
a = 17;
b = 20;
c = 1;
d = 9
print('%02d.%02d.%d%d' % (c, d, b, a))

# 2
a = [[1, 10], [2, -20]]
print('%d % d\n%d % d' % (a[0][0], a[0][1], a[1][0], a[1][1]))

# 3
a = 1, 2, 3, 4, 5, 6
print('%02d %02d %02d' % (a[0], a[2], a[4]))
print('%5.02d %02d %02d' % (a[1], a[3], a[5]))

# 4
a = "|"
b = "-"
print('%2s%-2s' % (b, b))
print('%-2s%2s' % (a, a))
print('%2s%-2s' % (b, b))

# 5
a = 1, 2, 3, 4
print('%2d' % (a[2]))
print('%-2d%2d' % (a[0], a[1]))
print('%2d' % (a[3]))
