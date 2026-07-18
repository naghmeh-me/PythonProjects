while True:
    a=int(input("enter amount of a from triangle:"))
    if a<0:
        print("error! a is invalid")
        continue
    b=int(input("enter amount of b from triangle:"))
    if b<0:
        print("error! b is invalid")
        continue
    c=int(input("enter amount of c from triangle:"))
    if c<0:
        print("error! c is invalid")
        continue
    if a+b>c and a+c>b and b+c>a:
        if a==b==c:
            print("مثلث نتساويالاضلاع است")
            break
        else:
            if a==b or a==c or b==c:
                print("مثلث متساويالساقين است")
                break
            else:
                print("فقط مثلث ساده است")
                break
    else:
        print("قوانيم براي اين مثلث صدق نميکندپس مثلث نيست")
        break
    
            
          
