from tabnanny import check


class QuizBrain:

    def __init__(self, q_list):
        self.quiz_number = 0
        self.quiz_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.quiz_number < len(self.quiz_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.quiz_list[self.quiz_number]
        self.quiz_number += 1
        user_answer = input(f"Q.{self.quiz_number}: {current_question.text}? (True/False): ")
        self.check_answer(current_question, user_answer)

    def check_answer(self, question, answer):
        if answer.lower() == question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You're wrong!")
            print(f"The correct answer is {question.answer}")