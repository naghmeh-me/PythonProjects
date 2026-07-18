#1
def len_last_word(text):
    list_text=text.split()
    len_list_text=len(list_text)
    len_last_word_in_list_text=len(list_text[len_list_text-1])
    return len_last_word_in_list_text

text=input("enter a text:")

print("lenght last word:" , len_last_word(text))

#2
def lenght_last_word(text):
    text=text.strip()
    word=text.split()
    if word:
        last_word=word[-1]
        print(f"lenght last word :{len(last_word)}")
    else:
        print("there is nothing.")

text=input("enter a text:")

lenght_last_word(text)
