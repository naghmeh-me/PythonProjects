#1
sum_=0

print("for break enter a number less than zero.")

while True:
    number=int(input("enter a number:"))
    if number<0:
        break
    else:
        if number!=0:
            sum_+=number
            continue
        else:
            print(sum_)
            sum_=0
            continue

#2
sum_=0

print("for break enter a number less than zero.")

while True:
    number=int(input("enter a number:"))
    if number<0:
        break
    else:
        if number!=0:
            sum_+=number
            continue
        else:
            print(sum_)
            continue
    
