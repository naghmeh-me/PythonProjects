x=0

name1=input("enter your name player number one:")
name2=input("enter your name palyer number two :")

score1=0
score2=0

print("1=ciser\n2=paper\n3=stone")

while x<5:
    x+=1
    print(f"Round{x}:")
    player1=int(input(f"enter the number {name1}:"))
    player2=int(input(f"enter the number {name2}:"))
    if player1==player2:
        print("Equal")
        continue
    else:
        if player1==1 and player2==2:
            score1+=1
            print(f"{name1} win this round.")
            continue
        else:
            if player1==1 and player2==3:
                score2+=1
                print(f"{name2} win this round.")
                continue
            else:
                if player1==2 and player2==1:
                    score2+=1
                    print(f"{name2} win this round.")
                    continue
                else:
                    if player1==2 and player2==3:
                        score1+=1
                        print(f"{name1} win this round.")
                        continue
                    else:
                        if player1==3 and player2==1:
                            score1+=1
                            print(f"{name1} win this round.")
                            continue
                        else:
                            if player1==3 and player2==2:
                                score2+=1
                                print(f"{name2} win this round.")
                                continue

print(f"{name1}:{score1}\n{name2}:{score2}")
if score1>score2:
    print(f"{name1} won.")
else:
    if score1<score2:
        print(f"{name2} won.")
    else:
        print("no one win you are both equal.")
                
                    
            
