import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in data.question_data:
    question = Question(i["text"], i["answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()
    print(f"Your current score is {quiz_brain.score}/{quiz_brain.quiz_number}\n")

print("You've completed the quiz!")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.quiz_number}")