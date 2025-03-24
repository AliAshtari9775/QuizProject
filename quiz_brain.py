class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        new_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q {self.question_number}. {new_q.text}.(True/False)?:").lower()
        correct_answer = new_q.answer
        self.check_answer(user_answer, correct_answer)


    def check_answer(self, input_answer, correct_answer):
        if input_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Current score: {self.score}/{self.question_number}.")
        print("\n")
