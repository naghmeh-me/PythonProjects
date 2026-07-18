from math import pow

class Circle:
    pi=3.14
    def __init__(self,x,y,radious):
        if pow(x,2)+pow(y,2)==pow(radious,2):
            self.x=x
            self.y=y
            self.radious=radious
        else:
            raise ValueError("invalid values for x,y,radious.")
        
    def calculate_area(self):
        return self.pi*pow(self.radious,2)

    def calculate_perimetr(self):
        return 2*self.pi*self.radious

    def __str__(self):
        return f"circle center at ({self.x},{self.y}),radious={self.radious}"

#create instances of circle
try:
    circle1=Circle(3,4,5)
    print(circle1)
    print("Area:",circle1.calculate_area())
    print("Perimter:",circle1.calculate_perimetr())
except ValueError as e:
    print(e)

try:
    circle2=Circle(1,2,2)
    print(circle2)
    print("Area:",circle12.calculate_area())
    print("Perimeter:",circle2.calculate_perimetr())
except ValueError as e:
    print(e)
