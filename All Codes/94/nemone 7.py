#codesh ghalate

import csv
import os

number=0

total_average=0

filename=input("enter name of the file:")

if os.path.exists(filename):
    with open(filename,'r') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            name=row["Name"]
            number+=1
            scores=int(row["Scores"])
            sum_=sum(scores)
            average=sum_/len(scores)
            total_average+=average
            print(f"{name}\naverage scores{average}")

else:
    print("this file is not exist.")

print(f"average of students work:{total_average}")
