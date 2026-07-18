text=input("enter a text:")

text1=input("enter another text:")

list_=(text1.strip()).split()

tuple_and_list=list(zip(text[::-1],list_))

print(tuple_and_list)



