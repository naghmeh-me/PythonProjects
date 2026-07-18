import os
from random import choice


while True:
    try:
        name=input("enter the file name:")
    except FileNotFoundError:
        print("please enter valid information.")
        continue
    else:
        if os.path.exists(name):
            with open(name,'r') as file:
                line=file.read()
                list_line=(line.strip()).split()
                winner=choice(list_line)
                print("the winner:",winner)
                continue
        else:
            print("sorry your file is not exist.")
            continue
