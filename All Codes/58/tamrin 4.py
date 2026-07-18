#1
def count_letters(text,number):
    readed_text=" "
    for i in text:
        if text.count(i)==number and i not in readed_text and not i.isspace():
            readed_text+=i
            return i
        continue
                
text=input("enter a text:")
def_=True

while True:
    try:
        number=int(input("enter a number:"))
    except:
        def_=False
        print(def_)
    else:
        break

if def_:
    print(count_letters(text,number))
else:
    print("eroor!")
    
#2
def count_char(text,n):
    if function==True:
        for i in taxt:
            if text.count(i)==n and i not in i.isspace():
                return i
            else:
                continue
    else:
        return "error"

while True:
    try:
        function=True
        text=input("enter a text:")
        n=int(input("enter a number:"))
    except:
        function=False
        print(function , "\nenter valid information.")
        continue
    else:
        print(count_char(text,n))
        break
        
        
        

