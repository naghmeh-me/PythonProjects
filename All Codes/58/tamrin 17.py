factoriel=lambda number:1 if number==0 or number==1 else number*factoriel(number-1)

number=int(input("enter anumber to give you the factoriel:"))

print(f"factoriel {number} =" , factoriel(number))
