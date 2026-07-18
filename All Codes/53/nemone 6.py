#1
from math import pow

def_=lambda x,y:pow(x,y)+pow(y,x)

while True:
    try:
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
    except:
        print("erroe! enter valid information.")
        continue
    else:
        print(def_(x,y))
        break

#2
z=lambda x,y:x**y+y**x

x=int(input("enter a number:"))
y=int(input("enter a number:"))

print(z(x,y))


