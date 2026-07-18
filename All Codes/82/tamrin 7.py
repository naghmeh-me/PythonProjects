#code dorost nist

import math

def Bin_search(list_words,search):
    mid_=math.floor(len(list_words)/2)
    if list_words[mid_]==search:
        return "found"
    else:
        if list_words[mid_]>search:
            Bin_search(list_words[:mid_],search)
        else:
            if list_words[mid_]<search:
                Bin_search(list_words[mid_+1:],search)
            else:
                return "not found"
            
        
words=input("enter some words in a line with distance:")

list_words=sorted((words.strip()).split())

print(list_words)

while True:
    print("for exit just enter.")
    search=input("wich word are you searching for:")
    if search =="":
        break
    else:
        print(Bin_search(list_words,search))
