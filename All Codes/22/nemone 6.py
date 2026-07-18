print("for exit enter exit.")

while True:
    try:
        char=input("enter a charecter:")
    except:
        print("please enter a valid charecter,")
        continue
    else:
        if char=="exit":
            break
        else:
            print(f"code aski {char}:{ord(char)}")
    
