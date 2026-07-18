#1
a=int(input("enter value of a:"))

b=int(input("enter value of b:"))

c=int(input("enter value of c:"))

delta=b**2-4*a*c

if delta==0:
    print("delta==0 so there is one root \nx1=x2=:" , -b/(2*a))
elif delta>0:
    print("delta>0 so there is two roots:" ,"\n" , f"x1={-b+(delta**0.5)/(2*a)}\nx2={-b-(delta**0.5)/(2*a)}")
else:
    print("delta<0 so ther is no root.")

#2
print("Quadratic equation ---> teta = b**2 - 4*a*c")

while True:
    a = float(input("Enter THe value of a:"))
    b = float(input("Enter THe value of b:"))
    c = float(input("Enter THe value of c:"))
    
    delta = b**2 - 4*a*c
    if delta<0 :
        print(f"delta = {delta} so delta<0 and There is no root.")
    elif delta>0:
        root1= ((-b) + (delta**(1/2))) / 2*a
        root2= ((-b) - (delta**(1/2))) / 2*a
        print(f"delta = {delta} so delta>0 and There is 2 roots\nroot1 = {root1}\nroot2 = {root2}.")
    else :
        root = (-b) / (2*a)
        print(f"delta = {delta} so delta == 0 and there is one root\nroot = {root}")
    end = input("do you want to do this agsin?:(yes/no)")
    if end == "yes":
        continue
    break
        

    
