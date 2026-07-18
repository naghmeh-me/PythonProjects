import json
import os

filename=input("enter the fule name:")

if os.path.exists(filename):
    #read student records from file
    with open(filename , 'r') as file:
        data=json.load(file)
        #print student information
        for student in data['Student']:
            name=student['Name']
            age=student['Age']
            grades=student['Grade']
            print(f"Name;{name},Age:{age},Grade:{grade}")

else:
    print("this file is not exist.")

print("students record successfully.")
