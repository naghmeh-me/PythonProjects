number=int(input("enter a number:"))

while True:
    numbers=input(f"enter {number} numbers:")
    list_numbers=(numbers.strip()).split()
    if len(list_numbers)==number:
        list_numbers.append(number)
        for i in range(len(list_numbers)):
            list_numbers[i]=int(list_numbers[i])
        sum_=sum(list_numbers)
        print(f"{sorted(list_numbers)}\nsum:{sum_}\naverage:{sum_/(number+1)}")
        break
    else:
        print(f"please enter {number} numbers.")
        continue



