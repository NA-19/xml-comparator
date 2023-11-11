import sys
from lxml import etree

def attribute_sort_key(element):
    # Generate a sort key based on tag and sorted attributes
    attributes_sorted = sorted([f"{k}={v}" for k, v in element.attrib.items()])
    return (element.tag,) + tuple(attributes_sorted)

def sort_element(element):
    # Sort the element's attributes
    sorted_attrib = dict(sorted(element.attrib.items()))
    element.attrib.clear()
    element.attrib.update(sorted_attrib)
    
    # Recursively sort the children of the element
    element[:] = sorted(element, key=attribute_sort_key)
    for child in element:
        sort_element(child)

# Check if the input and output file names are provided
if len(sys.argv) != 3:
    print("Usage: python canonize.py input_file.xml output_file.xml")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Parse the entire XML file into memory
tree = etree.parse(input_file)

# Sort the root element
sort_element(tree.getroot())

# Write the sorted XML to the output file
tree.write(output_file, encoding='utf-8', pretty_print=True, xml_declaration=True)


