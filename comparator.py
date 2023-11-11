import sys
from lxml import etree
from itertools import zip_longest

def compare_element(in1, in2, out1, out2):
    attrs1 = tuple(in1.attrib.items())
    attrs2 = tuple(in2.attrib.items())

#    if attrs1 != attrs2:
#        out1.append(in1)
#        out2.append(in2)
#    for element in in1.iter():
#        print(etree.tostring(element, pretty_print=True).decode())
#    for element in in2.iter():
#        print(etree.tostring(element, pretty_print=True).decode())
    a=0	
#    for element1, element2 in zip(in1.iter(), in2.iter()):
#        a+=1
#        print("iteration", a)
        
#        if element1 is not None:             
#            print(etree.tostring(element1, pretty_print=True).decode())
#        if element2 is not None:             
#            print(etree.tostring(element2, pretty_print=True).decode())

    for element1, element2 in zip_longest(in1.iter(), in2.iter(), fillvalue=None):
        print("iteration: ", a)
        a+=1           
        if element1 is not None and element2 is not None:
            # Compare elements or perform other operations
            if (etree.tostring(element1, pretty_print=True).decode()) == (etree.tostring(element2, pretty_print=True).decode()):
                print("Elements match.")
            else:
                print("Elements do not match.")
                print("element1:")
                print(etree.tostring(element1, pretty_print=True).decode())
                print("element2:")
                print(etree.tostring(element2, pretty_print=True).decode())
        elif element1 is not None:
            print("Element only in XML File 1:")
            print(etree.tostring(element1, pretty_print=True).decode())
        elif element2 is not None:
            print("Element only in XML File 2:")
            print(etree.tostring(element2, pretty_print=True).decode())

#    for element in in1.iter(tag=etree.Element):
#        print("%s - %s" % (element.tag, element.text))


# здесь нужен цикл, в котором мы будем двигаться по child item'ам одновременно в in1 и in2
# ...

# Check if the input and output file names are provided
if len(sys.argv) != 5:
    print("Usage: python comparator.py input_file1.xml input_file2.xml output_file1.xml output_file2.xml")
    sys.exit(1)

input1_file = sys.argv[1]
input2_file = sys.argv[2]
output1_file = sys.argv[3]
output2_file = sys.argv[4]

# Parse the entire XML file into memory
tree1 = etree.parse(input1_file)
tree2 = etree.parse(input2_file)
tree3 = etree.ElementTree(etree.Element("root"))
tree4 = etree.ElementTree(etree.Element("root"))

# Sort the root element
compare_element(tree1.getroot(), tree2.getroot(), tree3.getroot(), tree4.getroot())

# Write the sorted XML to the output file
tree3.write(output1_file, encoding='utf-8', pretty_print=True, xml_declaration=True)
tree4.write(output2_file, encoding='utf-8', pretty_print=True, xml_declaration=True)