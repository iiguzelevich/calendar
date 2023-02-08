from tkinter import *

import calendar


def click():
    year_g = year.get()
    a = calendar.TextCalendar(firstweekday=0)

    lbl_1 = Label(
        window,
        text=f'{a.formatyear(int(year_g), w=2, l=1, c=6, m=3)}',
        font='Terminal 10',
        justify=LEFT
    )
    lbl_1.pack(side="top", fill="x", expand=False)


window = Tk()

window.geometry('600x700')

lbl = Label(window, text='Год: ', justify='left')
lbl.pack(side="top", fill="x", expand=False)

year = Entry(window, width=10,)
year.pack(side="top", fill="x", expand=False)

btn = Button(window, text='Ввод', command=click)
btn.pack(side="top", fill="x", expand=False)
window.mainloop()
