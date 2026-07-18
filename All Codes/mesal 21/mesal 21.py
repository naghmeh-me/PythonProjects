#1
count=0
sum_=0

while True :
    try:
        number=int(input("enter a number:"))
        count+=1
        sum_+=number
    except:
        print("error!, the number is invalid.")
        continue
    else:
        if number<0:
            count-=1
            sum_-=number
            print("please e nter a positive number.")
            continue
        try:
            again=input("for exit enter exit:")
            if again=="exit":
                print("average:" , sum_/count)
                break
            else:
                continue
        except:
            print("enter exit or no.")


            
    
        
        
