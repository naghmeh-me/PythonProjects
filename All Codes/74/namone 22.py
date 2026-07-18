#1 list
fruits=input("enter name of some fruite:")

list_fruits=(fruits.strip()).split()

if "banana" in list_fruits:
    list_fruits.remove("banana")

if "pitch" not in list_fruits:
    list_fruits.append("pitch")

print("fruits:" , list_fruits)

#2 set
fruits={'banana', 'orange', 'apple', 'bluberry', 'straberry', 'kiwi', 'mango'}

if "banana" in fruits:
    fruits.remove("banana")

if "pitch" not in fruits:
    fruits.add("pitch")

print("fruits:" , fruits)


