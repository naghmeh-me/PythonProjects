file=open('5.py','r')

content=file.read()

print(content)

file.seek(10)

lines=file.readlines()

print(lines)

print(file.tell())

file.close()
