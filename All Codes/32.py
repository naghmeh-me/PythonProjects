sum_=0

while True:
    try:
        n=int(input("enter n :"))
        if n<0:
            print("please enter a positive number:")
            continue
    except:
        print("please enter a valid information.")
        continue
    else:
        for i in range(1,n+1):
            sum_+=i
        break

for j in range(1,n):
    print(f"{j}",end="+")


print(f"{n}={sum_}")
