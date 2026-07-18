#1
import math

def silver_word(text):
    if len(text)%2==0:
        return "this text hasn't silver word."
    if len(text)==1:
        return text
    if len(text)>1:
        silver_word=text[math.floor(len(text)/2))]
        return silver_word

text=input("enter a text to give you silver word:")

print("the silver word is :" , silver_word(text))
        

#2
import math

def silver_word(text):
    if len(text)%2==0:
        print("this text hasn't silver word.")
    if len(text)==1:
        return text
    if len(text)>1:
        silver_word=text[math.floor(len(text)/2))]
        return silver_word

text=input("enter a text to give you silver word:")

print("the silver word is :" , silver_word(text))
