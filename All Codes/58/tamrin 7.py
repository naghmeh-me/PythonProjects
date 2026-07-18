def earase_numbers(text):
    if text.isalpha()==False:
        for i in text:
            if i.isdigit()==True:
                text=text.replace(i,"")
            else:
                continue
    else:
        text=text.lower()
    return text
    

text=input("enter a text:")

print(earase_numbers(text))
