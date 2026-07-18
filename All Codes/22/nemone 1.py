#1
from random import randint

x=randint(1,6)

print(x)

#2(dice)

from random import randint

while True:
    x=input("roll a dice:")
    if x=='':
        print(randint(1,6))
    else:
        break

#3
from random import randint

while True:
    x=input("roll a dice:")
    if x=='':
        dice=randint(1,6)
        print(dice)
        if dice==6:
            print("horay! you've got a six.")
    else:
        break

#4
from random import randint

while True:
    dice = randint(1,6)
    number_dice = input("Roll the dice:")
    if number_dice == "exite":
        break
    print(f"Dice:{dice}")

