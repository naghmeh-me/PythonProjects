hight=int(input("قر خود را وارد منيد:"))

hight/=100

wieght=int(input("وزن خود را وارد کنيد"))

BMI=wieght/(hight**2)

print("BMI:" , BMI)

if 18.5<=BMI<25:
    print("فرد داراي وزن متعادل است")
elif BMI>30:
    print("فرد داراي اضافه وزن است")
else:
    print("فرد لاغر است")
    
    
