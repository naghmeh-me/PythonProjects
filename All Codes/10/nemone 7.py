kind_travel=input("where do you want to go for travel?:")

if kind_travel=="mountaine" or kind_travel=="island":
    boudget=float(input("enter your boudget:"))
    if boudget>2000:
        print("we suggest for you the lokcherry travel.")
    elif 1000<=boudget<=2000:
        print("we suggest for ypu the minrade travel.")
    else:
        print("we suggest for you the economic travel.")
else:
    print("sorry,we don't have plan for this travel .")






