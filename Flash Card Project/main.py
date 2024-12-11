from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
LAN_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}

# ------------------- Load data ------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    to_learn = pandas.read_csv("./data/french_words.csv")
    to_learn_dict = to_learn.to_dict(orient="records")
else:
    to_learn_dict = data.to_dict(orient="records")

# ------------------- machinism ------------------- #
def update_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    canvas.itemconfig(card_img, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    global current_card
    to_learn_dict.remove(current_card)
    to_learn_data = pandas.DataFrame(to_learn_dict)
    to_learn_data.to_csv("./data/words_to_learn.csv", index=False)
    update_card()

def flip_card():
    global current_card
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

# ------------------- UI Setting ------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Load image file
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

# Paint the canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="French", font=LAN_FONT, fill="black")
card_word = canvas.create_text(400, 263, text="trouve", font=WORD_FONT, fill="black")
canvas.grid(column=0, row=0, columnspan=2)

# Button
check_btn = Button(image=right, command=update_card ,highlightthickness=0)
check_btn.grid(column=1, row=1)
unknown_btn = Button(image=wrong, command=update_card ,highlightthickness=0)
unknown_btn.grid(column=0, row=1)


window.mainloop()