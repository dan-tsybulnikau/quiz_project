from data import question_data
import random
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []


def create_question_bank():
    data = question_data
    while data:
        random_question = random.choice(data)
        question = Question(random_question["question"], random_question["correct_answer"])
        question_bank.append(question)
        data.remove(random_question)


create_question_bank()
quiz_brain = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz_brain)



