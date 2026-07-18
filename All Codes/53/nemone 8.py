#1
def star(number):
    return ("* ")*number

while True:
    try:
        number=int(input("enter how many stars do you want?:"))
    except:
        print("error!enter valid information")
        continue
    else:
        print(star(number))
        break

#2
n=int(input("enter how many stars do you wanr:"))
x=n+1

def star(n):
    return
for i in range(1,x):
    print("*" , end=" ")

star(n)

#3
def star(n):
    print(n*"*")

    


