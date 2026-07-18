#1
while True:
    name=input("enter full name:")
    scores=input("enter scores:")
    scores=scores.strip()
    list_scores=scores.split()
    for index in range(len(list_scores)):
        list_scores[index]=float(list_scores[index])
    sum_scores=sum(list_scores)
    average=sum_scores/len(list_scores)
    print(f"name:{name} , list scores:{list_scores} , average:{average}", int(average)*"*")
    again=input("do you want to enter another person scores?:")
    if again=="yes":
        continue
    else:
        break

#2
def average(students):
    for i in students:
        print(i,'\n')
        value_=students[i]
        average=sum(value_)/len(value_)
        print("average:",average,'\n')
        print("*"*round(average))
    return "end"


students={}


print("fpr break just enter.")

while True:
    try:
        name=input("enter the name:")
        if name=="":
            break
        scores=input("please enter scores with space:")
    except ValueError:
        print("please enter valid information.")
        continue
    else:
        scores=(scores.strip()).split()
        for i in range(len(scores)):
            scores[i]=float(scores[i])
        students[name]=scores
        continue

print(students)
print(average(students))

