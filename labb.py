def get_sh(text):
    return ''.join([chr(ord(char)+13) for char in text])


def get_unsh(text):
    return ''.join([chr(ord(char)-13) for char in text])


status = input('... ')
text = input('input: ')
if status == 'sh':
    print(get_sh(text))
elif status == 'unsh':
    print(get_unsh(text))
else: print("it's fucking status...")
