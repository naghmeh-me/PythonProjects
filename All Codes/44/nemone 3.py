#1
sum_=0

for i in range(1000,10000):
    if str(i).count("0")>0:
        continue
    else:
        if i%5==0:
            sum_+=i

print(sum_)

#2     
sum_=0

for i in range (1000,10000,5):
    if str(i).count("0")>0:
        continue
    else:
        sum_+=i

print(sum_)
