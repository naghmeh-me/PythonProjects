birth=int(input("enter your birth year:"))
year=int(input("enter the current year:"))

age=year-birth

years=age
months=12*age
days=364*age
houres=days*24
minutes=houres*60
seconds=minutes*60

print(f"{years}:{months}:{days}:{houres}:{minutes}:{seconds}")
