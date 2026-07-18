import os

filename=input("enter the file name:")

if os.path.exists(filename):
    file=open(filename,'r')
    content=file.read()
    count=len(content)//8
    print("number of bytes this file :" , count)
    file.close()
else:
    print("this file dors not exist.")
