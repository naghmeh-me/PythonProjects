#1
from random import randint

sum_=0

n=1

score=0

try:
    guss=int(input("enter your guss:"))
except:
    print("error!enter a positive number.")
else:
     while n<=5:
        dice=input("roll a dice:")
        if dice=="":
            x=randint(1,6)
            print("dice:" , x)
            sum_+=x
            n+=1
            if x==6:
                print("horray!you earn agift.")
                dice=input("roll ypur gift:")
                if dice=="":
                    x=randint(1,6)
                    print("dice:" , x)
                    sum_+=x
                
                         

if guss==sum_:
    print(f"sum={sum_} ,you were right!")
    score+=guss
    print("your score:" , score)
elif sum_>guss:
    print(f"sum={sum_} , your guss is lower.")
    score=guss*5+(sum_-guss)
    print("your score:" , score)
else:
    print(f"sum={sum_} , you lost.")
    score=0
    print("your score:" , score)

#2 do nafare
from random import randint

sum_1=0

sum_2=0

n=1

score_player1=0

score_player2=0

try:
    name1=input("enter your name player number 1:")
    name2=input("enter your name player number 2:")
    guss1=int(input(f"enter your guss {name1}:"))
    guss2=int(input(f"enter your guss {name2}:"))
except:
    print("error!enter valid informations.")
else:
    while n<=5:
        dice1=input(f"roll a dice {name1}:")
        if dice1=="":
            x=randint(1,6)
            print("dice:" , x)
            sum_1+=x
            dice2=input(f"roll a dice {name2}:")
            if dice2=="":
                y=randint(1,6)
                print("dice:" , y)
                sum_2+=y
                n+=1
                if x==6:
                    print(f"horray!you earn a gift {name1}.")
                    dice1=input(f"roll your gift {name1}:")
                    if dice1=="":
                        x=randint(1,6)
                        print("dice:" , x)
                        sum_1+=x
                else:
                    if y==6:
                        print(f"horray! you earn a gift {name2}.")
                        dice2=input(f"roll your gift {name2}:")
                        if dice2=="":
                            y=randint(1,6)
                            print("dice:" , y)
                            sum_2+=y


if guss1==sum_1:
    print(f"sum dice {name1}={sum_1} ,you were right!")
    score_player1+=guss1
    print(f"{name1} score:" , score_player1)
else:
    if guss2==sum_2:
        print(f"sum dice {name2}={sum_2} , you were right!")
        score_player2+=guss2
        print(f"{name2} score:" , score_player2)
    else:
        if sum_1>guss1:
            print(f"sum dice {name1}={sum_1} , your guss is lower.")
            score_player1=guss1*5+(sum_1-guss1)
            print(f"{name1} score:" , score_player1)
        else:
            if sum_2>guss2:
                print(f"sum dice {name2}={sum_2} , your guss is lower.")
                score_player2=guss2*5+(sum_2-guss2)
                print(f"{name2} score:" , score_player2)
            else:
                if guss1>sum_1:
                    print(f"sum {name1}={sum_1} , you were wrong.")
                    score_player1=0
                    print(f"{name1} score:" , score_player1)
                else:
                    if guss2>sum_2:
                        print(f"sum {name2}={sum_2} , you were wrong.")
                        score_player2=0
                        print(f"{name2} score :" , score_player2)

print(f"total score {name1}:" , score_player1)
print(f"total score {name2} :" , score_player2)

if score_player1==score_player2:
    print("you are both winers.")
elif score_player1>score_player2:
    print(f"{name1} is the winner.\n{name2} is the lose:(")
else:
    print(f"{name2} is the winner.\n{name1} is the loser:(")
                        
    
                                
            
            
            
