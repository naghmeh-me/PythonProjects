#1
number=int(input("enter a number:"))

mul=1

for i in range(number,0,-1):
    print(i)
    mul*=i

print("ضرب اعداد:" , mul)

#2
n=int(input("enter a number:"))

mul=1

while n!=0:
    print(n)
    mul*=n
    n-=1
    continue

print("ضرب اعداد:" , mul)

#3
print("For exite enter 0(zero).")

while True:
    list_=[]
    count_=1
    n = int(input("Please enter a number:"))
    if n == 0:
        break
    for i in range(n , 0 , -1):
        list_.append(i)
        count_*=i
    print(f"{list_} , count = {count_}")

#4
multiply=1

print("for exit enter 0.")

while True:
    try:
        n=int(input("enter a number:"))
        if n==0:
            break
    except:
        print("please e nter a valid number.")
        continue
    else:
        for i in range(n,0,-1):
            multiply*=i
            print(i)
    print("multiply:",multiply)
    continue
