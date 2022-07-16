from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for index, content in enumerate(question_data):
    """loop added question objects into list, each index is new question object"""
    question_text = content["text"]
    question_answer = bool(content["answer"])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
