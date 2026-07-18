def binary_search(list_number,number):
    if len(list_number)==0:
        return False
    mid=len(list_number)//2 #mid==4
    if list_number[mid]==number:
        return True
    elif list_number[mid]>number:
        return binary_search(list_number[:mid],number)
    else:
        return binary_search(list_number[mid+1:],number)

numbers=input("enter numbers:")

numbers.strip()

list_number=numbers.split()

number=int(input("enter the number wich do you want to find:"))

for index in range(len(list_number)):
    list_number[index]=int(list_number[index])

print(binary_search(list_number,number))
