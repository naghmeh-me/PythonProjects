#1
for i in range(101,1000,2):
    sum_=0
    for j in str(i):
        sum_+=int(j)
    if int(i)%sum_==0:
        print(i)
    else:
        continue
#2
list_=[]

for i in range(101,1000,2):
    sum_=0
    for j in str(i):
        sum_+=int(j)
    if i%sum_==0:
        list_.append(i)
        
print(list_)
