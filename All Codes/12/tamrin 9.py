#1
number=int(input("enter a positive number:"))

smallest=9

for i in str(number):
    if int(i)<smallest:
        smallest=int(i)
    else:
        continue

print("smallest digit in number:" ,smallest)

#2
min_=9

print("for break enter 0.")

while True:
    try:
        number=int(input("enter a number:"))
        if number==0:
            break
    except:
        print("please e nter  avalid number.")
        continue
    else:
        for i in str(number):
            if int(i)<min_:
                min_=int(i)
    print(f"the smallest number of {number}={min_}")
    continue

#3
print("For exite enter 0(zero).")

while True:
    list_=[]
    number = int(input("Please enter a number:"))
    if number == 0:
        break
    for i in str(number):
        list_.append(int(i))
    print(f"The smallest integer in {number} = {min(list_)}")

    
        
    
    
    
