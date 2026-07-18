#1
scores=input("enter scores:")

scores=scores.strip()

list_scores=scores.split()

for i in range(len(list_scores)):
    list_scores[i]=float(list_scores[i])

sum_=sum(list_scores)

average=sum_/len(list_scores)

print("list scores :" , list_scores , "average of scores :" , average)

#2
def average_scores(scores):
    scores=(scores.strip()).split()
    print(sorted(scores))
    for i in range(len(scores)):
        scores[i]=float(scores[i])
    return sum(scores)/len(scores)

print("for exit just enter.")

while True:
    try:
        scores=input("please enter scores with space:")
        if scores=="":
            break
    except:
        print("please enter valid information.")
        continue
    else:
        print("average:",average_scores(scores))
        

