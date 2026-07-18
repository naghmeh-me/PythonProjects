#1
hour = int(input("enter the hour:"))
minute = int(input("enter the minute:"))
second = int(input("enter the second:"))

new_second = hour * 3600 + minute * 60 + second

print(str(new_second) + "second")

#2
minut=int(input("ener the minut:"))
second=int(input("enter the second:"))

print(minut*60+second,"second")

#3
while True:
    print("make any time to second.")
    
    second=int(input("Please enter thes second:"))
    minute=int(input("Please enter thes minute:"))
    houre=int(input("Please enter thes houre:"))
    
    print(f"The total second = {(houre*3600) + (minute*60) + second} seconds.")
    
    againe = input("Do you want to do this againe?(y/n):")
    if againe == "n":
        print("It was fun, let's do thos again soon.")
        break
