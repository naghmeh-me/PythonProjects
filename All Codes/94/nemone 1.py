#1
import csv

with open('1.py','r') as file:
    read_file=csv.reader(file)
    for row in read_file:
        print(row)

#2
import os
import csv

while True:
    try:
        name=input("enter the file name:")
    except FileNotFoundError:
        print("please enter valid information.")
        continue
    else:
        if os.path.exists(name):
            with open(name,'r') as file:
                read_file=csv.reader(file)
                for row in read_file:
                    print(row)
                break
        else:
            print("this file isn't exist.")

