list_student={}

print("for stop just enter.")
while True:
    student=input("enter the name of the student:")
    if student==" ":
        break
    else:
        min_term=float(input("enter score of min term:"))
        term=float(input("enter score term:"))
        quize1=float(input("enter score quize one:"))
        quize2=float(input("enter score quize two:"))
        quize=(quize1+quize2)*5
        total_score=quize*0.25+(0.25*min_term)+(0.5*term)
        list_student.student=total_score
        continue


print("for stop just enter.")
while True:
    name=input("enter the student name:")
    if name==" ":
        break
    else:
        if name in list_student:
            score=list_student.get(name)
            if score>=90:
                print(f"{name}\ntotal score={score}->A")
            else:
                if 80<=score<90:
                    print(f"{name}\ntotal score={score}->B")
                else:
                    if 70<=score<80:
                        print(f"{name}\ntotal score={score}->C")
                    else:
                        if 60<=score<70:
                            print(f"{name}\ntotal score={score}->D")
                        else:
                            if score<60:
                                print(f"{name}\ntotal score={score}->E")
        else:
            print("sorry the name isn't avoible.")
            continue
         

            
