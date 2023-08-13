from tkinter import *
from pygame import *
from morse_code_dictionary import morse_dict

mixer.init()
short_beep = mixer.Sound('beep sound\dit.wav')
long_beep = mixer.Sound('beep sound\dah.wav')


def sound_conversion(code):
    for character in code:
        if character == '.':
            short_beep.play()
        elif character == '_':
            long_beep.play()
        while mixer.get_busy():
            pass


def play_morse_sound(frame_objects):
    for index, widget in enumerate(frame_objects):
        if (index + 1) % 2 == 0:
            code = widget.cget('text')
            root.after(1, sound_conversion, code)


def translate():
    text = input_text.get()
    translation_frame = Frame()
    translation_frame.grid(row=2, column=0)

    start_column = 0
    for char in text:
        letter = Label(translation_frame, text=char)
        letter.grid(row=3, column=start_column)
        translation = Label(translation_frame, text=morse_dict.get(char))
        translation.grid(row=4, column=start_column)
        start_column += 1
    root.update()
    frame_elements = translation_frame.winfo_children()
    root.after(1, play_morse_sound, frame_elements)


root = Tk()
root.geometry('300x300')
root.config(padx=50, pady=50)

input_text = Entry(width=30)
input_text.insert(0, 'o')
input_text.grid(row=0, column=0)

button = Button(width=15, text='Translate', command=translate)
button.grid(row=1, column=0)

root.mainloop()
