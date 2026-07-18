from random import randint
from random import choice
#print("For start press enter, but for exite from the program enter 0(zero).")

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