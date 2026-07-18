print("for exit enter 00.")

while True:
    try:
        number=int(input("enter a number:"))
    except:
        print("erroe!entera valid number.")
        continue
    else:
        if number<0:
            print("enter a positive number:")
        else:
            if number==00:
                break
            else:
                reverse_number=str(number)[::-1]
                print("reverse number:" , reverse_number)
