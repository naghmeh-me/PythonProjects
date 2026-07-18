#1
def even_numbers(x,y):
    return [i for i in range(x+1,y) if i%2==0]

x=int(input("enter a number:"))
y=int(input("enter a number:"))

print(even_numbers(x,y))

#2
def even(start,stop):
    l=[]
    for i in range(start+1,stop):
        if i%2==0:
            l.append(i)
        else:
            continue
    return l
start=int(input("enter your forst number:"))
stop=int(input("enter your last number:"))

print(even(start,stop))

#3
def even_number_between_two_number(x,y):
    list_=[]
    if x>y:
        for i in range(x+1,y):
            if i%2==0:
                list_.append(i)
            else:
                continue
        return list_
    else:
        if y<x:
            for i in range(y+1,x):
                if i%2==0:
                    list_.append(i)
                else:
                    continue
            return list_
        else:
            if x==y:
                print("the two numbers are equal,there is no number between them.")
                return "no number"
            

while True:
    try:
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
    except:
        print("enter valid information.")
        continue
    else:
        print(even_number_between_two_number(x,y)) 
        break


    
