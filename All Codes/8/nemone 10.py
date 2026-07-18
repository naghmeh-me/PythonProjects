#1
while True:
    x=float(input("طول مستطيل رل وارد کنيد:"))
    y=float(input("عرض مستطيل را وارد کنيد:"))
    if x>y:
        break
    else:
        print("error!طول يايد از عرض بزرگتر باشد")
        continue

print("مساحت:" , x*y , "\n", "محيط:" , (x+y)*2)

#2
while True: 
    lenght = float(input("Enter the length of the rectangle:"))
    width = lemght = float(input("Enter the width of the rectangle."))
    
    if lenght > width :
        area = lenght * width
        perimeter = (lenght + width) * 2
        print(f"The area of ​​the rectangle:{area}\nThe peimeter of the rectangular:{perimeter}.")
        end = input("Do you want to do this again?(yes/no):")
        if end == "yes":
            continue
        else:
            break
    else:
        print("The lenght of the rectangle must be greater than its width.")
        continue
    
        
