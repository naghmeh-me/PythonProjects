fruits={'apple':3,'banana':5,'orange':2}
vegtabels={'parsley':7,'broccoli':4,'spinach':2,'basil':10}

greengroceries={**fruits , **vegtabels}

print(greengroceries)

goods_name=input("enter the name of goods:")

if goods_name in greengroceries:
    number=greengroceries[goods_name]
    print(f"number of {goods_name} is {number}.")
else:
    print("not found.")
