#1
while True:
    x=int(input("entr a number:"))
    if x<0:
        print("error!enter a positive number")
        continue
    y=int(input("entr a number:"))
    if y<0:
        print("error!enter a positive number")
        continue
    z=int(input("entr a number:"))
    if z<0:
        print("error!enter a positive number")
        continue
    if x==y or x==z or y==z:
        print("error! the numbers can't be equall.")
        continue
    if x>y and x>z:
        print(f"the first number:{x} is the biggest.")
        if y>z:
            print(f"the third number:{z} is the smallest.")
        else:
            if z>y:
                print(f"the second number:{y} is the smallest.")
                break
    else:
        if y>x and y>z:
            print(f"the second number:{y} is the biggest.")
            if x>z:
                print(f"the third number:{z} is the smallest.")
            else:
                if z>x:
                    print(f"the first number:{x} is  the smallest.")
                    break
        else:
            if z>x and z>y:
                print(f"the third number:{z} is the biggest.")
                if x>y:
                    print(f"the second number:{y} is the smallest.")
                else:
                    if y>x:
                        print(f"the first number:{x} is  the smallest.")
                        break



#2
x=int(input("entr a number:"))
y=int(input("entr a number:"))
z=int(input("entr a number:"))

max_=max(x,y,z)
min_=min(x,y,z)
print("smallest number:" , min_ , "biggest number:" , max_)

#3
import math


number1 = int(input("Enter a random number:"))
number2 = int(input("Enter another random number:"))
number3 = int(input("Enter another random number:"))
    
print(f"maximum:{max(number1,number2,number3)}\nminimum:{min((number1,number2,number3))}")
                    
                
    
