from tkinter import *
import random

class Main_display:
    def __init__(self, width=500, height=500):
        self.root = Tk()
        self.root.geometry('{}x{}'.format(width, height))
        self.button = Button(self.root,
                             font='Arial 14',
                             command=self.get_randoms,
                             text='Get Random Numbers',
                             bg='black', fg='white')
        self.text = Text(self.root,
                         font='Arial 20',
                         bg='white', fg='red',
                         wrap=WORD,
                         state=DISABLED)
        self.entry = Entry(self.root,
                           font='Arial 18',
                           bg='grey', fg='white')
        self.entry.pack(fill=X)
        self.button.pack(fill=X)
        self.text.pack(fill=BOTH)
        self.root.mainloop()

    def get_randoms(self):
        self.text.config(state=NORMAL)
        self.text.delete(0.0, END)
        try:
            numb_randoms = int(self.entry.get())
        except ValueError:
            self.text.insert(END, 'Введите целое число')
        else:
            self.text.insert(END, [random.randint(1, 100) for i in range(numb_randoms)])
        self.entry.delete(0, END)
        self.text.config(state=DISABLED)


Main_display()