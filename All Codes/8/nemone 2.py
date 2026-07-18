#1
a=float(input("enter a from triangle:"))

b=float(input("enter b from triangle:"))

c=float(input("enter c from triang;le:"))

if a+b>c and a+c>b and c+b>a:
    print("yes! it's a triagle.")
else:
    print("no , it's not a triangle.")
    

#2
a=float(input("enter a from triangle:"))

b=float(input("enter b from triangle:"))

c=float(input("enter c from triang;le:"))

if a+b>c:
    print("a+b>c")
    if a+c>b:
        print("a+c>b")
        if b+c>a:
            print("b+c>a")
            print("yes! it'sa triangle.")
        else:
            print("b+c<a")
            print("no it's not a triangle.")
    else:
        print("a+c<b")
        print("no it's not a triangle.")
else:
    print("a+b<c")
    print("no it's not a triangle.")


#3
while True:
    a = float(input("Enter the value of a triangle:"))
    b = float(input("Enter the value of b triangle:"))
    c = float(input("Enter the value of c triangle:"))
    
    if a+b>c:
        print("a+b>c")
        if a+c>b:
            print("a+c>b")
            if b+c>a:
                print("b+c>a\nit's a triangle.")
            else:
                print("b+c<a\nit's not a triangel.")
        else:
            print("a+c>b\nit's no a triangle.")
    else:
        print("a+b<c\nit's not a triangle.")
    
    end = input("Do you want to do this again?(yes/no):")
    if end == "yes":
        continue
    break
