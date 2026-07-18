list_=['book',True,12,'novel',100,12,False,12,'farvardin',13]

list_.pop(-1)
print(list_,'\n')

list_.append('python')
print(list_,'\n')

list_.append('6')
print(list_,'\n')

list_.extend('apple')
print(list_,'\n')

list_.insert(3,'amore')
print(list_,'\n')

print('\n',list_.count(12),'\n')

list_.remove(12)
print(list_,'\n')

list_.remove('farvardin')
print(list_,'\n')

print(list_.index(True) , '\n')

del list_[6:]
print(list_,'\n')

list_.reverse()
print(list_,'\n')

list_.clear()
print(list_,'\n')

list2=[8,-1,7,-2,9,0]

list2.sort(reverse=True)
print(list2,'\n')

list2.sort(reverse=False)
print(list2,'\n')
