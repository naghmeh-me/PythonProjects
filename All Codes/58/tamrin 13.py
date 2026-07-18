#1
from math import pow

def vatar(a,b):
    c=pow(pow(a,2)+pow(b,2),0.5)
    return c
    
a=float(input("enter a of triangle:"))

b=float(input("enter b of triangle:"))

print("c of triangle:" , vatar(a,b))

#2
import math

def fisaghores(a,b):
    '''enter a,b of triangle and recive your answer:
    fisaghores(3,4):
    >>>c=5
    '''
    c=a**2 + b**2
    vatar=math.floor(math.sqrt(c))
    return vatar

a=int(input("enter a from triangle:"))

b=int(input("enter b from triangle:"))

print("vatar of triangel or c:" , fisaghores(a,b))
    
