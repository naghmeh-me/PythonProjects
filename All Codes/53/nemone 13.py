#1
def check_number_order(numbers):
    list_numbers=numbers.split()
    if sorted(list_numbers)==list_numbers:
        return "صعودي است"
    elif sorted(list_numbers , reverse=True)==list_numbers:
        return "نزولي است"
    else:
        return "اعداد نامرتب هستند"

print("enter numbers like this-->1 2 3")
numbers=input("enter numbers:")

print(check_number_order(numbers))

#2
def check_number_order(n):
    num_str=str(n)
    if num_str=="".join(sorted(num_str)):
        return "ascending"
    elif num_str=="".join(sorted(num_str,reverse=True)):
        return "descending"
    else:
        return "not sorted"

n=input("enter a number:")

result=check_number_order(n)

print("the order of digit in the number is:" , result)
    
    
        
