#1
contact={}

contact["name"]=input("enter your name:")
contact["email"]=input("enter your email:")
contact["phone_number"]=int(input("enter your phone number:"))

print(contact)

#2
contact={}

print("for exit just enter.")

while True:
    try:
        name=input("enter the name:")
        if name=="":
            break
        emaile=input("enter the email:")
        phone_number=int(input("enter the phone number:"))
    except ValueError:
        print("please e nter valid informayions.")
        continue
    else:
        contact[name]={
        "emaile":emaile,
        "phone number":phone_number
        }
        print("contacts:",contact)


