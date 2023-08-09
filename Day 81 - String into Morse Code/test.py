from tkinter import *

from pygame import mixer

mixer.init()
sound = mixer.Sound("beep sound\dah.wav")


def play():
    random_label = Label(text='this is random text')
    random_label.grid(row=1, column=0)
    for _ in range(5):
        sound.play()
        while mixer.get_busy():
            pass


root = Tk()
button = Button(root, text='Press', command=play, width=20)
button.grid(row=0, column=0)
root.mainloop()
