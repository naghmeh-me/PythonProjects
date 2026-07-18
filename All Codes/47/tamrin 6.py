#1
from time import sleep

x=1

while x<=3:
    print(f"\nRound{x}")
    for i in range(1,6):
        sleep(1)
        print(i , end=" ")
    x+=1

#2
from time import sleep

print("For start press enter, but for exite from the program enter 0(zero).")

x=0
round_=0

while x<=3:
    try:
        text=input("Start:")
        x+=1
    except:
        print("Error!")
        continue
    else:
        if text=="0":
            break
        else:
            if text=="":
                round_+=1
                print(f"Round {round_}" , end=":")
                for i in range(1,6):
                    print(i , end=",")
                    sleep(1)
                continue