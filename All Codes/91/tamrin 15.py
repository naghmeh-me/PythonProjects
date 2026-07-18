#1
import os

filename=input("enter the file name:")

if os.path.exists(filename):
    file_size=os.path.getsize(filename)
    print("file size:" , file_size,'bytes')
else:
    print("this file is not exist.")

#2
import os

print("gust press return button to exit:")

while True:
    try:
        name=input("enter the file name:")
        if name=="":
            break
    except FileNotFoundError:
        print("please enter valid information.")
        continue
    else:
        if os.path.exists(name):
            file_size=os.path.getsize(name)
            print("file isze(bit):",file_size)
        else:
            print("file is not exist.")
            continue

