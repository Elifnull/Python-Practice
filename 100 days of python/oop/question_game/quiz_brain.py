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
        print(f"Category: {current_question.category}, Difficulty: {current_question.difficulty}")
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ").lower()
        if answer == "off":
            """end loop early feature"""
            self.question_number = len(self.questions_list)
        self.question_number += 1
        self.check_answer(answer, current_question.answer)
        return answer

    def check_answer(self, question, answer):
        if question == answer:
            self.score += 1
            print("You got it right!")
        else:
            self.score += 0
            print("You got it wrong")
        print(f'Your score: {self.score}/{self.question_number}\n')
