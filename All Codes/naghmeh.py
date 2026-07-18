stuffed_stream=""
def change_to_str(list_input_stream,stuffed_stream):
    for index in list_input_stream:
        stuffed_stream+=index
    return stuffed_stream
    
    
input_stream= input("Please enter the input stream:")

list_input_stream = list(input_stream)

len_input_stream=len(input_stream)

count_=0

for i in list_input_stream:
    home_number_i=list_input_stream.index(i)
    if list_input_stream[home_number_i:home_number_i+5]=='11111':
      list_input_stream.insert(home_number_i,"0")
        
                        

print(f"Frame number one (Input stream)={input_stream}")
print(f"Frame number two (stuffed stream)={change_to_str(list_input_stream,stuffed_stream)}")
print(f"Frame number three (unstuffed stream)={input_stream}")
print(f"Final frame(bit stuffing)=01111110{change_to_str(list_input_stream,stuffed_stream)}")
    
