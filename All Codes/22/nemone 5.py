#1
print("for exit enter 0")

while True:
    try:
        number=int(input("entera number:"))
        if number%2==0:
            x="number is even"
        else:
            x="number is odd"
    except:
        print("error!please enter a valid number.")
        continue
    else:
        if number==0:
            break
        else:
            print(f"{number}-->lenght:{len(str(number))} and {x}")
            

#2
print("for exit enter 0")

def even_odd(number):
    if number%2==0:
        return "the number is even"
    else:
        return "the number is odd"

while True:
    try:
        number=int(input("enter a number:"))
        if number==0:
            break
    except:
        print("error!please enter a valid number.")
        continue
    else:
        len_number=len(str(number))
        print("lenght number is :" , len_number  , f"and {even_odd(number)}")
        

#3
while True:
    try:
        number = int(input("Enter a integer:"))
        if number == 0:
            print("It was fun, let's do it again soon.")
            break
    except:
        print("Please enter valid information.")
        continue
    else:
        if number < 0:
            print("Please enter a positive unteger.")
            continue
        else:
            len_number = len(str(number))
            if number % 2 == 0:
                print(f"{number} is even\nlen number:{len_number}")
            else:
                print(f"{number} is odd\nlen number:{len_number}")
                
        
