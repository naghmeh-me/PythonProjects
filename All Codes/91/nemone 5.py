#1
file=open('2.py','r')

text=file.read()
list_text=(text.strip()).split()

file.close()

print("number of words in this file:",len(list_text))

#2
def count_word(filename):
    file=open(filename,'r')
    words=file.read().split()#make a list
    print(words)
    file.close()
    print(len(words))
    
filename=input("enter the file name:")

count_word(filename)
