#1
def fibonachi(number):
    if number==0 or number==1:
        return 1
    return fibonachi(number-1)+fibonachi(number-2)

while True:
    try:
        number=int(input("enter a number:"))
    except:
        print("erroe!enter a valid number.")
        continue
    else:
        for i in range(number+1):
            print(fibonachi(i) , end=" ")
        break

#2
def fibo(n):
    if n==0 or n==1:
        return 1
    return fib0(n-1)+fibo(n+2)

n=int(input("enter anumber;"))

for i in range(n+1):
    print(fibo(i) , end=" ")


