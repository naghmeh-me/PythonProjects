#"The volume of a sphere with radius r is given by the formula (4/3)πr³. What is the volume of a sphere with radius 6?"
#1
import math

r=float(input("enter r:"))

v=3/4*(math.pi)*r**3

print("v=" , v)

#2
pi = 3.14
r = int(input("pleasr enter Radius:"))
Volume = 3/4 * pi * ( r ** 3)
print("The volume of the circle is" , Volume)

#3
import math

while True:
    r = float(input("Please enter the radiuse of the circle:"))
    print(f"Volume of the circle = {(3/4) * (math.pi) * (r**3)}")
    again = input("Do you want to do this again?(y/n):")
    if again == "n":
        print("It was fun, let's do this againe soon!")
        break
