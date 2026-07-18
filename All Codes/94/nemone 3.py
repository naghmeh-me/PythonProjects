#1
import csv

#data to write to the csv file
data=[
    ["Name","Age","City","Work"],
    ['Ali',26,'Manager','Tehran'],
    ['Alice',17,'London','Receptionist'],
    ['Bob',20,'Paris','Seller'],
    ['Bill',23,'Shiraz','Accountant'],
    ['Helena',25,'Tehran','Seller'],
    ['Alex',26,'Manager','New York'],
    ['Naghmeh',21,'Computer Programer','Tehran'],
    ]

with open('1.py','w') as file:
    #creat a csv writer object
    csv_writer=csv.writer(file)
    #write the data to the csv file
    csv_writer.writerows(data)

print("data written to output.csv succesfuly.")

#2
import os
import csv

while True:
    try:
        name=input("enter the file name:")
    except FileNotFoundError:
        print("please enter valid information:")
        continue
    else:
        if os.path.exists(name):
            with open(name,'w') as file:
                data=[
                    ["Name","AGE","City","Work"],
                    ['Ali',26,"Tehran","MAnager"],
                    ['Alice',17,'London','Receptionist'],
                    ['Bob',20,'Paris','Seller'],
                    ['Bill',23,'Shiraz','Accountant'],
                    ['Helena',25,'Tehran','Seller'],
                    ['Alex',26,'Manager','New York'],
                    ['Naghmeh',21,'Computer Programer','Tehran'],
                    ]
                csv_writer=csv.writer(file)
                csv_writer.writerows(data)
                print("date imported successfully!")
                break
        else:
            print("the file is not exist.")
            continue
                

