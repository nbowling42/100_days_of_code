class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def next_quetion(self):
        question = self.question_list[self.question_number].text
        self.question_number += 1
        return input(f"\nQ.{self.question_number}: {question} (True/False)?: ").title()
        
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, answer):
        index = self.question_number - 1
        correct_answer = self.question_list[index].answer

        if correct_answer == answer:
            self.score += 1
            print(f"Correct! Current Score: {self.score}/{self.question_number}")
        else:
            print(f"Incorrect. Current Score: {self.score}/{self.question_number}")
