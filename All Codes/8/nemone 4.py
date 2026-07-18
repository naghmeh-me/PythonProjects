#1
num=99

count=0

while num<1000:
    num+=1
    if num%3==0:
        count+=1
    else:
        continue

print("total count:" , count)

#2
initial=102

count=0

while initial<=999:
    count+=1
    initial+=3

print(count)

#3
count=0

for i in range(100,1000):
    if int(i)%3==0:
        count+=1

print(count)
        
        

