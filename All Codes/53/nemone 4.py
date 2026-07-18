#1
def sort(a,b,c):
    '''enter three numbers to sort them:
    sort(124,3,99)
    >>>(3,99,124)
    '''
    max_=max(a,b,c)
    min_=min(a,b,c)
    mid_=(a+b+c)-min_-max_
    return (min_,mid_,max_)

#2
def sort(a,b,c):
    max_=max(a,b,c)
    min_=min(a,b,c)
    mid=(a+b+c)-max_-min_
    return (min_,mid,max_)

try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    c=int(input("enter a number:"))
except:
    print("error!enter valid information.")
else:
    print(sort(a,b,c))
    
