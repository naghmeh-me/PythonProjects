list_=[]

def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print("for exit enter.")
while True:
    try:
        n=int(input("enter a number:"))
        if n==" ":
            break
    except:
        print("please enter a valid information.")
        continue
    else:
        if n<0:
            print("please enter a positive number(negetive numbers aren't fibonachi numbers.")
            continue
        else:
            for i in range(1,n+1):
                fib_i=fibo(i)
                list_.append(fib_i)
        if n in list_:
            print(f"{n} is a fibonachi number.")
            continue
        else:
            print(f"{n} isn't a fibonachi number.")
            continue
