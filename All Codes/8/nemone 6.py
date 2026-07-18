#1
grade=float(input("enter the grade:"))

if 80<=grade<=100:
    print("A")
elif 60<=grade<80:
    print("B")
elif 40<=grade<60:
    print("C")
elif 20<=grade<40:
    print("D")
elif grade<20:
    print("fail")
else:
    print("error!\nthe grade must be higher than 0 and smaller than one hundered.")

#2
while True:
    print("for brake enter end.")
    grade = float(input("Enter the student grade(between 0 to 100):"))
    
    if grade == "end":
        break
    elif grade<0 or grade>100:
        print("Error!")
        continue
    elif 0<=grade<=40:
        print("fail!")
    elif 40<=grade<=70:
        print("C")
    elif 70<=grade<=90:
        print("B") 
    else:
        print("A")   

