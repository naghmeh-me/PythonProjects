import xml.etree.ElementTree as ET

filename=input("enter the file name:")

#parse thhe XML file
tree=ET.parse(filename)
#get the element root from the XML
root=tree.getroot()

#extract and display product details
for product in root.findall('product'):
    id=product.find('id').text
    name=product.find('name').text
    price=product.find('price').text
    description=product.find('description').text

    print(f"product ID:{id}")
    print(f"NAME:{name}")
    print(f"PRICE:{price}")
    print(f"DESCRIPTION:{description}")
    print()
