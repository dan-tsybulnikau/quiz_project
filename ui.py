from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = '#3375362'


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Trivia Quiz Game")
        self.window.config(bg='dark slate gray', padx=20, pady=20)
        
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,width=290, text="test", font=('Arial', 20, 'italic'))

        self.score_label = Label(bg='dark slate gray', font=('Arial', 12), fg='white')
        self.score_label.config(text="Score: 0")

        self.true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button()
        self.true_button.config(
            image=self.true_image,
            highlightthickness=0,
            command=self.answer_true)

        self.false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            command=self.answer_false
        )

        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            self.canvas.itemconfig(self.question_text, text="You have passed all questions!")
            self.window.after_cancel(self.get_next_question)

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg='green')
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_next_question)




