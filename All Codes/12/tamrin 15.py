#1
while True:
    n1=int(input("enter a number:"))
    n2=int(input("enter another number:"))
    if n2>n1:
        for i in range(n2,n1-1,-1):
            print(i)
        break
    else:
        print("عدد دوم بايد اذ عدد اول بزرگتر باشد.")
        break
    
#2
while True:
    number1 = int(input("Enter a number:"))
    number2 = int(input("Enter another number:"))
    
    if number2 > number1:
        for i in range(number2 , number1+1 , -1):
            print(i)
        again = input("Do you want to do this again?(yes/no):")
        if again == "yes":
            continue
        break
    else:
        print(f"{number1} is greater then {number2}.")
        break
        
