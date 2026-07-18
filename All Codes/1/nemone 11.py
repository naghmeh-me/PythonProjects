#1
number=int(input("enter a two digit number:"))

first_digit_number=number//10

second_digit_number=number%10

print(f"reverse number:{second_digit_number}{first_digit_number}")

#2
number=int(input("سک عدد دورقمي وارد کنيد:"))

print("مقلوب عدد وارد شده:" , f"{number%10}{number//10}")

#3
while True:
    number=int(input("Enter a 2 digit number:"))
    if len(str(number)) != 2:
        print("Invalid number")
        continue
    break
second_digit = number%10
first_digit = number//10

print(str(second_digit) + str(first_digit))





