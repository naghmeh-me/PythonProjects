#1
import csv

with open('1.py','r') as file:
    read_file=csv.DictReader(file)
    for row in read_file:
        print(row['Name'],row['Age'],row['Work'],row['City'])

#2
import os
import csv

while True:
    try:
        name=input("enter name of the file:")
    except FileNotFoundError:
        print("please enter valid information.")
        continue
    else:
        if os.path.exists(name):
            with open(name,'r') as file:
                read_file=csv.DictReader(file)
                for row in read_file:
                    print(row['Name'],row['Age'],row['Work'],row['City'])
                break
        else:
            print("sorry this file isn't exist.")

