import csv
import os

filename=input("enter the file name:")

if os.path.exists(filename):
    with open(filename,'r') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            number_book=int(row['Amount'])
            book_name=row["Name"]
            if number_book<5:
                print(f"warning!number of the {book_name} book is less than 5.")
            else:
                continue
else:
    print("this file dosn't exists.")

            
    
