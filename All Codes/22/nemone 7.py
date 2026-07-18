#1
from random import randint

while True:
    for i in range(3):
        coin=randint(1,2)
        print("head" if coin==1 else "tailes")
    ask=input("do you want to do this againe?:(yes/no)")
    if ask=="no":
        break
    else:
        continue

#2
from random import randint

while True:
    x = 0
    while x < 3:
        coin = randint(0,1)
        if coin == 0:
            coin ="Head"
            print(f"{coin}" , end =", ")
            x+=1
        else:
            coin = "Tail"
            print(f"{coin}" , end =", ")
            x+=1
        
    again = input("Do yoy want to do this again?(yes/no):")
    if again == "yes":
        continue
    else:
        print("It was fun let's do this again soon.")
        break
    
    
