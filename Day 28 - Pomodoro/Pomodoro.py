from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text='Timer')
    check_mark.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    window.eval('tk::PlaceWindow . center')
    window.bell()
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 1:
        count_down(WORK_MIN)
        timer_label.config(text='Work', fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text='Break', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:  # or if len(str(count_sec) < 2:
        count_sec = str(f'0{count_sec}')
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    #else:
    start_timer()
    if reps % 2 == 0:
        check_mark['text'] += '✓'

        # or:
        # marks = ''
        # for _ in range(math.floor(reps/2)):
        #     marks += '✓'
        # check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.eval('tk::PlaceWindow . center')
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 109, image=tomato_img)
timer_text = canvas.create_text(100, 140, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(column=1, row=0)

check_mark = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
check_mark.grid(column=1, row=4)

start_button = Button(text='Start', width=6, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', width=6, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
