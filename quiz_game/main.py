from question_bank_creator import QuestionBankCreator
from data import question_data
from quiz_brain import QuizBarin

#create a question bank from the data
question_bank = []
for i in question_data:
    #question is an obejct which has two attibutes "text" and "answer"
    question = QuestionBankCreator(i["text"], i["answer"])
    question_bank.append(question)

#create the quiz object
quiz = QuizBarin(question_bank)

while quiz.has_questions():
    quiz.next_question()

print("The Quiz has ended.")
print(f"Your Final Score is: ({quiz.score}/ {len(quiz.question_list)})")