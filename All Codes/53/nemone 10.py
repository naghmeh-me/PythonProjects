#1
def factoriel(number):
    if number==1:
        return 1
    else:
        return number*factoriel(number-1)

while True:
    try:
        number=int(input("enter a number:"))
    except:
        print("error!please enter a valid number.")
        continue
    else:
        print(f"factiriel {number}:" , factoriel(number))
        break

#2
def fact(n):
    if n==1:
        return n
    return n*fact(n-1) #fact(5)->5*fact(4)->5*4*fact(3)->5*4*3*fact(2)->60*2*fact(1)

