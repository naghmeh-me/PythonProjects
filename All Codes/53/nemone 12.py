#1
def bakhshpazir(n,x):
    y=0
    for i in range(1,x+1):
        if n%i==0:
            print("yes")
        else:
            return "no"

while True:
    try:
        n=int(input("enter a number:"))
        x=int(input("enter a number:"))
    except:
        print("error!please enter a positive number.")
        continue
    else:
        print(bakhshpazir(n,x))
        break

#2
def check_divisibility(x,n):
    for i in range(1,x+1):
        if n%i!=0:
            print("no")
            return
        print("yes")

n=int(input("enter a number:"))
x=int(input("enter a number:"))

chech_divisibility(x,n)

            
            
