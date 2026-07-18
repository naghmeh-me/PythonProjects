#in code ghalate
score=0
wroung_guss=0

card=("1 2 3 4 5 6 7 8 9 10")

shuffle_card=list(set((card.strip()).split()))

guss_player=input("enter your gusss:")
guss_player=(guss_player.strip()).split()

if guss_player==shuffle_card:
    print("amazing!")
    print("you won.")
    print("cards:",shuffle_card,"\nyour guss:",guss_player,"\nyour score:",score)
else:
    if shuffle_card[0]==guss_player[0]:
        score+=1
        print("your first guss was correct.")
    else:
        wroung_guss+=1
        if shuffle_card[1]==guss_player[1]:
            score+=1
            print("your second guss was correct.")
        else:
            wroung_guss+=1
            if shuffle_card[2]==guss_player[2]:
                score+=1
                print("your third guss was correct.")
            else:
                wroung_guss+=1
                if shuffle_card[3]==guss_player[3]:
                    score+=1
                    print("youe forth guss was correct.")
                else:
                    wroung_guss+=1
                    if shuffle_card[4]==guss_player[4]:
                        score+=1
                        print("your fifth guss was correct.")
                    else:
                        wroung_guss+=1
                        if shuffle_card[5]==guss_player[5]:
                            score+=1
                            print("your sixth guss was correct.")
                        else:
                            wroung_guss+=1
                            if shuffle_card[6]==guss_player[6]:
                                score+=1
                                print("your seventh guss was correct.")
                            else:
                                wroung_guss+=1
                                if shuffle_card[7]==guss_player[7]:
                                    score+=1
                                    print("your eights guss was correct.")
                                else:
                                    wroung_guss+=1
                                    if shuffle_card[8]==guss_player[8]:
                                        score+=1
                                        print("your nineths guss was correct.")
                                    else:
                                        wroung_guss+=1
                                        if shuffle_card[9]==guss_player[9]:
                                            score+=1
                                            print("your last guss was correct.")
                                        else:
                                            wroung_guss+=1

                                            
if wroung_guss>=3:
    print("sorry you lost.")
    print("cards:",shuffle_card,"\nyour guss:",guss_player,"\nyour score:",score)
else:
    print("you won.")
    print("cards:",shuffle_card,"\nyour guss:",guss_player,"\nyour score:",score)





