import json

with open("bonus/questions.json", "r") as file:
    content = file.read()   
    data = json.loads(content)

score =0
for question in data:
    print(question["question_text"])
    for index,Answers in enumerate(question["Answers"]):
        print(index+1 , "-" ,Answers)

    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer
    if question["user_answer"] == question["correct_answer"]:
        score += 1

for index,question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score +=1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"


    message = f"{index + 1} - Your answer: {question['user_answer']}, "\
              f"{index + 1} - Correct answer: {question['correct_answer']}"
    
    print(message)

print(data)
print(score,"/", len(data))
