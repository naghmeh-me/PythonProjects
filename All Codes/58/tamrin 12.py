#1
def reverse_string(text):
    text=text[::-1]
    return text

text=input("enter a text:")

print("reverse text:" , reverse_string(text))

#2
def reverse_string(text):
    return text[::-1]

print("foer exit just enter.")

while True:
    text=input("enter a text:")
    if text=="":
        break
    print("reverse text:",reverse_string(text))

