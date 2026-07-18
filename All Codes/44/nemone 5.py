#1
word=input("enter a sentence:")

number=False

for i in word:
    if i.isdigit():
        number=True
        word=word.replace(i,"")
    else:
        word=word.lower()
        

print(word)

#2
print("For exite from the program enter 0(zero).")

while True:
    
    text=input("Enter the text:")
    
    if text=="0":
        break
    
    if text.isalpha() == False:
        for i in text:
            if i.isdigit():
                text=text.replace(i , "")
    else:
        text=text.lower()
    
    print(text)
