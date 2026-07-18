def fibonachi(x):
    if x==1 or x==2:
        return 1
    else:
        return fibonachi(x-1)+fibonachi(x-2)

list_fibonachi=[]

while True:
    try:
        x=int(input("enter a number:"))
        if x<0:
            print("numbers less than zero aren't fibonachi numbers:")
            continue
    except:
        print("please enter valid information.")
    else:
        for i in range(1,x):
            list_fibonachi.append(fibonachi(i))
        break

if x in list_fibonachi:
    print(f"{x} is a fibonachi number.")
else:
    print(f"{x} isn't a fibonachi number.")


    
