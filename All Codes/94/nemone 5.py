import csv

with open('1.py','r') as file:
    dict_={}
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        name=row["Name"]
        job=row["Work"]
        if "Seller" in row["Work"]:
            dict_[name]=job
        

for name,job in dict_.items():
    print(f"{name}:{job}")

