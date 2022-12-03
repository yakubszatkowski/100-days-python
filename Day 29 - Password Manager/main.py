from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 5)
nr_numbers = random.randint(2, 5)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_generator():
    password_entry.delete(0, 'end')
    password = []
    password += [random.choice(letters) for _ in range(nr_letters)] \
                + [random.choice(numbers) for _ in range(nr_numbers)] \
                + [random.choice(symbols) for _ in range(nr_numbers)]
    random.shuffle(password)
    final_password = ''.join(password)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    if website_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror(title='Error!', message='You\'ve left empty spaces.')
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f'There are the details entered:'
                                                                          f'\n Email/username: {username_entry.get()}'
                                                                          f'\n Password: {password_entry.get()}'
                                                                          f'\n Do you want to save?')
        if is_ok:
            with open('User passwords.txt', 'a') as file:
                file.write(f'{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n')
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- LAST E-MAIL INSERT ------------------------------- #
with open('User passwords.txt') as file_open:
    contents = file_open.read().split()
    if len(contents) > 4:
        last_email = contents[-3]
    else:
        last_email = ''
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.eval('tk::PlaceWindow . center')
window.config(pady=40, padx=40)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Row 1
website_label = Label(text='Website: ')
website_label.grid(column=0, row=1)
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Row 2
username_label = Label(text='Email/Username: ')
username_label.grid(column=0, row=2)
username_entry = Entry(width=52)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, last_email)

# Row 3
password_label = Label(text='Password: ')
password_label.grid(column=0, row=3)
password_entry = Entry(width=33)  # show='*'
password_entry.grid(column=1, row=3)
generate_button = Button(text=' Generate Password', command=random_generator)
generate_button.grid(column=2, row=3)

# Row 4
add_button = Button(text='Add', width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
