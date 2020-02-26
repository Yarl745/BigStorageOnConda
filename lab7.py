import os, shutil, random, re

path = 'C:\\lab7'
surname = 'Kopailo'
file_path = 'C:\\13.txt'
file_name_13 = '13.txt'
file_name_132 = '132.txt'
file_name_131 = '131.txt'


def getsubdir(*subdirs):
    final_path = path
    for subdir in subdirs:
        final_path += '\\' + subdir
    return final_path


# Creating dir with files
try:
    print('FILE 13.TXT SHOULD BE CREATED IN THE DISK C (C:\\13.txt)'.center(150, '='))

    # CREATION OF THE FILE AND DIRECTORIES
    os.mkdir(path)
    print('Directory {} is created!'.format(path))
    os.mkdir(getsubdir(surname))
    print('Directory {} is created!'.format(getsubdir(surname)))
    file13 = open(getsubdir(surname, file_name_13), 'w+')
    shutil.copyfile(file_path, getsubdir(surname, file_name_13))
    print('File {} is created and filled with data from the {}'.format(getsubdir(surname, file_name_13), file_path))


    # REVERSE TASK (132.TXT)
    arr_lines = file13.readlines()
    for l_index in range(len(arr_lines)):
        arr_words = arr_lines[l_index].split()
        for w_index in range(len(arr_words)):
            arr_letters = list(arr_words[w_index])
            random.shuffle(arr_letters)
            arr_words[w_index] = ''.join(arr_letters)
            pass
        arr_lines[l_index] = ' '.join(arr_words) + '\n'
    file132 = open(getsubdir(surname, file_name_132), "w+")
    file132.writelines(arr_lines)
    print('File {} is created!'.format(getsubdir(surname, file_name_132)))


    # CHANGE 13.TXT
    file13.seek(0)
    arr_lines = file13.readlines()
    file13.seek(0)
    file13.truncate()
    text = ''.join(arr_lines)
    arr_lines.clear()
    arr_lines = re.split("[\.?!]+|\n\s{0,}\n", text)
    for l_index in range(len(arr_lines)):
        arr_words = arr_lines[l_index].split()
        if len(arr_words) % 2 == 1:
            for w_index in range(len(arr_words)):
                if str.isalpha(arr_words[w_index]):
                    if len(arr_words[w_index]) % 2 == 0: break
                else:
                    other_symbol = 0
                    for letter in list(arr_words[w_index]):
                        if not str.isalpha(letter): other_symbol += 1
                    if ((other_symbol % 2 == 0 and len(arr_words[w_index]) % 2 == 0)
                            or (other_symbol % 2 == 1 and len(arr_words[w_index]) % 2 == 1)): break
            else:
                file13.write(arr_lines[l_index].replace('\n', '') + '\n')
    print('Data in file {} is changed!'.format(getsubdir(surname, file_name_13)))

    file13.close()
    file132.close()
    print('All files are closed properly!')
    # RENAME FILE 13.TXT TO 131.TXT
    os.rename(getsubdir(surname, file_name_13), getsubdir(surname, file_name_131))
    print('Name of the file {} is changed to {} properly'.format(getsubdir(surname,file_name_13), getsubdir(surname, file_name_131)))
except FileExistsError as fee:
    print(fee.strerror)
except Exception as err:
    print(str(err))
else: print('Files and all directories are created!')
