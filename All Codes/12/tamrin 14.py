#1
number=int(input("enter a number:"))

mul=1

for i in range(number,0,-1):
    mul*=int(i)

print("factorial number:" , mul)

#2

number=int(input("enter a number:"))

mul=1

while number>=1:
    mul*=number
    number-=1

print("factorial number:" , mul)

#3
while True:
    multiply_=1
    number = int(input("Enter the number:"))
    
    for i in range(1 , number+1):
        multiply_ *= i
    
    print(f"Factoriel {number} : {multiply_}")
    
    again = input("Do you eant to do this again?(yes/no):")
    if again == "yes":
        continue
    break
