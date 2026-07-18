number=0
turn=1

while number<=75:
    player=input("enter your number or hope:")
    if int(player)==turn:
        turn+=1
        print(turn)
        turn+=1
        if turn%5==0 and player=="hope":
            turn+=1
            print(turn)
            turn+=1
            if turn%5==0:
                print("hope")
                turn+=1
    else:
        print("sorry you lost.")
        break
