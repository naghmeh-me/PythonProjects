def creat_participate_dict(list_names,list_records):
    participats_dict={list_names[i]:list_records[i] for i in range(len(list_names))}
    return participats_dict

def find_winner(participats_dict):
    winner=min(participats_dict,key=participats_dict.get)
    return winner ,participats_dict[winner]


print("for exit just enter:")

list_names=[]
list_records=[]

while True:
    name=input("enter the name:")
    if name=="":
        break
    else:
        list_names.append(name)
        record=float(input("enter the record:"))
        list_records.append(record)

participats_dict=creat_participate_dict(list_names,list_records)
winner_name,winner_record=find_winner(participats_dict)

print(f"winner:{winner_name} withh record:{winner_record}")
