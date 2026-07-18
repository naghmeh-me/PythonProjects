#1
initial=9

count=0

while initial<100:
    if initial%4==0:
        count+=1
        initial+=1
        continue
    else:
        initial+=1
        continue

print(count)

#2
count=0

for i in range(10,100):
    if i%4==0:
        count+=1
    else:
        continue

print(count)
