from morse_code_dictionary import morse_dict
from tkinter import *
from PIL import Image, ImageTk


class App:
    def __init__(self):
        # Initial interface
        self.frame2 = None
        self.root = Tk()
        telegraph_key_img = ImageTk.PhotoImage(Image.open('telegraph_key.png').resize((256, 256)))
        self.root.title('Morse code converter')
        self.root.geometry(
            f'400x450+{int(self.root.winfo_screenwidth() / 7)}+{int(self.root.winfo_screenheight() / 6)}')  # dimensions & positioning
        self.root.minsize(400, 450)
        self.root.maxsize(400, 450)
        self.root.config(pady=40, padx=40)

        # Empty variables
        self.input_text = None
        self.character_list = []
        self.morse_list = []
        self.frame2 = None

        # Execution
        self.user_interface(telegraph_key_img)
        self.root.mainloop()

    def translation_frame(self, final_char_list, final_morse_list, frame2):
        # Control
        print(f'{final_char_list} \n {final_morse_list}')

        # TODO - should it be another window or new frame?
        #  - one line first adjust font size of letters to morse code (morse code has to be way smaller)
        #  - evaluate how long should be the line
        #  - what can be done in this function or translate function to avoid making new line mid word?

        # Frame 3 - Adding frame with executed translation
        frame3 = Frame()
        frame3.place(in_=frame2, relx=-0.1, rely=1, y=20)

        # Cleaning the lists for the next usage
        self.character_list = []
        self.morse_list = []

    def translate(self, event=None):
        text = self.input_text.get()
        for character in text:
            if character in morse_dict:
                self.character_list.append(character.upper())
                self.morse_list.append(morse_dict.get(character))
            elif character == ' ':  # could've also added space to the dictionary itself lol
                self.character_list.append(' ')
                self.morse_list.append(' ')
            else:
                pass

        final_char_list = self.character_list
        final_morse_list = self.morse_list

        self.translation_frame(final_char_list, final_morse_list, self.frame2)

    def user_interface(self, telegraph_key_img):
        # Frame 1 - Canvas and title - initiating relative placement
        frame1 = Frame()
        frame1.place(relx=0.5, rely=0.3, anchor=CENTER)

        # Widgets inside of frame with grid placement
        title_label = Label(frame1, text='Morse Code Converter', font=('Calibri Light', 20, 'bold'))
        title_label.grid(row=1, column=0)

        canvas = Canvas(frame1, width=256, height=256)
        canvas.grid(row=0, column=0)
        self.root.update()
        canvas.create_image(canvas.winfo_width() / 2, canvas.winfo_height() / 2, image=telegraph_key_img)

        # Frame 2 - Label, Input box, execution button
        self.frame2 = Frame()
        self.frame2.place(in_=frame1, relx=-0.1, rely=1, y=20)

        # Widgets
        input_label = Label(self.frame2, text='Enter text for Morse code conversion', font=('Calibri Light', 12))
        input_label.grid(row=0, column=0)

        self.input_text = Entry(self.frame2, width=52)
        self.input_text.grid(row=1, column=0, pady=5)

        translate_button = Button(self.frame2, width=26, text='Translate', command=self.translate)
        translate_button.grid(row=2, column=0)
        self.root.bind("<Return>", self.translate)


if __name__ == "__main__":
    app = App()
