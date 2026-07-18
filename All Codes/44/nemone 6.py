#1
counted_char=" "

print("for breaking enter exit.")

while True:
    try:
        word=input("enter a sentence:")
        number=int(input("enter a number:"))
    except:
        print("error!please enter valid enformation.")
        continue
    else:
        if word=="exit":
            break
        else:
            for i in word:
                if word.count(i)==number and i not in counted_char and not i.isspace():
                    print(i)
                    counted_char+=i
                else:
                    if counted_char==" ":
                        print("not found.")


#2
print("for break enter exit.")

while True:
    try:
        words=[]
        text=input("enter the text:")
        if text=="exit":
            break
        number=int(input("enter the number:"))
    except ValueError:
        print("please e nter valid information:")
        continue
    else:
        
        if number<0:
            print("please enter a positive number.")
            continue
        else:
            for i in text:
                if text.count(i)==number and not i.isspace():
                    if i not in words:
                        words.append(i)
            if len(words)==0:
                print(f"sorry there is no word with {number} number.")
            else:
                if " " in words:
                    words.replace(" ","")
                print(words)
                continue
                    

                    
                
                
        
