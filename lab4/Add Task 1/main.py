import xml.etree.ElementTree as ET
import yaml

yaml_data = open('schedule.yaml', 'r').read()

# Parse YAML into a Python data structure
yaml_dict = yaml.load(yaml_data, Loader=yaml.FullLoader)

# Create an XML element for the root
root = ET.Element('root')

# Recursively convert the YAML data to XML
def yaml_to_xml(parent, data):
    for key, value in data.items():
        if isinstance(value, dict):
            element = ET.Element(key)
            yaml_to_xml(element, value)
        else:
            element = ET.Element(key)
            element.text = str(value)
        parent.append(element)

yaml_to_xml(root, yaml_dict)

# Convert the XML tree to a string
xml_data = ET.tostring(root)

xml_file = open('schedule.xml', 'wb')
xml_file.write(xml_data)