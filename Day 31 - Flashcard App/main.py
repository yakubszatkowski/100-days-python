from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Reading database of words #
try:
    data = pandas.read_csv('./data/words to learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')

data = data.to_dict(orient='records')
current_card = {}
learned_words_list = []


# Additional button functions #
def next_and_remove_card():
    data.remove(current_card)
    next_card()


# Card flip #
def card_flip():
    canvas.itemconfig(card, image=img_card_back)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')


# Press button option #
def next_card():
    global current_card, flip_timer
    # if you press next card too many times timer doesn't cancel and line below prevents it
    window.after_cancel(flip_timer)
    new_word = random.choice(data)
    current_card = new_word
    canvas.itemconfig(card, image=img_card_front)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=new_word['French'], fill='black')
    flip_timer = window.after(3000, card_flip)


# UI #
window = Tk()
window.title('Flashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, card_flip)

img_card_front = PhotoImage(file='./images/card_front.png')
img_card_back = PhotoImage(file='./images/card_back.png')
img_correct_button = PhotoImage(file='./images/right.png')
img_wrong_button = PhotoImage(file='./images/wrong.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=img_card_front)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'italic'))

correct_button = Button(image=img_correct_button, highlightthickness=0, command=next_and_remove_card)
correct_button.grid(column=1, row=1)
unknown_button = Button(image=img_wrong_button, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

# Starts the program #
next_card()

window.mainloop()
# Saves data to csv #
words_to_learn = pandas.DataFrame(data)
words_to_learn.to_csv('./data/words to learn.csv', index=False)
