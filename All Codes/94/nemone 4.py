import csv

with open('2.py','r') as file:
    csv_reader=csv.DictReader(file)
    total_quantity={}
    for row in csv_reader:
        product=row['Name Product']
        quantity_sold=int(row["Number Of Sold Product"])
        if product in total_quantity:
            total_quantity[product]+=quantity_sold
        else:
            total_quantity[product]=quantity_sold

for product ,quantity in total_quantity.items():
    print(f"{product}:{quantity}")
        
