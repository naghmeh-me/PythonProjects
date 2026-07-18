#1
text=input("enter some name:")

list_=(text.strip()).split()

name=input("wich name in list are looking for:")

if name in list_:
    print("found")
else:
    print("not found.")

#2
text=input("enter some name:")

list_=(text.strip()).split()

name=input("wich name in list are looking for:")

position=0

for i in list_:
    if i==name:
        print(f"found \n this name is in the {position} position.")
    else:
        position+=1
        
