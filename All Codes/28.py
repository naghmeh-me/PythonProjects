def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

sum_=0
n=int(input("enter the n:"))

while n>=1:
    sum_+=1/fact(n)
    n-=1

print("answer:",sum_)


