while True:
    price_one_night=int(input("قيمت يک اتاق براي هر شب:"))
    count_nights=int(input("تعداد شب هاي اقامت را وارد منيد:"))
    if count_nights==0:
        print("حداقل سک شب بايد انتخاب شئد")
        continue
    count_adults=int(input("تعرار افراد بزرگتر از 18 سال را وارد کنيد:"))
    count_teenagers=int(input("تعداد افراد 3تا 18 سال را ئ=وارد کنيد:"))
    if count_adults==0 and count_teenagers>0:
        print("امکان رزرو برقرار نميباشد")
        break
    count_childs=int(input("تعداد کودکان زير سه يال را وارد کنيد:"))
    if count_adults+count_childs+count_teenagers<1:
        print("رزرو اکمان پذير نميباشد وحداقل يک نفر بايد ثبت شود.")
        break
    if count_adults+count_childs+count_teenagers>7:
        print("رزرو امکان ÷زير نميباشد وظرفيت يک اتاق حداثر 7 نفر است.")
        break
    if count_childs>0:
        count_child_want_service=int(input("جند کودک از خدمات هتل استفاده ميکند؟:"))
        total_price=(((count_adults+count_teenagers)*price_one_night)+count_child_want_service*(price_one_night/2))*count_nights
        print("مبلغ قابل پرداخت:" , total_price)
        break
    else:
        count_childs=0
        total_price=(((count_adults+count_teenagers)*price_one_night))*count_nights
        print("مبلغ قابل پرداخت:" , total_price)
        break







