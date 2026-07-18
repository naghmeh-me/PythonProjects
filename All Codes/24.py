while True:
    number=int(input("enter a 5 digit number:"))
    if number<0:
        break
    else:
        if len(str(number))!=5:
            print("please enter a 5 digit number:")
            continue
        else:
            break

for i in str(number)[::-1]:
    print(i , end=" ")
