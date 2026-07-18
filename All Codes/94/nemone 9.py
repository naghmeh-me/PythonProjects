#kar nemikone
import xml.etree.ElementTree as ET
import os

filename=input("enter the file name:")

if os.path.exists(filename):
    #parse thhe XML file
    tree=ET.parse(filename)
    #get the element root from the XML
    root=tree.getroot()
    #access & work with XML data
    for child in root:
        print(child.tag , child.attrib)
    #find elements with specific tags
    element=root.findall("Name")
    for elemnts in elements:
        print(element.find("Feature").text)
