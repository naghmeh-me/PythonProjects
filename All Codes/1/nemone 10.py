#"Design a program that takes the three side lengths of a triangle as input and computes its perimeter and area using the formulas below:
p = (a + b + c) / 2
s = √(p(p − a)(p − b)(p − c))"

#1
a=int(input("enter a of triangle:"))

b=int(input("enter b of triangle:"))

c=int(input("enter c of triangle:"))

p=(a+b+c)/2

s=(p*(p-a)*(p-b)*(p-c))**1/2

print("mohit:" , p,"masahat:" , s)

#2
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
perimeter = a + b + c

print("Perimeter =", perimeter)
print("Area =", area)
