def sort_lines_file(filename):
    file=open(filename,'r')
    lines=file.readlines()
    lines.sort(key=len)
    file.close()
    for i in lines:
        if i=="\n":
            continue
        print(i)

filename=input("enter the file name:")

print(sort_lines_file(filename))
