class Car:
    wheel_count=4
    def __init__(self,color,brand,model):
        self.color=color
        self.brand=brand
        self.model=model
        self.door_count=4

    def __str__(self):
        return f"{self.color} {self.model} car ,from {self.brand} compony has {self.wheel_count} wheels and {self.door_count} doors."

input_color1=input("enter the color:")
input_color2=input("enter the color:")
input_color3=input("enter the color:")

C1=Car(input_color1,"Ford","Mustang")
C2=Car(input_color2,"Toyota","Perius")
C3=Car(input_color3,"Volkswagen","Golf")

C1.model="Landcruiser"
C2.door_count=2

print(C1)
print(C2)
print(C3)

