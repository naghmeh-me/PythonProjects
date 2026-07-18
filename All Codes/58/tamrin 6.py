#1
def print_error():
    return "error"

def do_twice():
    print_error()
    print()
    print_error()

number1=int(input("enter a number:"))
number2=int(input("enter a number:"))

if number1<0 or number2<0:
    print(print_error())
else:
    if number1<0 and number2<0:
        print(do_twice())

#2
def print_error():
    return "error"

def do_twice():
    print_error()
    print()
    print_error()

a=int(input("entee a number:"))
b=int(input("enter a number:"))

while True:
    if a>0 and b>0:
        break
    else:
        if a<0 or b<0:
            print(print_error())
        else:
            if a<0 and b<0:
                print(do_twice())
            
    
