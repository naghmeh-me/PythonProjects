count_not_vowels=lambda text:sum(1 for i in text if i.lower() not in "aioue" )

text=input("enter a text:")

print("count od not vowels word:" , count_not_vowels(text))
