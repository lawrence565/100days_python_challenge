from spyder.config.gui import set_font
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuestionUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question text", width=280,
                                                     font=("Ariel", 20, "italic"), fill="black")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_btn_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_btn_img, bg=THEME_COLOR, padx=30, pady=30, command=self.true_pressed, highlightthickness=0)
        self.true_btn.grid(column=1, row=2, pady=20)

        false_btn_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_btn_img, bg=THEME_COLOR, padx=10, pady=10, command=self.false_pressed, highlightthickness=0)
        self.false_btn.grid(column=0, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        is_right =  self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.canvas.itemconfig(self.question_text, fill="white")
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)


