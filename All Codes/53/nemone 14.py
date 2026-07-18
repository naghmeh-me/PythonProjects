#1
print("for exit just enter.")

while True:
    number=input("enter a number:")
    if number=="":
            break
    else:
        if len(number)==1:
            print(number)
            continue
        else:
            if int(number)>0:
                new_number=number[-1]+number[1:-1]+number[0]
                print(new_number)
                continue
            else:
                new_number=number[0]+number[-1]+number[2:-1]+number[1]
                print(new_number)
                continue

#2
def swap_first_last_digit(number):
    list_number=number.strip()
    if len(list_number)==1:
        return number
    new_list_number=number[-1]+list_number[1:-1]+number[0]
    new_number=" ".join(new_list_number)
    return new_number

number=input("enter a number:")

print(swap_first_last_digit(number))

#3
def swap_first_last_digit(num):
    num_str=str(num)
    if len(num_str)>1:
        new_num_str=num_str[-1]+num_str[1:-1]+num_str[0]
        new_num=int(new_num_str)
        return mew_num
    return num

num=int(input("enter a text of numbers:"))

new_num=swap_first_last_digit(num)

print("number with swap first and last digit:" , new_num)


        


        
    
    
    
