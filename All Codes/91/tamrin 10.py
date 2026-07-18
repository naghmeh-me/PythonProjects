#1
search_word=input("enter the word for search:")

file=open('2.py','r')

lines=file.readlines()

for line in lines:
    if search_word in line:
        print(line)

file.close()

#2
import os

while True:
    print("for exit enter 0.")
    word=input("enter the word you want to found:")
    if word=="0":
        break
    else:
        filename=input("enter the fila name:")
        if os.path.exists(filename):
            file=open(filename,'r')
            for i in file:
                if word in i:
                    print(i)
                else:
                    continue
        else:
            print("this file is not exists.")
            continue

#3
import os

print("for exit just press enter button.")

while True:
    try:
        name=input("enter the file name:")
        word=input("enter the word:")
        if name=="":
            break
    except ValueError:
        print("please enter valid information.")
        continue
    else:
        if os.path.exists(name):
            with open(name,'r') as file:
                lines=file.readlines()
                for i in lines:
                    if word in i:
                        print(i)
        else:
            print("the file doesn't exist.")
            continue
                    

