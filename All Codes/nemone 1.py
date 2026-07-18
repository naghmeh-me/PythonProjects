class Animals:
    def __init__(self,name,age,race):
        self.name=name
        self.age=age
        self.race=race
        self.eye_count=2

    def __str__(self):
        return f"hi i'm {self.name},{self.age} years old, i have {self.eye_count} eyes and i'm a {self.race} dog."

A1=Animals("Brouse",5,"Neopolitan Mastiff")
A2=Animals("Poppy",2,"Maltese")
A3=Animals("Chessnut",3,"Chow Chow")

cat=Animals(name="Garfield",age=10,race="Persian")

print(A1,'\n',A2,'\n',A3)
print(cat.name)
print(cat.age)
print(cat.race)
cat.eye_count=1
print(cat.eye_count)

print(type(cat))
