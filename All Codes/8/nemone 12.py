#1
number=input("enter a number:")

largest_i=0

for i in number:
    int_i=int(i)
    if int_i>largest_i:
        largest_i=int_i

print("بذدگترين رقم عدد:" , largest_i)
    
#2
while True:
    max_ = 0
    
    number = int(input("Enter a random number:"))
    
    for i in str(number):
        if int(i) > max_:
            max_ = int(i)
        
    print(f"Greater number in this integer is:{max_}")
    
    end = input("Do you want to do this again?(yes/no):")
    if end == "yes":
        continue
    break

#3
max_=0

print("for exit enter 0:")

while True:
    try:
        number=int(input("enter a number:"))
        if number==0:
            break
    except:
        print("please enter a valid number.")
        continue
    else:
        for i in str(number):
            if int(i)>max_:
                max_=int(i)
        print(f"largest integer in {number}:{max_}")
        continue
            
            
        
        
