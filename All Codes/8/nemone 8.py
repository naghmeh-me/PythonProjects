#1
numbers=input("Please enter 5 number (like this: 1 2 3 4 5):")

list_numbers=(numbers.strip()).split()

sum_=0

for i in list_numbers:
    sum_+= int(i)

print("Average of numbers:" , sum_/5)

#2
initial=1

sum_=0

while initial<6:
    number=int(input("enter a positive number:"))
    if number<0:
        print("error!")
        continue
    else:
        initial+=1
        sum_+=number
        continue

print("ميانگين:" , sum_/5)

#3
while True:
    while True:
        n1 = int(input("Enter first integer:"))
        if n1<0:
            print("Error!")
            continue
        break
    
    while True:
        n2 = int(input("Enter second integer:"))
        if n2<0:
            print("Error!")
            continue
        break
    
    while True:
        n3 = int(input("Enter third integer:"))
        if n3<0:
            print("Error!")
            continue
        break
    
    while True:
        n4 = int(input("Enter fourth integer:"))
        if n4<0:
            print("Error!")
            continue
        break
    
    while True:
        n5 = int(input("Enter fifth integer:"))
        if n5<0:
            print("Error!")
            continue
        break
    
    sum_ = n1 + n2 + n3 + n4 + n5
    average_ = sum_/5
    
    print(f"Average of numbers: {average_}")
    enter = input("Do you want to do this again?(yes/no):")
    if enter == "yes":
        continue
    print("It's was fun, let's do it again soon.")
    break
