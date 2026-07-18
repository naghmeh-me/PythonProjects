#1
count=0

sum_=0

print("for exit enter 0.")

while True:
    number=float(input("enter a positive number:"))
    if number<0:
        print("error!please enter a positive number.")
        continue
    elif number==0:
        break
    else:
        count+=1
        sum_+=number
        continue

print("average:" , sum_/count)

#2
numbers=input("Please enter 5 number (like this: 1 2 3 4 5):")

list_numbers=(numbers.strip()).split()

len_numbers=len(list_numbers)

sum_=0

for i in list_numbers:
    sum_+= int(i)

print("Average of numbers:" , sum_/len_numbers)

    
    
