from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def count_down(count):
    global check_mark
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(10, count_down, count - 1)
    else:
        start_action()
        check_mark = ""
        for _ in range(int(math.floor(reps / 2))):
            check_mark += "✔"
        check_marks.config(text=check_mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_action():
    start_button.config(state="disabled")
    global reps
    reps += 1

    if (reps % 8) == 0:
        label.config(text="Break")
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label.config(text="Break")
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text="Work")
        count_down(WORK_MIN * 60)


# ---------------------------- UI SETUP ------------------------------- #
def reset_action():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global check_mark
    check_mark = ""
    check_marks.config(text=check_mark)
    start_button.config(state="active")

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


def say_something(thing):
    print(thing)


#window.after(1000, say_something, "Hello")

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_action, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_action, highlightthickness=0)
reset_button.grid(row=2, column=2)
check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
