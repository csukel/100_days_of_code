from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
import html

params = {
    "amount" : 10,
    "type" : "boolean"
}
res = requests.get("https://opentdb.com/api.php", params=params)
res.raise_for_status()

data = res.json()
question_bank = []
for question in data["results"]:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
