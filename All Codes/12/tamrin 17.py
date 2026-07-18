total_price=float(input("مبلغ کل خريد را وارد کنيد:"))

if 5000000<=total_price<=15000000:
    discount_price=(95*total_price)/100
    print("مبلغ قابل پرداخت:" , discount_price)
else:
    if total_price>15000000:
        discount_price=(90*total_price)/100
        print("مبلغ قابل پرداخت:" , discount_price)
    else:
        if total_price<5000000:
            print("discount=0" , "\nمبلغ قابل پرداخت:" , total_price)

        
