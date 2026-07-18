text=input("enter a string:")

dict_={}

count_u=0
count_l=0

for i in text:
    if i==" ":
        continue
    else:
        if i.isupper():
            count_u+=1
        else:
            count_l+=1

dict_["uppercase"]=count_u
dict_["lowercass"]=count_l

print(dict_)
    
