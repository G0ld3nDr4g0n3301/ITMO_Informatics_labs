def convert_yaml_to_xml(yaml_text):
    # Define a recursive function to process YAML and convert it to XML
    def process_yaml(yaml_lines, level=0):
        xml_result = ""  # Initialize the result
        while yaml_lines:
            line = yaml_lines[0]  # Get the first line of YAML
            if line.strip() == "":
                # Skip empty lines
                yaml_lines.pop(0)
                continue
            indent = len(line) - len(line.lstrip())  # Calculate the current line's indentation
            if indent < level:
                # If the current line is less indented than the previous one, return to the higher level
                break
            yaml_lines.pop(0)  # Remove the processed line from the list
            key, value = line.split(":", 1)  # Split the line into key and value
            key = key.strip()  # Remove leading/trailing whitespace from the key
            value = value.strip()  # Remove leading/trailing whitespace from the value
            if value == "":
                # If the value is empty, it indicates a nested structure
                xml_result += " " * (indent * 2) + f"<{key}>\n"  # Create an XML opening tag
                xml_result += process_yaml(yaml_lines, indent + 1)  # Recursively process nested YAML
                xml_result += " " * (indent * 2) + f"</{key}>\n"  # Create an XML closing tag
            else:
                # If the value is not empty, it's a simple key-value pair
                xml_result += " " * (indent * 2) + f"<{key}>{value}</{key}>\n"
        return xml_result

    yaml_lines = yaml_text.split("\n")  # Split the YAML text into lines
    xml_text = process_yaml(yaml_lines)  # Start the conversion process
    return xml_text

# Example YAML data
yaml_data = open('schedule.yaml', 'r').read()
# Convert YAML to XML
xml_data = convert_yaml_to_xml(yaml_data)
xml_file = open('schedule.xml', 'w')
xml_file.write(xml_data)
xml_file.close()