#1
def count_vowels(text):
    return sum(1 for char in text if char.lower() in "aioue")

text=input("enter a text:")

print("count of vowels in text:" , count_vowels(text))

#2
def count_vowels(text):
    count_=0
    for i in text:
        if i in "aioue":
            count_+=1
        else:
            continue
    return count_

text=input("enter a text:")

print("count of vowels in text:" , count_vowels(text))
