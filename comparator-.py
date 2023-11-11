import sys
from itertools import islice
from itertools import zip_longest

def line_f(file_path, line_number):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Use islice to skip lines until the desired line number
        desired_line = next(islice(file, line_number - 1, None), None)
    return desired_line

def compare_element(in1, in2, out1):
    a=0
    with open(in1, 'r', encoding='utf-8') as in1_open:
        with open(in2, 'r', encoding='utf-8') as in2_open:
#            print(in1_open)
            for el1, el2 in zip_longest(in1_open, in2_open, fillvalue=None):
                a+=1
                if(el1 == None or el2 == None or el1.strip()!=el2.strip()):
                    print("lines are different")
                print(a)
                print(el1)
                print(el2)




# Check if the input and output file names are provided
if len(sys.argv) != 5:
    print("Usage: python comparator.py input_file1.xml input_file2.xml output_file1.xml output_file2.xml")
    sys.exit(1)

input1_file = sys.argv[1]
input2_file = sys.argv[2]
output1_file = sys.argv[3]
output2_file = sys.argv[4]

compare_element(input1_file, input2_file, output1_file)