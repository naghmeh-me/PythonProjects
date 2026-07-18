wight_product=float(input("وزن محصول را وارد کنيد:"))

amount=float(input("قيمت محصول را وارد کنيد:"))

if wight_product<5 and amount>1000000:
    print("محصولات رايگان ارسال ميشود")
else:
    print("مبلغ ارسال باسد پرداخت شود.")
