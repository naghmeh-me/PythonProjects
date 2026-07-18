x=1

sum_=0

while x<=10:
    number=int(input("enter a number:"))
    if number<0:
        print("error! , number must be positive.")
        continue
    else:
        x+=1
        sum_+=number

print("average:" , sum_/10)
        
