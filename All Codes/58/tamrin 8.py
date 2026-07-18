x="global"

def change_x(x):
    x="local"
    return x
print("first x was:" , x , "\nnow x is :" , change_x(x))
