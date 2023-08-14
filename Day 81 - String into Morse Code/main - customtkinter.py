import tkinter.messagebox
from morse_code_dictionary import morse_dict
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import textwrap
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # telegraph_key_img = ImageTk.PhotoImage(Image.open('telegraph_key.png').resize((256, 256)))
        self.title('Morse code converter')
        self.geometry(
            f'400x400+{int(self.winfo_screenwidth() / 7)}+{int(self.winfo_screenheight() / 8)}')  # 400x450
        self.minsize(400, 450)
        self.maxsize(500, 850)
        self.config(pady=50, padx=0)

        # Sound mixer
        mixer.init()
        self.long_beep = mixer.Sound("beep sound\dah.wav")
        self.short_beep = mixer.Sound("beep sound\dit.wav")

        # Empty variables
        self.input_text = None
        self.input_frame = None
        self.text = None
        self.text_and_translation_frame = Frame()
        self.copy_button = Button()

        # Execution
        self.user_interface()

    def user_interface(self):
        # Title frame consisting of picture and title
        title_frame = customtkinter.CTkFrame(self)
        title_frame.place(relx=0.5, y=110, anchor='center')  # relative width and fixed height

        title_label = customtkinter.CTkLabel(title_frame, text='Morse Code Converter', font=('Calibri Light', 20, 'bold'))
        title_label.grid(row=1, column=0)

        telegraph_key_img = customtkinter.CTkImage(Image.open('telegraph_key.png'), size=(256, 256))
        canvas = customtkinter.CTkLabel(title_frame, text="", image=telegraph_key_img)
        canvas.grid(row=0, column=0, padx=20, pady=10)

        # Input frame consisting of text label, input box and translation button
        self.input_frame = customtkinter.CTkFrame(self)
        self.input_frame.place(in_=title_frame, relx=-0.05, rely=1, y=20)

        input_label = customtkinter.CTkLabel(self.input_frame, text='Enter text for Morse code conversion', font=('Calibri Light', 12))
        input_label.grid(row=0, column=0, columnspan=2)

        self.update()
        self.input_text = customtkinter.CTkEntry(self.input_frame, width=int(title_frame.winfo_width()*1.1))
        self.input_text.grid(row=1, column=0, pady=5, columnspan=2)

        translate_button = customtkinter.CTkButton(self.input_frame, width=15, text='Translate', command=self.add_translation_frame)
        translate_button.grid(row=2, column=0)
        self.bind("<Return>", self.add_translation_frame)

        self.copy_button = customtkinter.CTkButton(self.input_frame, width=15, text='Copy', command=self.copy_translation)
        self.copy_button.grid(row=2, column=1)
        self.copy_button["state"] = "disabled"

    def add_translation_frame(self, event=None):
        self.text = self.input_text.get()
        self.text = self.text.lower()

        if len(self.text) == 0:
            return

        for widget in self.text_and_translation_frame.winfo_children():
            widget.destroy()
        self.text_and_translation_frame.destroy()

        # Translation frame
        self.text_and_translation_frame = customtkinter.CTkFrame(self)
        self.text_and_translation_frame.place(in_=self.input_frame, relx=-0.1, rely=1, y=20, x=3)

        text_in_lines = textwrap.fill(self.text, 17).split('\n')

        if len(text_in_lines) > 8:
            tkinter.messagebox.showwarning(title='Too many lines', message='Oops! Looks like your message is a bit too long to fit in the window. Please try a shorter message.')
            self.input_text.delete(0, 'end')
            return

        letter_row = 0
        for line in text_in_lines:
            letter_row += 2
            letter_column = 0
            for character in line:
                translation_row = letter_row + 1
                letter_label = Label(self.text_and_translation_frame, text=character.upper(),
                                     font=('Calibri Light', 12),
                                     width=2, height=1)

                letter_label.grid(row=letter_row, column=letter_column)
                translation_label = Label(self.text_and_translation_frame, text=morse_dict.get(character),
                                          font=('Calibri Light', 12), width=2,
                                          height=1)
                translation_label.grid(row=translation_row, column=letter_column)
                letter_column += 1

        self.update()
        self.geometry(f'400x{450 + self.text_and_translation_frame.winfo_height()}')
        self.update()
        self.copy_button["state"] = "active"
        self.play_morse_sound()

    def copy_translation(self):
        translated_text = "".join([morse_dict.get(letter, ' ') for letter in self.text])
        self.clipboard_clear()
        self.clipboard_append(f'{self.text.upper()}\n{translated_text}')

    def play_morse_sound(self):
        frame_elements = self.text_and_translation_frame.winfo_children()
        for index, widget in enumerate(frame_elements):
            if (index + 1) % 2 == 0:
                frame_elements[index - 1].config(bg="LightSkyBlue2")
                frame_elements[index].config(bg="LightSkyBlue2")
                self.update()
                singular_letter_morse = widget.cget('text')
                for character in singular_letter_morse:
                    if character == '.':
                        self.short_beep.play()
                    elif character == '_':
                        self.long_beep.play()
                    while mixer.get_busy():
                        pass
                frame_elements[index - 1].config(bg="LightSkyBlue1")
                frame_elements[index].config(bg="LightSkyBlue1")
                self.update()


if __name__ == "__main__":
    app = App()
    app.mainloop()
