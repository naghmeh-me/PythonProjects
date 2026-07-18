#1
degree=int(input("مقدار دماي هوا را وارد کنيد:"))

if degree<=1:
    print("يخبندان")
elif 1<degree<=9:
    print("سرماي شديد")
elif 9<degree<=16:
    print("هواي سرد")
elif 16<degree<=23:
    print("هواي مطلوب")
elif 23<degree<=30:
    print("هواي گرم")
else:
    print("گرماي شديد")

#2
degree=int(input("مقدار دماي هوا را وارد کنيد:"))

if degree<=1:
    print("يخبندان")
else:
    if 1<degree<=9:
        print("سرماي شديد")
    else:
        if 9<degree<=16:
            print("هواي سرد")
        else:
            if 16<degree<=23:
                print("هواي مطلوب")
            else:
                if 23<degree<=30:
                    print("هواي گرم")
                else:
                    if degree>30:
                        print("گرماي شديد")
