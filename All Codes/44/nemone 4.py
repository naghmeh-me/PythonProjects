#1
name1=input("entera name:")

age1=int(input("entera age:"))

name2=input("enter another name:")

print(f"hello i'm {name1} , {age1} years old.")
print(f"hello {name1} , i'm {name2}.")

#2
name1=input("entera name:")

age1=int(input("entera age:"))

name2=input("enter another name:")

text="""hello i'm {name1} , {age} years old
hello {name1} , i'm {name2}"""

print(text.format(name1=name1 , name2=name2 , age=age1))

#3
name1=input("entera name:")

age1=int(input("entera age:"))

name2=input("enter another name:")

text="hello i'm {} , {} years old".format(name1 , age1)
text1="hello {} , i'm {}".format(name1,name2)
print(text,"\n",text1)

