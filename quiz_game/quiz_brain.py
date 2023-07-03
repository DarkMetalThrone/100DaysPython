class QuizBarin:
    def __init__(self, question_list) -> None:
        """initialise the question bank object into the quiz brain object"""
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def has_questions(self):
        """returns true if the current question number is less than or equal to the length of question bank"""
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        """goes to the next questions and checks answers"""
        ans = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}? (True/ False): ")
        # check if the answer is correct
        self.check_answer(ans, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, answer, correct_answer):
        """checks the answers and prints the score"""
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it Right!")
        else:
            print("You got it Wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your Score is ({self.score}/ {self.question_number + 1})")
        print("\n")