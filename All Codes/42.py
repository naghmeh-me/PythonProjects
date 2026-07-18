import os
import csv

def create_dict_players(list_players,list_scores):
    return {list_players[i]:list_scores[i] for i in range(len(list_players))}


def winner(dict_records):
    reverse_dict={}
    for key in dict_players:
        value_=dict_players[key]
        if value_ not in reverse_dict:
            reverse_dict[value_]=key
        else:
            reverse_dict[value_].append(key)
    keys=reverse_dict.keys()
    best_record=min(keys)
    return reverse_dict.get(best_record)
            
    

list_players=[]
list_scores=[]

print("foe exit gust press return bitton.")


while True:
    
    try:
        name=input("enter the name of the player:")
        if name=="":
            break
        score=float(input("enter scores of player:"))
    except ValueError:
        print("please enter valid information.")
        continue
    else:
        list_players.append(name)
        list_scores.append(score)
        continue

        
dict_players=create_dict_players(list_players,list_scores)
print("best record is for:",winner(dict_players))


enter=input("do you want to save information in a csv file?(y\n):")
if enter=='y':
    while True:
        try:
            name=input("enter the name of file :")
        except FileNotFoundError:
            print("please enter valid information.")
            continue
        else:
            if os.path.exists(name):
                with open(name,'w') as file:
                    write_=csv.writer(file)
                    write_.writerows(["player","score"])
                    for player , score in dict_players.items():
                        write_.writerows([player,score])
                    print("data imported siccessfully.")
                    break
            else:
                print("file dosnot exist.")
                continue
    
                

            

            
            
