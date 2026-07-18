from random import randint

score=0

while True:
    x=randint(1,2)
    if x==1:
        coin="head"
    else:
        coin="tail"
    guss=input("enter your guss(tail/head):")
    if guss==coin:
        print("coin:" , coin , "\nyou were right!")
        score+=1
        continue
    else:
        print("coin:" , coin , "\nyou were wrong!" , "\nscore:" ,score)
        again=input("do you want to play again?(yes/no):")
        if again=="yes":
            continue
        else:
            break

        
        
    
