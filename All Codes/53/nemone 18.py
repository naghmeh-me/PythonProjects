#1
from math import pow

math=lambda x,y:pow(x,0.5)/y

x=float(input("enter a number for x:"))

y=float(input("enter a number for y:"))

print("result:" , math(x,y))

#2
import math

calculate=lambda x,y:math.sqrt(x)/y

x=float(input("enter a number for x:"))

y=float(input("enter a number for y:"))

print("result:" , calculate(x,y))


