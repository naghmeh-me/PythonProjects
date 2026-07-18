#1
even_odd=lambda number:"even" if number%2==0 else "odd"

number=int(input("enter a number:"))

print("the number is :" , even_odd(number))

#2
is_even=lambda n:n%2==0

number=int(input("enter a number:"))

print("it's even" if is_even(number) else "it's odd")
