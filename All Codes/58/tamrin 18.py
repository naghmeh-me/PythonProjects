reverse_not_reverse=lambda text:"equal" if text[::-1]==text else "not equal"

text=input("enter a text:")

print(f"this text is {reverse_not_reverse(text)} with it's reverse.")
