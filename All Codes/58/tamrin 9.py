#1
def average_scores(scores):
    scores=scores.strip()
    scores=scores.split()
    count_scores=len(scores)
    for index in range(count_scores):
        scores[index]=float(scores[index])
        average=sum(scores)/count_scores
    return average

        
name=input("enter name of the student:")

scores=input("enter grades:")

print(f"average scores of {name} =" , average_scores(scores))

#2
def get_avg(scores):
    scores_list=scores.split()
    for index in range(len(scores_list)):
        scores_list[index]=float(scores_list[index])
    return sum(scores_list)/len(scores_list)

scores=input("enter scores:\n" )#12 12 14 ...

print(f"average={get_avg(scores):2f}")

