#1
from random import randint

print("for exit enter 0")

point=0

wrong_guss=0

def chance():
    chance=randint(1,1000)
    return chance

while True :
    try:
        number=int(input("enter a number between 1 to 1000:"))
    except:
        print("please enter a valid number.")
        continue
    else:
         if number==00:
             print(" amount off your wrong gusses:" , wrong_guss ,"\nyour final score:" , point)
             break
         elif number<0:
            print("error!please enter a positive number.")
            continue
         else:
             if number==chance():
                 print(f"number was {chance()} and you were right!")
                 point+=1
                 print(f"your point:{point}.")
                 continue
             else:
                 if number>chance():
                     print(f"number was {chance()}, you said higher!")
                     wrong_guss+=1
                     continue
                 else:
                     if number<chance():
                         print(f"number was {chance()}, you said lower!")
                         wrong_guss+=1
                         continue

