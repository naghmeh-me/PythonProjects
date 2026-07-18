#1
odd_numbers=lambda x,y:[i for i in range(x+1,y) if i%2!=0]

odd_numbers_=lambda x,y:[i for i in range(y+1,x) if i%2!=0]

x=int(input("enter a number:"))
y=int(input("enter a number:"))

if x<y:
    print(odd_numbers(x,y))
else:
    print(odd_numbers_(x,y))

#2
    def odd_numbers(number1,number2):
    list_=[]
    if number1>number2:
        for i in range(number2,number1):
            if i%2!=0:
                list_.append(i)
        return list_
    else:
        if number2>number1:
            for i in range(number1,number2):
                if i%2!=0:
                    list_.append(i)
            return list_
            

print("enter 0 for break.")

while True:
    try:
        number1=int(input("enter a number:"))
        if number1==0:
            break
        number2=int(input("enter another number:"))
    except ValueError:
        print("please enter valid information.")
        continue
    else:
        if number1==number2:
            print("please enter two number wich aren't equall.")
            continue
        print(odd_numbers(number1,number2))

