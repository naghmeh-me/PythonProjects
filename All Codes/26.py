text=input("enter atext:")

count_=0

for i in text:
    if i=="o" or i=='e' or i=='u' or i=='i' or i=='a':
        count_+=1
    else:
        if i=="O" or i=="E" or i=="U" or i=="I" or i=="A":
            count_+=1
        else:
            if i==" ":
                continue
            else:
                continue

print(count_)
        
