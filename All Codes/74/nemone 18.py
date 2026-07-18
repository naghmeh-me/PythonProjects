#1
numbers=input("enter numbers:")

number=input("wich number are you looking for:")

list_numbers=(numbers.strip()).split()

if number in list_numbers:
    print("the position of this number is:" , list_numbers.index(number))
else:
    print("not found.")

#2
numbers=[5.2.7.1.9]

given_number=9

found_index=numbers.index(given_number) if given_number in numbers else "not found."

print(found_index)

#3
numbers=input("enter numbers:")

numbers=(numbers.strip()).split()

for i in range(len(numbers)):
    numbers[i]=int(numbers[i])

search=int(input("enter the number wich you want to find:"))

if search in numbers:
    print("the position of this number is:" , numbers.index(search))
else:
    print("not found.")

    
