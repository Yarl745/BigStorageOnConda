import dict_lab6


class Dictionary:
    def __init__(self, diction):
        self.diction = diction
        print('Kopailo Dictionary'.center(50, '-'))
        print('Для виходу введіть: STOP'.center(50))
        self.get_word()

    def get_word(self):
        print('{0:<20}'.format('Введіть англійьке слово:'), end=' ')
        self.eng_word = str(input()).lower().replace(' ', '')
        if self.eng_word == 'stop':
            print('Кiнець програми'.center(50, '-'))
        else:
            self.get_translate()

    def get_translate(self):
        if self.eng_word in self.diction:
            print('{0:5} {1}'.format('', self.eng_word))
            for translation in self.diction[self.eng_word]:
                print('{0:20}{1:<30}'.format('', translation))
        else:
            print('Це слово вiдсутнє в базi словаря...')
        self.get_word()


if __name__ == '__main__':
    Dictionary(dict_lab6.diction)
