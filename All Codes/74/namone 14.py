#1
string=input("enter a text:")

list_string=(string.strip()).split()

charecter=input("wich charecter do you want to count:")

counts=[i.count(charecter) for i in list_string]

print(counts)


#2
text=input("enter a text:")

list_text=(text.strip()).split()

charecter=input("wich charecter do you want to count:")

list_count_charecter=[]

for i in list_text:
    count_charecter_in_i=i.count(i)
    lsit_count_charecter=list_count_charecter.append(count_charecter_in_i)
    continue

print(list_text,f"\n count of {word}:" , list_count_charecter)
    
