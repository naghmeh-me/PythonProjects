number=int(input("enter a number:"))#55

n=int(input("wich number you want to chane to one :"))#4

bin_number=str(bin(number))#0b110111

number_n=bin_number[n+1]#0

bin_number=bin_number.replace(number_n,'1')

print(f"binary {number} is {bin(number)}\nafter replace:{bin_number}")
    
    
