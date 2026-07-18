number=int(input("enter the number:"))
n=int(input("enter the position of the bit you want to change:"))

bin_number=str(bin(number))
n_bin=bin_number[n+1]
print(n_bin)

if n_bin=='0':
    bin_number=bin_number.replace(n_bin,'1')
else:
    if n_bin=='1':
        bin_number=bin_number.replace(n_bin,'0')

print(f"binary {number}:{bin(number)}\nafter change:{bin_number}\nwich is equal with number {eval(bin_number)}")
