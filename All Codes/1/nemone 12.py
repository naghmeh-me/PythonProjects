#"Suppose the price of one copy of a book is $24.75, and the bookstore buys it at a 41% discount. The shipping cost for one copy is $5, and the shipping cost for each additional copy is 62 cents. What is the total cost of selling 80 copies?"

#1
price=float(input("enter the price of the book:"))

discount=float(input("ente the amount of discount:"))

print("price for posting 5$ , for any add of book +0.62.")

number=int(input("enter number of book:"))

if number==1:
    total_price=number*((price*(100-discount))/100)+5
else:
    total_price=number*((price*(100-discount))/100)+5+(number-1)*0.62

print("total price:" , total_price)

#2
price=float(input("قيمت محصول را وارد کنيد:"))

count=int(input("تعداد محصول را وارد کنيد:"))

discount=int(input("مقدار تخفيف را وارد کنيد:"))

deliver=float(input("عزينه ارسال را وارد کنيد:"))

deliver_plus=float(input("هزينه ارسال اضافي:"))

print("هذينه کل:" , ((price*(100-discount))/100)*count+deliver+(deliver_plus*(count-1)))
