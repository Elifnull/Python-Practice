class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        # simplified return statement will output bool
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False):").lower()
        self.question_number += 1
        print(answer)
        return answer

    def check_answer(self, question, answer):
        pass
