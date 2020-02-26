f = "Грає море зелене, Тихий день догора"
# 0
b1 = bytes(f, 'cp1251')
b2 = bytes(f, 'utf-8')
print(b1, b2, sep='\n')
print('len b2 > b1 ({} > {})'.format(len(b2), len(b1)), '\n')

# 1
b_ar = bytes(f, 'cp1251')
d_ar = bytes([int(b)-1 for b in b_ar])
print(str(d_ar, 'cp1251'), '\n')

# 2
b = bytes(f, 'utf-8')
b_ar = bytearray(b)
b_ar.reverse()
print(b_ar.decode('cp1251'), '\n')

#3
ch_arr = list(f)
hex_arr = [hex(ch.encode('cp1251')[0]) for ch in ch_arr]
hex_str = ''.join(hex_arr).replace('0x', '')
print(str(bytes.fromhex(hex_str), 'cp1251'), '\n')

# 4
b_old = bytearray(f, 'cp1251')
b_new = bytearray([b_old[index] for index in range(0, len(b_old), 2)])
b_old = bytearray([b_old[index] for index in range(1, len(b_old), 2)])
print(str(b_old, 'cp1251'))
print(bytearray.decode(b_new, 'cp1251'), '\n')

# 5
f_arr = f.split(',')
f_arr = [list(bytes(line, 'cp1251')) for line in f_arr]
full_arr = [f_arr[i][j] for i in range(len(f_arr)) for j in range(len(f_arr[i]))]
print(bytearray.decode(bytearray(full_arr), 'cp1251'))





pass



