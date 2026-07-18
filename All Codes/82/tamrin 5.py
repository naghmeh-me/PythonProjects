phone_book={}

def reverse_phone_book(phone_book):
    inverse={}
    for key in phone_book:
        value_=phone_book[key]
        if value_ not in inverse:
            inverse[value_]=key
        else:
            inverse[value_].append(key)
    return inverse
    
def phone_book_1():
    while True:
        try:
            name=input("enter the name:")
            phone_number=int(input("enter the phone number:\n"))
        except ValueError:
            print("please enter valid information.\n")
            continue
        else:
            if name  not in phone_book:
                phone_book[name]=phone_number
                print("phone book:",phone_book,'\n')
                return "phone number inserted successfully.\n"
            else:
                return "sorry this name and number is already exist,\n"

def phone_book_2():
    while True:
        try:
            name=input("enter the name wich you want to delete:\n")
        except:
            print("please enter valid information.\n")
            continue
        else:
            if name in phone_book:
                phone_book.pop(name)
                print("phone book:",phone_book,'\n')
                return "contact deleted successfully.\n"
            else:
                return "sorry there is no contact with this name.\n"

def phone_book_3():
    while True:
        try:
            name=input("enter the name:\n")
        except:
            print("please enter valid information.\n")
            continue
        else:
            if name in phone_book:
                print(f"{name}:{phone_book.get(name)}\n")
                return "serach don.\n"
            else:
                return "sorry there is no contact with this name.\n"

def phone_book_4():
    while True:
        try:
            phone_number=int(input("enter phone phone number:\n"))
        except:
            print("plese enter valid phone number.\n")
            continue
        else:
            reverse_book=reverse_phone_book(phone_book)
            if phone_number in reverse_book:
                print(f"{phone_number} belongs to {reverse_book.get(phone_number)}.\n")
                return "serch don!\n"
            else:
                return "sorry this number is not exist.\n"



def phone_book_5():
    while True:
        try:
            phone_number=int(input("enter the phone number:\n"))
        except:
            print("please enter valid information.\n")
            continue
        else:
            reverse_book=reverse_phone_book(phone_book)
            if phone_number in reverse_book:
                try:
                    new_phone_number=int(input("please enter new phone number:\n"))
                except:
                    print("please enter valid phone number.\n")
                    continue
                else:
                    if new_phone_number not in reverse_book:
                        name=reverse_book.get(phone_number)
                        phone_book[name]=new_phone_number
                        return "changed don!\n"
                    else:
                        return "this new phone number is already exist.\n"
            else:
                return "sorry this phone number is not exist.\n"

def phone_book_6():
    while True:
        try:
            name=input("enter the name:\n")
        except:
            print("plese enter a valid information.\n")
            continue
        else:
            if name in phone_book:
                try:
                    new_name=input("enter the new name:\n")
                except:
                    print("please e nter valid information.\n")
                    continue
                else:
                    if new_name not in phone_book:
                        phone_book[new_name]=(phone_book.get(name))
                        phone_book.pop(name)
                        return "changed don!.\n"
                    else:
                        return "sorry this name is already exist.\n"
            else:
                return "sorry this name is not exist.\n"

def phone_book_7():
    return phone_book
                
                
            
print("enter 0 to break.")

while True:
    try:
        enter=int(input("enter (number) what do you want to do:\n1.insert new contact.\n2.earase phone number.\n3.search phone number.\n4.search name.\n5..change phone number.\n6.change name.\n7.show phone book.\n"))
        if enter==0:
            break
    except:
        print("plese e nter a valid number.\n")
        continue
    else:
        if enter==1:
            print(phone_book_1())
        else:
            if enter==2:
                print(phone_book_2())
            else:
                if enter==3:
                    print(phone_book_3())
                else:
                    if enter==4:
                        print(phone_book_4())
                    else:
                        if enter==5:
                            print(phone_book_5())
                        else:
                            if enter==6:
                                print(phone_book_6())
                            else:
                                if enter==7:
                                    print(phone_book_7())
                                else:
                                    if enter>7 or enter<0:
                                        print("please enter a number between 0 to 8.")
                                        continue
                        
    


     

