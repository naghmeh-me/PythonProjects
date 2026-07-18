#1
number=int(input("enter a number:"))

sum_=0

for i in range(1,number+1):
    i=int(i)**3
    sum_+=i

print(sum_)


#2
number=int(input("enter a number:"))

initial=1

sum_=0

while initial<=number:
    x=initial**3
    sum_+=x
    initial+=1
    continue

print(sum_)

#3
sum_=0

print("for exit enter 0.")

while True:
    try:
        number=int(input("enter a number:"))
        if number==0:
            break
    except:
        print("plaese enter valid information.")
        continue
    else:
        for i in range(1,number+1):
            sum_+=i**3
    print("answer:",sum_)
    continue
        
        
