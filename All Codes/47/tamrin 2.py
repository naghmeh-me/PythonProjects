from random import randint

score=0

while True:
    try:
        chance1=randint(1,9)
        print("number:" , chance1)
        guss=input("enter your guss(upper/lower/equal):")
        chance2=randint(1,9)
    except:
        print("error! enter valid information.")
        continue
    else:
        if guss=="upper" and chance2>chance1:
            print(f"the next number is {chance2},you were right!")
            score+=1
            continue
        else:
            if guss=="upper" and chance2<chance1 or chance2==chance1:
                print(f"the next number is {chance2},you were wrong!")
                print("count of your right gusses:" , score)
                break
            else:
                if guss=="lower" and chance2<chance1:
                    print(f"the next number is {chance2},you were right!")
                    score+=1
                    continue
                else:
                    if guss=="lower" and chance2>chance1 or chance2==chance1:
                        print(f"the next number is {chance2},you were wrong!")
                        print("count of your right gusses:" , score)
                        break
                    else:
                        if guss=="equal" and chance2==chance1:
                            print(f"the next number is {chance2},you were right!")
                            score+=1
                            continue
                        else:
                            if guss=="equal" and chance2>chance1 or chance2<chance1:
                                print(f"the next number is {chance2},you were wrong!")
                                print("count of your right gusses:" , score)
                                break
                                
                            
                        
                    
                
            
    
    
    
