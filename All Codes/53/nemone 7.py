#1
from math import pow

def_=lambda x,y:3*pow(x,2)*pow(y,2)-2*x*pow(y,2)-2*x+6

while True:
    try:
        x=int(input("enter a number for x:"))
        y=int(input("enter anumber for y:"))
    except:
        print("error!enter valid information.")
        continue
    else:
        print(def_(x,y))
        break

#2
def_=lambda x,y:3*x**2*y**2-2*x*y**)-2*x+6

x=int(input("enter a number for x:"))
y=int(input("enter anumber for y:"))

print(def_(x,y))
