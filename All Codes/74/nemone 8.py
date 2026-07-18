#1
def del_odd(l):
    for i in l[:]:
        if i%2!=0:
            l.remove(i)
        l.sort(reverse=True)
    return l

n=input("enter numbers:")

n=n.split()

for i in range(len(n)):
    n[i]=int(n[i])

print(del_odd(n))


#2
def remove_odd(l):
    return sorted([x for x in l if x%2==0],reverse=True)

n=input("enter numbers:")

n=n.split()

for i in range(len(n)):
    n[i]=int(n[i])

print(remove_odd(n))

#3
def new_list(numbers):
    numbers=(numbers.strip()).split()
    for i in range(len(numbers)):
        numbers[i]=int(numbers[i])
    new_numbers=list(filter(lambda a:a%2==0,numbers))
    return sorted(new_numbers,reverse=True)
    

print("for break just enter.")

while True:
    try:
        numbers=input("please enter number with space:")
        if numbers=="":
            break
    except:
        print("please e nter valid information.")
        continue
    else:
        print(new_list(numbers))
        
