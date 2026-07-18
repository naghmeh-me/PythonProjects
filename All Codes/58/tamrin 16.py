#1
def even(number):
    if number%2==0:
        for i in range(number,0,-2):
            print(i)
    else:
        for i in range(number-1,0,-2):
            print(i)

number=int(input("enter a number:"))

print(even(number))

#2
def n(number):
    list_=[]
    for i in range(number,0,-1):
        if i%2==0:
            list_.append(i)
    return list_

print("for exit enter 0.")

while True:
    try:
        number=int(input("number:"))
        if number==0:
            break
    except:
        print("please enter a valid number:")
        continue
    else:
        if number<0:
            print("please enter a positive number:")
            continue
        else:
            print(n(number))
            

