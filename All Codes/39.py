n=int(input("enter how many dentens do you want:"))

odd_number=1

m=0

sum_=0

print("|x|pi|")

print("------")

while m<n:
    m+=1
    pi=4/odd_number
    sum_+=pi
    print(f"|{m}|{sum_}|")
    print("-------")
    odd_number+=2
    continue
