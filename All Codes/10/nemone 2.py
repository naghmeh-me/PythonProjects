pin_code=input("enter a pin code:")

if len(pin_code)<8:
    print("رمز ضعيف است")
elif 8<=len(pin_code)<12:
    print("رمز متوسط است")
else:
    print("رمز قوي است")
