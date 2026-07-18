def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

sum_=0

n=int(input("enter the n:"))

for i in range(1,n+1):
    number=1/fact(i)
    sum_+=number

print(f"answer:{sum_}")
    
