from tkinter import *
from pygame import mixer

mixer.init()
sound = mixer.Sound("beep sound\dah.wav")

morse_code = '____._ _____._._..___'

list_of_something = ['apple', 'banana', 'coconut']


# def sound_play(value):
#     for _ in list_of_something:
#         sound.play()
#         print(_)
#         while mixer.get_busy():
#             pass

def sound_play(list_of_something):
    for value in list_of_something:
        sound.play()
        print(value)
        # print('ok')
        while mixer.get_busy():
            pass


def play():
    random_label = Label(text='this is random text')
    random_label.grid(row=1, column=0)
    root.after(1, lambda: sound_play(list_of_something))


root = Tk()
root.geometry('300x300')
button = Button(root, text='Press', command=play, width=20)
button.grid(row=0, column=0)
root.mainloop()
