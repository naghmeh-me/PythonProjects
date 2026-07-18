import xml.etree.ElementTree as ET

filename=input("enter the file name:")

#parse thhe XML file
tree=ET.parse(filename)
#get the element root from the XML
root=tree.getroot()

#extract and display product details
for product in root.findall('product'):
    price=product.find('price')
    if int(price.text)>500:
        price.set('class','expensive')
    else:
        price.text=str(int(price.text) + 0.3 * int(price.text))

tree.write('output.xml')
print("modified XML file successfully.")
