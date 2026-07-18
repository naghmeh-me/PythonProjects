class Person:
    gender=""
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Hello i'm {self.name} and i'm {self.age} years old\nGender={self.gender}."

P1=Person("Ali",51)
P1.gender="Male"
P2=Person("Nima",17)
P2.gender="Male"
P3=Person("masome",46)
P3.gender="Female"

print(P1)
print(P2)
print(P3)
        
