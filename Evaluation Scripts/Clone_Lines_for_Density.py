import xml.etree.ElementTree as ET

def calculate_total_clone_lines(filename, tool_type):
    total_clone_lines = 0

    if tool_type == 'simian':
        tree = ET.parse(filename)
        root = tree.getroot()
        for clone_set in root.findall('.//set'):
            line_count = int(clone_set.get('lineCount'))
            pair_count = len(clone_set.findall('block'))
            pair_count = pair_count-1
            total_clone_lines += line_count * pair_count

    elif tool_type == 'cpd':
        with open(filename, 'r') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                line = lines[i]
                if "Found a" in line:
                    line_count = int(line.split(" line ")[0].split(" ")[2])
                    pair_count = 0
                    i += 1
                    while i < len(lines) and "Starting at line" in lines[i]:
                        pair_count += 1
                        i += 1
                    pair_count = pair_count - 1
                    total_clone_lines += line_count * pair_count
                else:
                    i += 1

    elif tool_type == 'nicad':
        tree = ET.parse(filename)
        root = tree.getroot()
        for clone_class in root.findall('.//class'):
            line_count = int(clone_class.get('nlines'))
            pair_count = len(clone_class.findall('source'))
            pair_count = pair_count-1
            total_clone_lines += line_count * pair_count

    return total_clone_lines

files = [
    ('/home/vestel/Downloads/Open Source Projects/TestCloneResults/Test Type Compare/Manual/Kivy_unit_simian_filtered.xml', 'simian'),
    ('/home/vestel/Downloads/Open Source Projects/TestCloneResults/Manual/Filtered/Vestel_CPD_Before.xml', 'cpd'),
    ('/home/vestel/Downloads/Open Source Projects/TestCloneResults/Test Type Compare/Manual/Toga_unit_before_Nicad.xml', 'nicad')
]
print("For Vestel")

for filename, tool_type in files:
    total_clone_lines = calculate_total_clone_lines(filename, tool_type)

    print(f"{tool_type} Total Clone Lines: {total_clone_lines}")

