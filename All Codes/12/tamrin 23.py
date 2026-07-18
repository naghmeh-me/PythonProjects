salary=float(input("enter amount of your salalry:"))

married=input("are you married:")

if married=="yes":
    if salary>=50000:
        print("18 درصد بايد ماليات داده شود" , "مبلغي که بايد به دولت داده شود:" , (salary*18)/100)
    else:
        if 30000<=salary<50000:
            print("13 درصد بايد ماليات داده شود" , "مبلغي که بايد به دولت داده شود:" , (salary*13)/100)
        else:
            if 10000<=salary<30000:
                print("8 درصد بايد ماليات داده شود" , "مبلغي که بايد به دولت داده شود:" , (salary*8)/100)
            else:
                print("اذ ماليات معاف است")
else:
    if salary>=50000:
        print("20درصد بايد ماليات داده شود" , "مبلغي که بايد به دولت داده شود:" , (salary*18)/100)
    else:
        if 30000<=salary<50000:
            print("15 درصد بايد ماليات داده شود" , "مبلغي که بايد به دولت داده شود:" , (salary*15)/100)
        else:
            if 10000<=salary<30000:
                print("10 درصد بايد ماليات داده شود" , "مبلغي که بايد به دولت داده شود:" , (salary*10)/100)
            else:
                print("اذ ماليات معاف است")
        
