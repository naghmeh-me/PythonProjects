number=int(input("enter a number:"))

n=int(input("enter number bit:"))

binary=bin(number)

print(f"binary {number}:{binary}\n",(str(binary)[::-1])[n])
    
