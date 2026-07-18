for i in range(1000,100000):#2141
    n=i-((i//1000)*1000)#141
    nn=n-((n//100)*100)#41
    yekan=nn-((nn//10)*10)#1
    dahgan=nn//10#4
    sadgan=n//100#1
    hezargan=i//1000#2
    y=yekan+pow(hezargan,4)#17
    x=pow(dahgan,2)+pow(sadgan,3)#17
    if y==x:
        print(i)


    
    
