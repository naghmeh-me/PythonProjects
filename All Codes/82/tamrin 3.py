create_list=input("enter somthings for list:")
list_=(create_list.strip()).split()
print(list_)

while True:
    print("1.add to list 2.remove from list\n3.sort the list 4.count indexs in the list\n5.give the place of index in the list 6.reverse the list")
    choose=int(input("what do you want to do(for exit enter 0:"))
    if choose==1:
        add=input("what do you want to add :")
        list_.append(add)
        print("list:" ,list_)
        continue
    else:
        if choose==2:
            erase=input("what do you want to delete:")
            if erase in list_:
                list_.remove(erase)
                print("list:" ,list_)
                continue
            else:
                print("not found.")
                continue
        else:
            if choose==3:
                sort_=input("how do you want to sort the list:(ascending/descending)")
                if sort_=="ascending":
                    list_.sort()
                    print("list:" ,list_)
                    continue
                else:
                    list_.sort(reverse=True)
                    print("list:" ,list_)
                    continue
            else:
                if choose==4:
                    count_=input("wich index do you want to count:")
                    if count_ in list_:
                        answer=list_.count(count_)
                        print(answer)
                        continue
                    else:
                        print("not found.")
                        continue
                else:
                    if choose==5:
                        index_=input("which index do you want to know where is that place:")
                        if index_ in list_:
                            place=list_.index(index_)
                            print(place)
                            continue
                        else:
                            print("not found.")
                            continue           
                    else:
                        if choose==6:
                            reverse_=input("how do you eant to reverse the list:(ascending/descending")
                            if reverse_=="ascending":
                                sorted(list_)
                                print("reverse ascending list:" ,list_)
                                continue
                            else:
                                sorted(list_,reverse=True)
                                print("reverse descending list:" ,list_)
                                continue
                        else:
                            if choose==0:
                                print("list:" , list_)
                                break


    
