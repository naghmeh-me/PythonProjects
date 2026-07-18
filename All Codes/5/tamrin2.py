r1 = float(input("Enter the value of the first resistor:"))
r2 = float(input("Enter the value of the second resistor:"))
r3 = float(input("Enter the value of the third resistor:"))

print("R = " , ((r1 * r2 * r3) / (r1 * r2) + (r1 * r3) + (r2 * r3)))
