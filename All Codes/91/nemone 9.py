#1
count=0

namefile=input("enter the file name:")

file=open(namefile,'r')

lines=file.readlines()

for line in lines:
    if lines=='\n':
        continue
    count+=1

print(count)

#2
import os

count=0

filename=input("ente the file name:")

if os.path.exists(filename):
    file=open(filename,'r')
    for i in file:
        if i!='\n':
            count+=1
        else:
            continue
else:
    print("this file dosn;t exist.")

print("count of lines in this file :" , count)

#3
import os

print("for exit just enter:")

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
            with open(name,'r') as file:
                lines=file.readlines()
                print("count lines:" , len(lines))
        else:
            print("file didn't found.")
            continue
                



    



