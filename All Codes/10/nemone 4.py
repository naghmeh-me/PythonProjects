price_one_night=int(input("قيمت يک اتاق براي هر شب:"))

count_adults=int(input("تعرار افراد بزرگتر از 18 سال را وارد کنيد:"))

count_teenagers=int(input("تعداد افراد 3تا 18 سال را ئ=وارد کنيد:"))

count_childs=int(input("تعداد کودکان زير سه يال را وارد کنيد:"))

count_child_want_service=input("جند کودک از خدمات هتل استفاده ميکند؟:")

count_nights=int(input("تعداد شب هاي اقامت را وارد منيد:"))

if count_adults==0 and count_teenagers>0:
    print("امکان رزرو برقرار نميباشد")

total_price=(((count_adults+count_teenagers)*price_one_night)+count_child_want_service*(price_one_night/2))*count_nights
print("مبلغ قابل پرداخت:" , total_price)




