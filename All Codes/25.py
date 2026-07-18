text=input("enter the text:")

list_text=(text.strip()).split()

print(list_text)

for i in list_text:
    if len(i)>len(list_text[(list_text.index(i))+1]):
        max_=i
    else:
        if len(i)<len(list_text[(list_text.index(i))+1]):
            max_=list_text[(list_text.index(i))+1]
        else:
            if len(i)==len(list_text[(list_text.index(i))+1]):
                continue

if max_==False:
    print("all words have equal lenght.")
else:
    print("the longest word in this text is:",max_)
