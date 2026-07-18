number=int(input("enter a number:"))

if number%2==0 and number%3==0:
    print("بر هر دو بخش پذير است")
else:
    if number%2==0 and number%3!=0:
        print("فقط بر دو بخش پذير است")
    else:
        if number%2!=0 and number%3==0:
            print("فقط بر 3 بخش پذير است")
        else:
            if number%2!=0 and number%3!=0:
                print("بر هيچ کدام بخش پذير نيست")
#2
while True:
    number = int(input("Enter the number:"))
    if number < 0:
        print("Please enter a positive number.")
        continue
    else:
        if number % 2== 0  and number % 3 == 0:
            print(f"{number} is divisible by two and three.")
        else:
            if number % 2 == 0:
                print(f"{number} is devisible by two.")
            else:
                if number % 3 == 0:
                    print(f"{number} is divisible by three.")
                else:
                    print(f"{number} is not divisible by two or three.")
                
    again = input("Do you want to do this again?(yes/no):")
    if again == "yes":
            continue
    else:
        print("It was fun let's do it again soon.")
        break
                
    
