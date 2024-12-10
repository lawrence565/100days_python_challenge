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
rounds = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global rounds, timer
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text=f"00:00")
    time_label.config(text="Timer")
    rounds = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rounds
    rounds += 1

    if rounds == 8:
        times = LONG_BREAK_MIN
        time_label.config(text="Long Break", fg=RED)
    elif rounds % 2 == 0:
        times = SHORT_BREAK_MIN
        time_label.config(text="Short Break", fg=PINK)
    else:
        times = WORK_MIN
        time_label.config(text="Work", fg=GREEN)

    count_down(times * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    check_marks.config(text="")
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Formating the number
    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(rounds/2)):
            mark += "✔️"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

time_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
time_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="start", command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=3)

reset_btn = Button(text="reset", command=reset, highlightthickness=0)
reset_btn.grid(column=2, row=3)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)



window.mainloop()
