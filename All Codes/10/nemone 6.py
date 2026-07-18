grade=float(input("نمره را وارد کنيد"))

if 80<=grade<100:
    print("A" , "\n" , "پاس شده است")
else:
    if 60<=grade<80:
        print("B" ,"\n" ,"پاس شده است")
    else:
        if 40<=grade<60:
            print("C" ,"\n" ,"پاس شده است")
        else:
            if 20<=grade<40:
                print("D" ,"\n" ,"پاس شده است")
            else:
                if grade<20:
                    print("F" ,"\n" ,"درس را افتاده است")
                else:
                    print("errpr!" , "\n" ,"نمره اشتباه وارد شده است")
