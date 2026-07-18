list1=['amin' , 'arian' , 'poyan' , 12]
list2=[1 , 22 , 33 , 44]
list3=['amin' , 'arian' , 'poyan' , 12]
list4=['sorena' , 'nader' , 122 , 'arash' , 'tir' , 3]

list1_4=list1+list4
print("list1 + list2=" , list1_4)

list4_1=list4+list1
print("list4 + list1 =" , list4_1)

print("soreana" in list1)

print("sorena" in list4)

print(list1==list3)

print(list1 is list3)

list3[1]="akbar"
print(list3)
print(list1)

print(list2*4)

list5=list1

list5[1]="asghar"
print(list1)

print(list5 is list1)

print(list4[:])
print(list4[:4])
print(list4[2:4])
print(list4[::-1])
print(list4[::-2])
print(list4[:7:2])




