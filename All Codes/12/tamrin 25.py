x=int(input("enter x:"))

y=int(input("enter y:"))

if x==y==0:
    print("نقطه مرکزي")
    print("(0,0)")
else:
     if x==0:
         if y>0:
             print(f"({x},{y})")
             print("نقطه بر  روي خط ربه اول و دوم قرا رادر")
         else:
            if y<0:
                print(f"({x},{y})")
                print("نقطه بر رئي خط ربع سوم و چهارم قرار دارد")
            else:
                if y==0:
                    if x>0:
                        print(f"({x},{y})")
                        print("نقطه ب روي خط ربع اول و چهارم قرار دارد")
                    else:
                        if x<0:
                            print(f"({x},{y})")
                            print("نقطه بد دئي خط ربع سوم و چهارم قرار دارد")
                        else:
                            if x>0 and y>0:
                                print(f"({x},{y})")
                                print("اين نقطه رد ربعع اول قرار دارد")
                            else:
                                if x>0 and y<0:
                                    print(f"({x},{y})")
                                    print("اين نقطه در ربع چهارم قرار دارد")
                                else:
                                    if x<0 and y>0:
                                        print(f"({x},{y})")
                                        print("اين نقطه در ربع دوم قرار دارد")
                                    else:
                                        if x<0 and y<0:
                                            print(f"({x},{y})")
                                            print("اين نقطه در ربع سوم قرار دارد")
           
               
                
