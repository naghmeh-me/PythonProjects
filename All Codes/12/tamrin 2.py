page=int(input("تعداد صفحات کتاب را وارد کنيد:"))

felash=float(input("گنجايش فلش را به گيگابايت وارد کنيد:"))

bit_page=33*76

bit_book=page*bit_page

bit_felash=felash*(10**9)

print("تعداد کتابهايي که در فلش ميتواند قرار بگيرد:" , bit_felash/bit_book)
