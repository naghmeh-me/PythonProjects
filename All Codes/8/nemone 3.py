#1
number=input("عددي يک يا دو رقمي وارد کنيد:")

if len(number)==1:
    if int(number)%2==0:
        print("e1")
    if int(number)%2!=0:
        print("o1")
elif len(number)==2:
    if int(number)%2==0:
        print("e2")
    if int(number)%2!=0:
        print("o2")
else:
    print("error! عدد بايد يک يا دو رقمي باشد")

#2
while True:
    number = input("Enter a random number:")
    
    if len(str(int(number))) == 1:
        if int(number) % 2 == 0:
            print("e1")
        else:
            print("o1")
    elif len(str(int(number))) == 2:
        if int(number) % 2 == 0 :
            print("e2")
        else:
            print("o2")
    else:
        print("Error! enter a one-digit or two-digit number")
        continue
    
    end = input("Do you want to do this again:(yes/no):")
    if end == "yes":
        continue
    break
    
