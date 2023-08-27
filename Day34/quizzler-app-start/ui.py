from tkinter import *
from quiz_brain import QuizBrain
from functools import partial

THEME_COLOR = "#375362"
TEXT_FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lbl_score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.lbl_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_id = self.canvas.create_text(
            150, 125, font=TEXT_FONT, text="Question", fill=THEME_COLOR, width=280
        )
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        correct_img = PhotoImage(file="Day34/quizzler-app-start/images/true.png")
        wrong_img = PhotoImage(file="Day34/quizzler-app-start/images/false.png")
        self.btn_correct = Button(image=correct_img, highlightthickness=0)
        self.btn_correct.grid(column=0, row=2)
        self.btn_correct.config(command=partial(self.check_answer, "True"))
        self.btn_wrong = Button(image=wrong_img, highlightthickness=0)
        self.btn_wrong.grid(column=1, row=2)
        self.btn_wrong.config(command=partial(self.check_answer, "False"))
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_id, text=question)
        else:
            self.canvas.itemconfig(
                self.question_id, text="You have reached the end of this quiz!!"
            )
            self.btn_correct.config(state="disabled")
            self.btn_wrong.config(state="disabled")

    def check_answer(self, answer: str) -> None:
        is_correct: bool = self.quiz.check_answer(answer)
        if is_correct:
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

        # self.get_next_question()
