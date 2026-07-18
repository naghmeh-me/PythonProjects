#1
number=input("enter a number:")

reverse_number=number[::-1]

print("reverse number:" , reverse_number)

#2
print("for exit enter 0:")

while True:
    try:
        number=int(input("enter a number:"))
        if number==0:
            break
    except:
        print("enter valid information.")
        continue
    else:
        reverse_number=str(number)[::-1]
        print("reverse number:",reverse_number)
        continue
        

