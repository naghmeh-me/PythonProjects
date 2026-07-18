import os
from time import sleep

count_=0

name=input("enter the file name:")

if os.path.exists(name):
    with open(name,'r') as file:
        text=file.readlines()
        for line in text:
            count+=1
            if count_%22==0:
                print(text)
                sleep(1)
                continue
            else:
                continue
else:
    print("this file is not exist.")
            
