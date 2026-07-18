def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

list_=[]

for i in range(100,1000):#123
    n=i-((i//100)*100)#23
    yekan=n-((n//10)*10)#2
    dahgan=n//10
    sadgan=i//100
    sum_fact=fact(yekan)+fact(dahgan)+fact(sadgan)
    if i==sum_fact:
        print(i)


