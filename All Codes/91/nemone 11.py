input_file="2.py"
output_file="3.py"
shift=3

try:
    with open(input_file,'r') as file:
        encrypted_content=file.read()
        decrypted_content=""
        for char in encrypted_content:
            if char.isalpha():
                if char.isupper():
                    descrypted_char=chr((ord(char)-ord('A')-shift%26+ord('A')))
                else:
                    descrypted_char=chr((ord(char)-ord('a')-shift%26+ord('a')))
            else:
                descrypted_char=char
            decrypted_content+=descrypted_char

    with open(output_file,'w') as file:
        file.write(decrypted_content)


    print("Descrypted completed succesfuly.")
except FileNotFoundError:
    print("file not found.")
                                        
