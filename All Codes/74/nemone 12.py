#1
numbers=input("enter numbers:")

list_numbers=(numbers.strip()).split()

for index in range(len(list_numbers)):
    list_numbers[index]=int(list_numbers[index])

all_positive=all(number>0 for number in list_numbers)

if all_positive:
    print("all numbers are positive.")
else:
    print("all numbers aren't positive.")

#2
numbers=input("enter numbers:")

list_numbers=(numbers.strip()).split()

for i in range(len(list_numbers)):
    list_numbers[i]=int(list_numbers[i])

positive_numbers=list(map(lambda numbers:numbers>0 , list_numbers))

if False in positive_numbers:
    print("all numbers aren't positive.")
else:
    print("all numbers are positive.")

print(positive_numbers)


#3
list_even_numbers=[]

numbers=input("enter numbers:")

numbers.strip()

list_numbers=numbers.split()

for i in range(len(list_numbers)):
    list_numbers[i]=int(list_numbers[i])

for j in list_numbers:
    if j>0:
        list_even_numbers.append(j)

if len(list_numbers)==len(list_even_numbers):
    print("all numbers positive.")
else:
    print("all numbers aren't positive.")
        
