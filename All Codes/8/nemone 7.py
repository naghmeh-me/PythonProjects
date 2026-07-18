#1
while True:
    number=int(input("عدد موردنظر را وارد کنيد:"))
    if number<0:
        print("erroe!لطفا يک عدد طبيعي وارد کنيد")
    else:
        break
    
initial=1

while initial<=number:
    if initial%5!=0:
        print(initial)
    initial+=1

#2
while True:
    x=int(input("enter a positive number:"))
    if x<0:
        print("error!")
        continue
    else:
        for i in range(1,x+1):
            if i%5==0:
                continue
            print(i)
    break
    

#3
num=1

while True:
    number=int(input("عدد موردنظر را وارد کنيد:"))
    if number<0:
        print("erroe!لطفا يک عدد طبيعي وارد کنيد")
    else:
        break

while num<=number:
    if num%5!=0:
        print(num)
        num+=1
        continue
    else:
        num+=1
        continue


#4
while True:
    number = int(input("Enter an integer:"))
    
    if number<0:
        print("Error!")
        continue
    else:
        for i in range(1 , number+1):
            if i % 5 == 0:
                continue
            print(i)
        end = input("Do you want to do this again?(yes/no):")
        if end == "yes":
            continue
        print("It's was fun, let's do it again enother time:)")
        break
