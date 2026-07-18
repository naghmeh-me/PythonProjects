#dorost kar nemikone
import csv
import os

filename=input("enter the file name:")

if os.path.exists(filename):
    with open(filename,'r') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            food=row["Name"]
            comments=row["Comment"]
            if 'food' or 'service' in row["Comment"]:
                print(f"comment for {food}:{comments}")

else:
    print("this file isn't exist.")
