sum_=0
count_=0

while True:
    try:
        number = int(input("Enter the number:"))
    except:
        print("Please enter valid informaton.")
        continue
    else:
        sum_+=number
        count_+=1
        continue_ = input("Continue?")
        if continue_ == "exite":
            print("Avrerage:" , sum_/count_)
            break
        continue
