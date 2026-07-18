filename1=input("enter the name of file 1:")
filename2=input("enter the name of file 2:")
charecter=input("enter the charecter to remove:")

try:
    with open(filename1,'r') as file1 , open(filename2,'w') as file2:
        content=file1.read()
        modified_content=content.replace(charecter," ")
        file2.write(modified_content)
        print("charecter removed successfuly.")
except FileNotFoundError:
    print("file not found.")


