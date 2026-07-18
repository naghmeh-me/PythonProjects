from math import floor

numbers=input("enter some numbers:")

list_numbers=(numbers.strip()).split()

mid_=floor(len(list_numbers)/2)

count_0=0

list_=[]

for i in range(len(list_numbers)):
    list_numbers[i]=int(list_numbers[i])

while True:
    if list_numbers[mid_]==0:
        count_0+=1
        mid_=mid_+1
        if list_numbers[mid_]==0:
            count_0+=1
            mid_=mid_-2
            continue
        else:
            x=list_numbers[floor(mid_)]
            break
    else:
        x=list_numbers[floor(mid_)]
        break

if count_0==len(list_numbers):
    print("all the numbers are zero.")
else:
    for i in list_numbers:
        y=i/x
        list_.append(y)

print(list_)    
