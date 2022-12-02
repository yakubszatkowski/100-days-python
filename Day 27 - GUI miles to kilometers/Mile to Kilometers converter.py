from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(100, 100)  # doesnt do much lol
window.eval('tk::PlaceWindow . center')
pad = 5
window.config(padx=20, pady=20)


def calculate():
    result = round(1.609344 * float(miles_amount.get()), 2)
    amount.config(text=result)


miles_amount = Entry(width=10)
miles_amount.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)
miles_label.config(padx=pad, pady=pad)

is_equal_label = Label(text='is equal to:')
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=pad, pady=pad)

amount = Label(text=0)
amount.grid(column=1, row=1)
amount.config(padx=pad, pady=pad)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)
km_label.config(padx=pad, pady=pad)

calculate_button = Button(text='Calculate',command=calculate)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=pad, pady=pad)

window.mainloop()
