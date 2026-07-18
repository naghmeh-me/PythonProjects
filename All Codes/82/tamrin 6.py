#1
def set_works(set1,set2):
    print("اجتماع:",set1|set2)
    print("اشتراک:",set1&set2)
    print("تفاضل(set1-set2):",set1-set2)
    print("تفاضل(set2-set1):" , set2-set1)
    print("تفاضل متقارن(set1^set2):" , set1^set2)
    print("تفاضل متاقرن(set2^set1):" , set2^set1)
    return "end"
    

set1=input("enter set one:")
set2=input("enter set two:")

set1=set(set1.strip())
set2=set(set2.strip())

print(set_works(set1,set2))

#2
def sets(set1_,set2_):
    print(f"UNION={set1_|set2_}")
    print(f"INTERSECTION={set1_&set2_}")
    print(f"DIFFERENCE(set1-set2)={set1_-set2_}")
    print(f"DIFFERENCE(set2-set2)={set2_-set1_}")
    print(f"SEMMETRIC-DEFFERENCE={set1_^set2_}")
    return 'DON!'
    

print("just enter for exit.")

while True:
    try:
        set1=input("enter index set one with distance:")
        if set1=="":
            break
        set2=input("enter index set two with distance:")
    except ValueError:
        print("please enter valid information.:")
        continue
    else:
        set1_=set((set1.strip()).split())
        set2_=set((set2.strip()).split())
        print(sets(set1_,set2_))
        



