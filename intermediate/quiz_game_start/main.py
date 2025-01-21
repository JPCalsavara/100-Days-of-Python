from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_box = []
for index in question_data:
    quest_text = index["question"]
    quest_answer = index["correct_answer"]
    question = Question(quest_text,quest_answer)
    question_box.append(question)

quiz = QuizBrain(question_box)

while quiz.is_still_question():
    quiz.next_question()

quiz.end_game()