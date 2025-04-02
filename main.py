from question_model import Question
from data import question_data, alternative_question_data
from quiz_brain import QuizBrain

question_bank = []
## The default question database
# for question in question_data:
#     question_text = question['text']
#     question_answer = question['answer']
#     my_question = Question(question_text,question_answer)
#     question_bank.append(my_question)

## The alternative question database
for question in alternative_question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    my_question = Question(question_text,question_answer)
    question_bank.append(my_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz\n"
      f"Your final score was: {quiz.score}/{quiz.question_number}")
