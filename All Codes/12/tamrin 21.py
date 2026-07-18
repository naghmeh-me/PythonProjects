monthly_internet=float(input("ميزان مصرف اينترنت ماهانه خود را وارد کنيد:"))

call=int(input("ميزام دقايق تماس خود را وارد کنيد:"))

if call>300 and monthly_internrt>20:
    print("بسته نامجدود تملس ئ بسته نامحدود اينترنت")
else:
    if call>300 and monthly_internet<20:
        print("بسته نامحدود تماس و بسته محدود اينترنت")
    else:
        if call<300 and monthly_internet>20:
            print("بستخ محدود تماس و بسته نامحدود اينترنت")
        else:
            if call<300 and monthly_internet<20:
                print("بسته محدود تماس و بسته محدود اينترنت")
