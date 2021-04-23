from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#8fd9a8"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_count = None


def reset_all():
    global reps
    window.after_cancel(timer_count)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg="white")
    check_marks.config(text="")
    reps = 0



def reset():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg="white")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg="white")
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=RED)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count - 1)
    else:
        reset()
        marks = ""
        working_session = math.floor(reps/2)
        for _ in range(working_session):
            marks += "✔"
        check_marks.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=2, column=2)

timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg="white")
timer.grid(row=1, column=2)

start_button = Button(text="Start", bg="#ff7171", font=(FONT_NAME, 12, "bold"), fg="white", highlightthickness=0,
                      command=reset)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", bg="#ff7171", font=(FONT_NAME, 12, "bold"), fg="white", highlightthickness=0,
                      command=reset_all)
reset_button.grid(row=3, column=3)

check_marks = Label(bg=YELLOW, fg="#295939", font=(FONT_NAME, 12, "bold"))
check_marks.grid(row=4, column=2)

window.mainloop()
