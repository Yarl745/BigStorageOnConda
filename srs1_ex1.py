# Всё это будет работать из-за приведения типов (False = 0, True = 1)
# 0
print(False - True) #-1

# 1
print(True * (-True)) #-1

# 2
print(2 * (-True)) #-2

# 3
a = 2 * (-True)
a += 6
print(a) #4

# 4
a = 6
a -= True
print(a) #5

