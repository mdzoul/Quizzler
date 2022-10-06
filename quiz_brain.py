class QuizBrain:
	
	def __init__(self, q_list):
		self.question_number = 0
		self.question_list = q_list
		self.score = 0
		
	def still_has_questions(self):
		return self.question_number < len(self.question_list)
	
	def next_question(self):
		current_question = self.question_list[self.question_number]
		print(f"\33[34;4m{current_question.category}\33[0m")
		self.question_number += 1
		user_answer = input(f"Q.{self.question_number}: {current_question.text}\n(\33[32mTrue\33[0m/\33[31mFalse\33[0m)? ")
		self.check_answer(user_answer, current_question.answer)
		
	def check_answer(self, user_answer, correct_answer):
		if user_answer.lower() == correct_answer.lower():
			print("\n\33[32mYou got it right!\33[0m")
			self.score += 1
		else:
			print("\n\33[31mThat's wrong.\33[0m")
		print(f"The correct answer: \33[1m{correct_answer}\33[0m.")
		print(f"Your current score: \33[31m{self.score}\33[0m/{self.question_number}\n")
		