from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

logo()

question_bank = []
for question in question_data:
	question_text = question["question"]
	question_answer = question["correct_answer"]
	category = question["category"]
	new_question = Question(category=category, q_text=question_text, q_answer=question_answer)
	question_bank.append(new_question)
	
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\33[1;4mYou've completed the quiz!\33[0m")
if quiz.score == quiz.question_number:
    print(f"Your final score: \33[32m{quiz.score}\33[0m/\33[34m{quiz.question_number}\33[0m")
else:
    print(f"Your final score: \33[31m{quiz.score}\33[0m/\33[34m{quiz.question_number}\33[0m")
