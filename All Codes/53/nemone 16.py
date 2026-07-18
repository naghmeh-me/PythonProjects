vowels=lambda text:sum(1 for i in text if i.lower() in 'aioue')

text=input("enter a text:")

print("the number of vowels in text:" , vowels(text))
