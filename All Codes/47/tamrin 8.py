#1
from random import randint
from random import choice

x=1

number=1

score=0

while x<=20:
    number1=randint(-9,9)
    coneshgar="+-*"
    number2=randint(-9,9)
    question=f"{number1}{choice(coneshgar)}{number2}"
    print(f"question{number}:({question})")
    answer=int(input("enter answer of question(number}:"))
    if eval(question)==answer:
        print("excelent!you were right.")
        score+=1
        x+=1
    else:
        print(f"sorry you were wrong.\nthe correct answer was {eval(question)}")
        x+=1

print(f"your score:{score} from 20")

#2
from random import randint
from random import choice

question=0
score=0

while question<=20:
    koneshgar="*+-"
    first_number=randint(-9,9)
    second_number=randint(-9,9)
    question_=f"{first_number}{choice(koneshgar)}{second_number}"
    
    try:
        print(f"Question {question}: {question_}")
        answer=int(input("Please enter your answer:"))
        question+=1
    except:
        print("Error! Please enter correct number.")
        question_=1
        continue
    else:
        if eval(answer)==eval(question_):
            score+=1
            print("Correct!")
        else:
            print("Wroung!")
            
print(f"Your total score: {score}.")