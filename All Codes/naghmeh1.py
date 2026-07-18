data = input("Please enter the data:")

list_data = (data.strip()),split()

new_list_data = list_data

new_data = ""

if "SYNC"in list_data[0]:
        home_number = list_data[0].find("SYNC")
        new_data.insert(home_i+1 , "DLE")

for i in new_list_data:
    new_data+=i

print(f"The data = {data}")
print(f"The final frame = {new_data}")
