from morse_code_dictionary import morse_dict
from tkinter import *
from PIL import Image, ImageTk


class App:
    def __init__(self):
        # Setting up initial interface
        gui = Tk()
        gui.title('Morse code converter')
        gui.geometry(f'600x400+{int(gui.winfo_screenwidth() / 7)}+{int(gui.winfo_screenheight() / 6)}')  # dimensions & positioning
        gui.minsize(400, 400)
        gui.maxsize(800, 800)
        gui.config(pady=40, padx=40)

        # Setting up the telegraph key on the canvas
        canvas = Canvas(width=200, height=200)
        telegraph_key_img = ImageTk.PhotoImage(Image.open('telegraph_key.png').resize((200, 200)))
        canvas.create_image(100, 100, image=telegraph_key_img)
        canvas.grid(column=0, row=0)
        # TODO input text to graphical morse code - letters and below them morse code

        # TODO input text to sound of morse code - play automatically, then leave play button

        # TODO highlight letters as the sound goes?

        gui.mainloop()


if __name__ == "__main__":
    app = App()
