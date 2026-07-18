#1
file1=open('1.py','r')
file2=open('2.py','w')

text=file1.read()
file2.write(text)

file1.close()
file2.close()

#2
file1=open('1.py','r')
file2=open('2.py','a')

text=file1.read()
file2.write(text)

file1.close()
file2.close()

    
