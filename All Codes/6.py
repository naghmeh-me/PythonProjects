def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)

while True:
    try:
        range_=int(input("enter the range:"))
        if range_<0:
            print("please enter a positive number:")
            continue
    except:
        print("please enter a positive number:")
        continue
    else:
        for i in range(1,range_+1):
            print(fibo(i))
    break

        
