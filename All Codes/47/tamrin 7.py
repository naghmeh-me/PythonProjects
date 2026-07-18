from time import sleep

print("for exit enter 0.")

while True:
    try:
        y=0
        round_=int(input("\nenter how many round:"))
        if round_==0:
            break
        number=int(input("enter hoe may number do you want to count:"))
        second=int(input("enter how many second for delay:"))
    except ValueError:
        print("please enter valid information.")
        continue
    else:
        while y<round_:
            y+=1
            print(f"\nRound {y}")
            for i in range(1,number+1):
                sleep(second)
                print(i , end=" ")
            continue
                
                
                    
                    
