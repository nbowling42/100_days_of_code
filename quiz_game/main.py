from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    answer = quiz.next_quetion()
    quiz.check_answer(answer)
