import re

def main():
    # Reading YAML data from the file
    yaml_data = open('schedule.yaml', 'r').read()

    # Function to convert YAML to XML
    def yaml_to_xml(yaml_text):
        # Replace YAML keys and values with XML tags and content
        xml_text = re.sub(r'^(\s*)(\w+):\s*(.*)', r'\1<\2>\3</\2>', yaml_text, flags=re.MULTILINE)
        return xml_text

    # Convert YAML to XML
    xml_data = yaml_to_xml(yaml_data)
    return xml_data

if __name__ == '__main__':
    xml_data = main()
    # Writing XML data to file
    xml_file = open('schedule.xml', 'w')
    xml_file.write(xml_data)
    xml_file.close()