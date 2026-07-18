#1
def multiply_digit(number):
    multiply=1
    for i in number:
        if int(i)==0:
            continue
        else:
            multiply*=int(i)
    return multiply

number=input("enter a number:")

print("multiply digit of number is :" , multiply_digit(number))

#2
def multiply_(number):
    multiply_=1
    if number>0:
        for i in str(number):
            if i!=0:
                multiply_*=int(i)
        return multiply_
    else:
        if len(str(number))==2:
            return int(str(number)[1])*-1
        else:
            for i in str(number)[1:len(str(number))]:
                if i!=0:
                    multiply_*=int(i)
            return multiply_*-1
                    
            
        

print("for break enter 0.")

while True:
    try:
        number=int(input("enter a number:"))
        if number==0:
            break
    except:
        print("please enter valid information.")
        continue
    else:
        print(multiply_(number))


