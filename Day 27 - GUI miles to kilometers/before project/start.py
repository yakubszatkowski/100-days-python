from tkinter import *


def button_clicked():
    new_text = miles_amount.get()
    my_label.config(text=new_text)


# Tkinter introduction
window = Tk()
window.title('My first GUI')
window.minsize(500, 300)

# Setting up label
my_label = Label(text='I am a Label', font=('Calibri Light', 20, 'bold'))
# my_label.pack(side='left')  # it's rewritten later on
my_label['text'] = 'New text'  # ^ this is dictionary so this line changes its property
my_label.config(text='New text')  # or this
# my_label.pack['side'] = 'right'  # however this won't work because it's function

# Setting up button
button = Button(text='Click me!', command=button_clicked)
# button.pack(side='right')  #it's rewritten later on

# Setting up entry - which is gui input
miles_amount = Entry(width=10)
# miles_amount.pack()
miles_amount.get()

# # Layout managers besides .pack():
# # Place
# my_label.place(x=100, y=50)


# Grid
button.grid(column=1, row=1)
miles_amount.grid(column=2, row=2)

# Adding pad
window.config(padx=100, pady=100)
# Can also add pad around widgets
button.config(padx=50, pady=50)

window.mainloop()
