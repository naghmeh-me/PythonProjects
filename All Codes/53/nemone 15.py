fibonachi=lambda n:n if n==1 or n==0 else fibonachi(n-1)+fibonachi(n-2)

n=int(input("enter a number:"))

print(f"fibonacho {n}'om=" , fibonachi(n))
