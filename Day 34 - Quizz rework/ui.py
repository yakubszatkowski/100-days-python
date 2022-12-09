from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface(Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super(QuizInterface, self).__init__()
        self.title('Quizzler')
        self.eval('tk::PlaceWindow . center')
        self.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz_brain

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280, text=f'',
                                                     fill=THEME_COLOR, font=('Arial', 20, 'italic'))

        self.score_label = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        false_img = PhotoImage(file='./images/false.png')
        true_img = PhotoImage(file='./images/true.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false)
        self.false_button.grid(column=1, row=2)
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'ve reached the end of the quiz!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        elif not is_right:
            self.canvas.config(bg='red')
        self.after(1000, self.get_next_question)
