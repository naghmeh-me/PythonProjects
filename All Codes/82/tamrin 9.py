def invert_tuple(tuple_):
    x=list(tuple_)
    x.reverse()
    return x

code=input("enter the code:")

code=tuple((code.strip()).split())

print("the right code:" , invert_tuple(code))

           
