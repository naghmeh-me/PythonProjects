number=int(input("enter the number:"))

bin_number=list(str(bin(number)))[2::]

for i in bin_number:
    index_=bin_number.index(i)
    if i=="1":
        bin_number[index_]="0"
    else:
        bin_number[index_]="1"

bin_number[0]='0'
bin_number[1]='b'
bin_number=" ".join(bin_number)

print(f"binary {number}:{bin(number)}\nafter change:{bin_number}")






