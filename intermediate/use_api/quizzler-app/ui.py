from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR,fg="white",font=("Arial",15))
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250,highlightthickness=0,bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some text",
            fill=THEME_COLOR,
            font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image,highlightthickness=0,command=self.right_print)
        self.right_button.grid(column=0,row=2)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0,command=self.wrong_print)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_print(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_print(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)


