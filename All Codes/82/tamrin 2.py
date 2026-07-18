#1
def sort_numbers(x):
    sort=sorted(x,reverse=True)
    return sort

numbers=input("enter some numbers:")
numbers=(numbers.strip()).split()

for i in range(len(numbers)):
    numbers[i]=int(numbers[i])

print(sort_numbers(numbers))


#2
import math

def list_max_min(numbers):
    return[max(numbers),min(numbers)]

numbers=input("enter some numbers:")
numbers=numbers.split()

for i in range(len(numbers)):
    numbers[i]=int(numbers[i])

print(list_max_min(numbers))

#3
def max_min_list(list_numbers):
    list_numbers.sort()
    print(list_numbers)
    list_sorted=[]
    list_sorted.append(list_numbers[-1])
    list_sorted.append(list_numbers[0])
    return list_sorted
    

numbers=input("enter some numbers:")




