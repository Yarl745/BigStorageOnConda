import pprint

dictionary = {}


def add_or_open_word():
    new_word = input('Input new English word: ').lower().replace(' ', '')

    # END OF PROGRAM
    if new_word == 'exit' or new_word == '':
        print('DICTIONARY:')
        pprint.pprint(dictionary)
        exit()

    # WORD ALREADY EXISTS
    if new_word in dictionary:
        print('already exists\n' +
              '{0} - {1}'.format(new_word, dictionary[new_word]))
        add_or_open_word()

    # ADD NEW WORD
    dictionary[new_word] = []
    print('Enter empty field for closing adding translation')
    add_translation(new_word)

    # REPEAT ADDING
    add_or_open_word()


def add_translation(new_word):
    trans = input('Add translation: ')
    # IF NOT EMPTY FIELD
    if trans:
        dictionary[new_word] += [trans]
        add_translation(new_word)


def main():
    print('Print "exit" for closing program and showing dictionary')
    add_or_open_word()


if __name__ == '__main__':
    main()
