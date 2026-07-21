#"Write a program that takes x and y as input, and uses an anonymous (lambda) function to compute and display x raised to the power of y plus y raised to the power of x."

#1
z=lambda x,y:x**y+y**x

x=int(input("enter a number:"))
y=int(input("enter a number:"))

print(z(x,y))

#2
from math import pow

print("For exit from the program enter 0 for value of x.")

while True:
    try:
        x=int(input("Enter value of x:"))
        
        if x==0:
            break
        
        y=int(input("Enter value of y:"))

    except ValueError:
        print("Error! Please enter CORRECT NUMBERS.")
        continue

    else:
        function_=lambda x,y:pow(x,y)+pow(y,x)
        print(f"Answer: {function_(x,y)}")
