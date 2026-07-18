from random import choice

text=input("enter a text:")

for i in text:
    if i==" ":
        text=text.replace(i,"")

choice_=choice(text)

print("random cahrecter is :",choice_)

