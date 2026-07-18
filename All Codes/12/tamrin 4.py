#1
number=int(input("enter a number:"))

initial=1

while initial<=number:
    if initial%6==0:
        print(initial)
        initial+=1
    else:
        initial+=1
        continue

#2
number=int(input("enter a number:"))

initial=1

while initial<=number:
    if initial%6==0:
        print(initial)
     initial+=1

#3
number=int(input("enter a number:"))

for i in range(1,number+1):
    if int(i)%6==0:
        print(i)
    
        
    



    

