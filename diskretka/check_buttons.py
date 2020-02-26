from tkinter import *
# ----------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title('DichApp')
root.geometry('500x500')
# ----------------------------------------------------------------------------------------------------------------------
label = Label(root,
              bg='black', fg='white',
              font='Arial 20')
label.pack()
# ----------------------------------------------------------------------------------------------------------------------
def on_click():
    label['text'] = "I'm " + ' '.join([text for flag, text in check_data if flag.get()])
    # for flag, text in check_data: print('{} - {}'.format(flag.get(), text))
button = Button(root,
                font='Arial 12',
                text='Show Me',
                command=on_click)
button.pack()
# ----------------------------------------------------------------------------------------------------------------------
check_data = [(IntVar(), 'stupid'),
              (IntVar(), '...'),
              (IntVar(), 'crazy')
              ]
for flag, text in check_data:
    check = Checkbutton(root,
                        text=text,
                        variable=flag,
                        onvalue=1, offvalue=0,
                        font='Arial 12',
                         )
    check.pack(anchor=W)
# ----------------------------------------------------------------------------------------------------------------------
root.mainloop()