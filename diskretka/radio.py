from tkinter import *

# ----------------------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry('500x500')
# ----------------------------------------------------------------------------------------------------------------------
label = Label(root,
              text='My favourite language is',
              font='Arial 20')
label.pack(anchor=W)
# ----------------------------------------------------------------------------------------------------------------------
label_language = Label(root,
                       font='Arial 30',
                       bg='black', fg='white')
label_language.pack(anchor=W)
# ----------------------------------------------------------------------------------------------------------------------
var = IntVar()
radio_data = [(0, 'Python'), (1, 'JS'), (2, 'Java'), (3, 'C++'), (4, 'C#')]
def on_radio_click():
    label_language['text'] = radio_data[var.get()][1]
for val, lang in radio_data:
    radio = Radiobutton(root,
                        variable=var,
                        value=val,
                        text=lang,
                        font='Arial 15',
                        command=on_radio_click)
    radio.pack(anchor=W)
# ----------------------------------------------------------------------------------------------------------------------
root.mainloop()
