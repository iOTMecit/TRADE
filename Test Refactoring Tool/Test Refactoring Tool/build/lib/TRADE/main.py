import os
import time
import xml.etree.ElementTree as ET
import re
import argparse

CONTEXT_SIZE = 2  # Number of lines before/after to check
stored_differences = {}
global_param_deff= []
param_index = 1
common_blocks = []
function_counter = 1
old_line_count_80 = 0
new_line_count_80 = 0
signal_eighty = 0

def parse_args():
    parser = argparse.ArgumentParser(description="Process and refactor files based on XML clone data.")
    parser.add_argument('--xml_path', type=str, required=True, help="Path to the XML file to process")
    return parser.parse_args()

def read_non_comment_lines(filepath, start_line=None, end_line=None):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    if start_line is not None and end_line is not None:
        lines = lines[start_line - 1:end_line]

    non_comment_lines = []
    in_block_comment = False

    for line in lines:
        stripped_line = line.strip()

        # Detect start of block comments or multi-line string literals
        if (stripped_line.startswith("'''") or stripped_line.startswith('"""')) and not in_block_comment:
            # Check if it's a single-line block comment (e.g., """comment""")
            if stripped_line.endswith("'''") or stripped_line.endswith('"""'):
                continue
            else:
                # Start of a multi-line block comment
                in_block_comment = True
                continue

        # Detect end of block comments or multi-line string literals
        if in_block_comment:
            if stripped_line.endswith("'''") or stripped_line.endswith('"""'):
                in_block_comment = False
            continue

        # Skip single-line comments
        if stripped_line.startswith('#'):
            continue

        # If not in a block comment, add the line
        if not in_block_comment:
            non_comment_lines.append(line.rstrip('\n'))

    return non_comment_lines

def extract_code_from_file(file_path, start_line, end_line):
    """
    Extracts code from a file given a start line and end line.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return ''.join(lines[start_line - 1:end_line])


def has_class_dependency(lines):
    """Check if a given function has class dependency."""
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('def ') and ('self' in stripped_line or 'cls' in stripped_line):
            return True
        if 'self.' in stripped_line or 'cls.' in stripped_line:
            return True
    return False

def has_class_dependency_80(function_code_blocks):
    """Check if a given function has class dependency."""
    for block in function_code_blocks:
        for line in block:
            stripped_line = line.strip()
            if stripped_line.startswith('def ') and ('self' in stripped_line or 'cls' in stripped_line):
                return True
            if 'self.' in stripped_line or 'cls.' in stripped_line:
                return True
    return False


def extract_up_to_marker(line, marker="#"):
    marker_position = line.find(marker)
    if marker_position != -1:
        line = line[:marker_position].strip()
        return line  # Get the part up to the marker and trim whitespace
    else:
        return line.strip()  # If no marker is found, return the entire line trimmed


def is_empty_or_comment(line):
    stripped = line.strip()
    return not stripped or stripped.startswith("#")

def find_matching_line(target_line, lines, start, end):
    for k in range(start, end):
        if extract_up_to_marker(lines[k]) == extract_up_to_marker(target_line):
            return k
    return None

def sync_compare_files_ignore_comments(file1_lines, file2_lines):
    differences = []
    i, j = 0, 0

    if file1_lines and file2_lines:
        differences.append((0, 0, file1_lines[0], file2_lines[0]))
        i += 1
        j += 1

    while i < len(file1_lines) and j < len(file2_lines):
        # Skip empty or comment lines
        if is_empty_or_comment(file1_lines[i]):
            i += 1
            continue
        if is_empty_or_comment(file2_lines[j]):
            j += 1
            continue

        if file1_lines[i] != file2_lines[j]:
            file1_part = extract_up_to_marker(file1_lines[i])
            file2_part = extract_up_to_marker(file2_lines[j])

            if file1_part == file2_part:
                differences.append((i, j, file1_lines[i], file2_lines[j]))
                i += 1
                j += 1
            else:
                found_match = False

                # Check the next few lines for a match in file1
                if i + 1 < len(file1_lines) and extract_up_to_marker(file1_lines[i + 1]) == file2_part:
                    differences.append((i, j, file1_lines[i], None))  # file1 is missing this line
                    i += 1
                elif j + 1 < len(file2_lines) and extract_up_to_marker(file2_lines[j + 1]) == file1_part:
                    differences.append((i, j, None, file2_lines[j]))  # file2 is missing this line
                    j += 1
                else:

                    match_j = find_matching_line(file2_lines[j], file1_lines, i + 1, min(i + 1 + CONTEXT_SIZE, len(file1_lines)))
                    if match_j is not None:
                        differences.append((i, j, None, file2_lines[j]))
                        j += 1
                        i = match_j
                        found_match = True

                    # Check the next few lines for a match in file2
                    match_i = find_matching_line(file1_lines[i], file2_lines, j + 1, min(j + 1 + CONTEXT_SIZE, len(file2_lines)))
                    if match_i is not None:
                        differences.append((i, j, file1_lines[i], None))
                        i += 1
                        j = match_i
                        found_match = True

                    if not found_match:
                        differences.append((i, j, file1_lines[i], file2_lines[j]))
                        i += 1
                        j += 1
        else:
            differences.append((i, j, file1_lines[i], file2_lines[j]))
            i += 1
            j += 1

    while i < len(file1_lines):
        if not is_empty_or_comment(file1_lines[i]):
            differences.append((i, len(file2_lines), file1_lines[i], None))
        i += 1

    while j < len(file2_lines):
        if not is_empty_or_comment(file2_lines[j]):
            differences.append((len(file1_lines), j, None, file2_lines[j]))
        j += 1

    return differences


def refactor_and_generate_function(differences, function_name, function_2_name, line_count_primer, line_count_seconder, store_first=False):
    param_function_code = []
    param_definitions = []
    param_assignments = {}
    unique_params = {}
    global param_index
    global global_param_deff  # Declare it as global

    def add_with_indent(line, parameter_name=None):
        leading_spaces = len(line) - len(line.lstrip())
        reduced_indent = max(leading_spaces - 4, 0)
        if parameter_name:
            return f"{' ' * reduced_indent}exec({parameter_name})"
        return ' ' * reduced_indent + line.lstrip()

    if store_first:
        for diff in differences[1:]:
            i, j, line1, line2 = diff

            if line1 is not None and line2 is not None and line1.strip() == line2.strip():
                param_function_code.append(add_with_indent(line1))
            elif line1 is not None and line2 is not None:
                if line1.strip() == "" and line2.strip() == "":
                    param_function_code.append(add_with_indent(line1))
                else:
                    param_name = f"param{param_index}"
                    if param_name not in unique_params:
                        unique_params[param_name] = (line1.strip(), line2.strip())
                        param_definitions.append(f"{param_name}='{line1.strip()}'")
                        global_param_deff = param_definitions
                        param_assignments[param_name] = line2.strip()
                        stored_differences[(i, j)] = {
                            'param_name': param_name,
                            'line1': line1,
                            'line2': line2,
                            'param_index': param_index
                        }
                        param_index += 1
                    param_function_code.append(add_with_indent(line1, param_name))
            elif line1 is not None:
                if line1.strip() != "":
                    param_name = f"param{param_index}"
                    if param_name not in unique_params:
                        unique_params[param_name] = (line1.strip(), None)
                        param_definitions.append(f"{param_name}='{line1.strip()}'")
                        global_param_deff = param_definitions
                        param_assignments[param_name] = " "  # Handle missing line with a space
                        stored_differences[(i, j)] = {
                            'param_name': param_name,
                            'line1': line1,
                            'line2': line2,
                            'param_index': param_index
                        }
                        param_index += 1
                    param_function_code.append(add_with_indent(line1, param_name))
                else:
                    param_function_code.append(add_with_indent(line1))
            elif line2 is not None:
                if line2.strip() != "":
                    param_name = f"param{param_index}"
                    if param_name not in unique_params:
                        unique_params[param_name] = (None, line2.strip())
                        param_definitions.append(f"{param_name}=' '")  # Handle missing line with a space
                        global_param_deff = param_definitions
                        param_assignments[param_name] = line2.strip()
                        stored_differences[(i, j)] = {
                            'param_name': param_name,
                            'line1': line1,
                            'line2': line2,
                            'param_index': param_index
                        }
                        param_index += 1

                    param_function_code.append(add_with_indent(line2, param_name))
    else:
        for diff in differences[1:]:
            i, j, line1, line2 = diff
            if line1 is not None:
                stripped_line = line1.strip()
                striping_name = stripped_line.split("m")[0].strip()

                if striping_name == 'exec(para':
                    param_name = stripped_line.split("(")[1].split(")")[0].strip()
                    if line2 is not None:  # Add this condition to check if line2 is not None
                        param_assignments[param_name] = line2.strip()
                    else:
                        param_assignments[param_name] = None  # Handle the case where line2 is None


        for diff in differences[1:]:
            i, j, line1, line2 = diff
            if line1 is not None:
                stripped_line = line1.strip()
                striping_name = stripped_line.split("m")[0].strip()

                if striping_name == 'exec(para':
                    param_function_code.append(add_with_indent(line1))
                    continue

            if line1 is not None and line2 is not None and line1.strip() == line2.strip():
                param_function_code.append(add_with_indent(line1))
            elif line1 is not None and line2 is not None:
                if line1.strip() == "" and line2.strip() == "":
                    param_function_code.append(add_with_indent(line1))
                else:
                    param_name = f"param{param_index}"
                    if param_name not in unique_params:
                        unique_params[param_name] = (line1.strip(), line2.strip())
                        param_definitions.append(f"{param_name}='{line1.strip()}'")
                      #  global_param_deff.extend(param_definitions)  # Append new definitions
                        param_assignments[param_name] = line2.strip()
                        stored_differences[(i, j)] = {
                            'param_name': param_name,
                            'line1': line1,
                            'line2': line2
                        }
                        param_index += 1
                    param_function_code.append(add_with_indent(line1, param_name))
            elif line1 is not None:
                if line1.strip() != "":
                    param_name = f"param{param_index}"
                    if param_name not in unique_params:
                        unique_params[param_name] = (line1.strip(), None)
                        param_definitions.append(f"{param_name}='{line1.strip()}'")
                     #   global_param_deff.extend(param_definitions)  # Append new definitions
                        param_assignments[param_name] = " "  # Handle missing line with a space
                        stored_differences[(i, j)] = {
                            'param_name': param_name,
                            'line1': line1,
                            'line2': line2
                        }
                        param_index += 1
                    param_function_code.append(add_with_indent(line1, param_name))
                else:
                    param_function_code.append(add_with_indent(line1))
            elif line2 is not None:
                if line2.strip() != "":
                    param_name = f"param{param_index}"
                    if param_name not in unique_params:
                        unique_params[param_name] = (None, line2.strip())
                        param_definitions.append(f"{param_name}=' '")  # Handle missing line with a space
                      #  global_param_deff.extend(param_definitions)  # Append new definitions
                        param_assignments[param_name] = line2.strip()
                        stored_differences[(i, j)] = {
                            'param_name': param_name,
                            'line1': line1,
                            'line2': line2
                        }
                        param_index += 1
                    param_function_code.append(add_with_indent(line2, param_name))

        global_param_deff.extend(param_definitions)

    param_function_code_str = '\n'.join(param_function_code)
    empty_rows = line_count_primer - len(param_function_code)
    added_empty_rows = ['\n'] * empty_rows
    added_empty_rows_str = ''.join(added_empty_rows)

    param_definitions_str = ', '.join(global_param_deff)
    indented_code = '\n    '.join(param_function_code_str.split('\n'))
    indented_code_with_blanks = indented_code + added_empty_rows_str

    refactored_code = f"def {function_name}, {param_definitions_str}):\n    {indented_code_with_blanks}"

    param_assignments_str = ', '.join([f"{k}='{v}'" for k, v in param_assignments.items()])
    function_call = f"def {function_2_name}\n\t{function_name}, {param_assignments_str})"
    empty_rows_seconder = line_count_seconder - len(function_call.split('\n'))
    added_empty_rows_seconder = ['\n'] * empty_rows_seconder
    added_empty_rows_seconder_str = ''.join(added_empty_rows_seconder)
    function_call = function_call + added_empty_rows_seconder_str

    return refactored_code, function_call, param_function_code

def replace_lines_in_file(file_path, start_line, end_line, replacement_code):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for i, line in enumerate(lines):
            if i + 1 == start_line:
                file.write(replacement_code + '\n')
            if not (start_line <= i + 1 <= end_line):
                file.write(line)


def add_import_to_file(import_statement, target_file):
    """Belirtilen import cümlesini hedef dosyanın başına ekler."""
    with open(target_file, 'r') as file:
        content = file.read()

    # Import cümlesini dosyanın başına ekle
    new_content = import_statement + '\n' + content

    # Dosyayı güncelle
    with open(target_file, 'w') as file:
        file.write(new_content)

def convert_path_to_module(file_path, base_directory):
    """Dosya yolunu Python modül adlandırmasına çevirir."""
    relative_path = os.path.relpath(file_path, base_directory)
    module_path = relative_path.replace(os.path.sep, '.')
    module_name = os.path.splitext(module_path)[0]  # .py uzantısını kaldır
    return module_name

def code_length_difference(code_line, start_point , end_point):
    """Kaydırma yapmmak için."""
    refactored_code_length = len(code_line) + 1
    code_length = end_point - start_point
    difference = (code_length - refactored_code_length) - 1

    return code_length, refactored_code_length, difference

def extract_variables(lines):

    variables = set()
    variable_pattern = re.compile(r'(\b\w+\b)\s*=')

    for line in lines:
        matches = variable_pattern.findall(line)
        variables.update(matches)

    return variables


def is_comment_or_docstring(line):
    stripped = line.strip()
    return stripped.startswith("#") or stripped.startswith("'''") or stripped.endswith("'''")


def has_unmatched_closing_bracket(lines):
    opening_brackets = {'(': ')', '{': '}', '[': ']'}
    closing_brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    # Check all lines except the last one for 'return'
    for i, line in enumerate(lines[:-1]):
        stripped_line = line.strip()
        if stripped_line.startswith('return'):
            print(f"Return statement found in line {i + 1} (not the last line): {stripped_line}")
            return True

    # Check the last line normally (which could contain 'return')

    for char in lines:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if stack and stack[-1] == closing_brackets[char]:
                stack.pop()
            else:
                print(f"Unmatched closing bracket found in line: {lines[-1].strip()}")
                return True

    if stack:
        print("Unmatched opening brackets remain in stack.")
    return bool(stack)



def find_common_lines_80(func1_lines, func2_lines, type , min_length=5):
    global common_blocks, function_counter
    length1, length2 = len(func1_lines), len(func2_lines)
    equal_counter = 0
    i = 0
    if type == 0:
        while i < length1:
            j = 0
            start_i = i
            while j < length2:
                temp_common = []
                start_j = j

                while (i < length1 and j < length2 and
                       func1_lines[i].strip() == func2_lines[j].strip() and
                       not is_comment_or_docstring(func1_lines[i])):
                    temp_common.append(func1_lines[i])
                    i += 1
                    j += 1

                if temp_common and temp_common[-1].strip().startswith("return"):
                    temp_common = temp_common[:-1]

                if len(temp_common) >= min_length:

                    if has_unmatched_closing_bracket(temp_common):
                        print("Aborting refactor due to unmatched closing brackets.")
                        i = start_i
                        break
                    else:
                        function_name = f"extracted_function_{function_counter}"
                        function_counter += 1
                        common_blocks.append((function_name, temp_common))
                        j = start_j + len(temp_common)
                        i = start_i + len(temp_common)
                        start_i = i

                else:
                    j += 1
                    i = start_i

            i += 1
    else:
        if func1_lines and func1_lines[0].strip().startswith("def"):
            func1_lines = func1_lines[1:]  # Listenin başındaki 'def' satırını çıkar

        if len(func1_lines) > 1 and func1_lines[0].strip().startswith("nonlocal"):
            func1_lines = func1_lines[1:]  # İkinci sıradaki 'nonlocal' satırını çıkar

        if func1_lines and func1_lines[-1].strip().startswith("extracted"):
            func1_lines = func1_lines[:-1]


        while i < len(func1_lines):
            j = 0
            start_i = i
            while j < length2:
                temp_common = []
                start_j = j

                while (i < length1 and j < length2 and
                       func1_lines[i].strip() == func2_lines[j].strip()):
                    temp_common.append(func1_lines[i])
                    equal_counter += 1
                    i += 1
                    j += 1

                length1 = len (func1_lines)

                if equal_counter == len(func1_lines):
                    for line in temp_common:
                        print(line.strip())
                    function_name = f"extracted_function_{function_counter}"
                    function_counter += 1
                    j = start_j + len(temp_common)
                    i = start_i + len(temp_common)
                    start_i = i
                    equal_counter = 0

                else:
                    j += 1
                    i = start_i

            i += 1


    return common_blocks if common_blocks else []

def add_with_relative_indent(line, base_indent):

    leading_spaces = len(line) - len(line.lstrip())
    relative_indent = leading_spaces + base_indent
    adjusted_indent = max(relative_indent, 0)
    return ' ' * adjusted_indent + line.lstrip()


def refactor_functions_80(func1, func2, path1, path2, type):
    func1_lines = func1
    func2_lines = func2
    global old_line_count_80, new_line_count_80, signal_eighty

    common_blocks = find_common_lines_80(func1_lines, func2_lines, type)

    if type == 0:
        if common_blocks:
            refactored_functions = []
            func1_refactored, func2_refactored = '\n'.join(func1), '\n'.join(func2)  # List to string conversion

            for i, (function_name, lines) in enumerate(common_blocks):
                variables = extract_variables(lines)

                first_common_line = lines[0]
                base_indent = len(first_common_line) - len(first_common_line.lstrip())

                # Refactored code block
                refactored_code = []
                refactored_code.append(add_with_relative_indent(f"def {function_name}():", base_indent))

                # Add nonlocal declaration if variables are found
                if variables:
                    nonlocal_declaration = "nonlocal " + ", ".join(variables)
                    refactored_code.append(add_with_relative_indent(nonlocal_declaration, base_indent + 4))

                # Add the lines of the common block to the refactored code
                refactored_code += [
                    add_with_relative_indent(line, base_indent) for line in lines if
                    not (line.strip().startswith("return") and line == lines[-1])
                ]
                refactored_code.append(add_with_relative_indent(f"{function_name}()", base_indent))

                # Save refactored code as a new function in the list
                refactored_functions.append(refactored_code)

                # Refactored function call for func2 with the same base indentation as the common block
                refactored_function_call = add_with_relative_indent(f"{function_name}()", base_indent)

                # Calculate the difference in line count between the original and refactored code
                original_line_count = len(lines)
                refactored_line_count = len(refactored_code)
                refactored_line_count_2 = 1

                # Add the difference in blank lines after the function call in func2
                if refactored_line_count < original_line_count:
                    blank_lines_to_add_1 = original_line_count - refactored_line_count
                    refactored_code += ['\n'] * blank_lines_to_add_1  # Add blank lines
                elif refactored_line_count_2 < original_line_count:
                    blank_lines_to_add_2 = original_line_count - refactored_line_count_2
                    refactored_function_call += '\n' * blank_lines_to_add_2

                # Convert back to strings before performing replacements
                common_block_text = "\n".join(lines)
                refactored_code_text = '\n'.join(refactored_code)

                old_line_count_80 = len(func1)

                # Perform replacements on string versions
                func1_refactored = func1_refactored.replace(common_block_text, refactored_code_text)

                if i == len(common_blocks) - 1:
                    func1_new = func1_refactored.split("\n")
                    new_line_count_80 = len(func1_new)
                    if path1 == path2:
                        blank_lines_to_remove_2 = (new_line_count_80 - old_line_count_80 )
                        if blank_lines_to_remove_2 > 0 and signal_eighty == 0:
                            refactored_function_call = refactored_function_call[:-blank_lines_to_remove_2]
                            signal_eighty = 1

                func2_refactored = func2_refactored.replace(common_block_text, refactored_function_call)

            return refactored_functions, func1_refactored, func2_refactored, function_name
        else:
            return None, '\n'.join(func1), '\n'.join(func2), None
    else:

        if common_blocks:
            refactored_functions = []
            func1_refactored, multi_refactored = func1, func2  # Convert list to string

            for i, (function_name, lines) in enumerate(common_blocks):

                first_common_line = lines[0]
                base_indent = len(first_common_line) - len(first_common_line.lstrip())

                # Refactored function call for func2 with the same base indentation as the common block
                refactored_function_call = add_with_relative_indent(f"{function_name}()", base_indent)

                # Calculate the difference in line count between the original and refactored code
                original_line_count = len(lines)
                refactored_line_count = 1

                # Add the difference in blank lines after the function call in func2
                if refactored_line_count < original_line_count:
                    blank_lines_to_add = original_line_count - refactored_line_count
                    refactored_function_call += "\n" * blank_lines_to_add

                # Replace the common block in func2 with the function call
                common_block_text = "\n".join(lines)


                if path1 == path2:
                    blank_lines_to_remove_2 = (new_line_count_80 - old_line_count_80 )
                    if blank_lines_to_remove_2 > 0 and signal_eighty == 0:
                        refactored_function_call = refactored_function_call[:-blank_lines_to_remove_2]
                        signal_eighty = 1



                # Perform replacement on string version of func2
                multi_refactored = multi_refactored.replace(common_block_text, refactored_function_call)

            return func1, func1, multi_refactored, function_name
        else:
            return None, '\n'.join(func1), '\n'.join(func2), None


def parse_xml_and_compare(xml_file_path):
    tree = ET.parse(xml_file_path)
    base_path = os.getenv('BASE_PATH', os.path.dirname(os.path.abspath(__file__)))
    root = tree.getroot()
    multi_clone = 2
    multi_clone_ary = []
    multi_array_path = []
    multi_array_start = []
    multi_array_end = []

    function_length = 0
    # Find all clone classes and store them with their similarity
    clone_classes = []
    for clone_class in root.findall('.//class'):
        similarity = int(clone_class.attrib['similarity'])
        clone_classes.append((clone_class, similarity))

    # Sort the clone classes by similarity in descending order
    sorted_clone_classes = sorted(clone_classes, key=lambda x: x[1], reverse=True)

    # Remove all existing class elements from the XML tree
    for clone_class, _ in clone_classes:
        root.remove(clone_class)

    # Add the sorted classes back to the XML tree
    for clone_class, similarity in sorted_clone_classes:
        root.append(clone_class)

    # Save the modified XML to the original file
    tree.write(xml_file_path)
    for clone in root.findall('class'):
        time.sleep(2)
        similarity = float(clone.get('similarity'))
        ismultipair = int(clone.get('nclones'))
        global global_param_deff
        global_param_deff = []
        global param_index

        param_index = 1
        source_files = clone.findall('source')

        file1_path = os.path.join(base_path, source_files[0].get('file'))
        file1_start_line = int(source_files[0].get('startline'))
        file1_end_line = int(source_files[0].get('endline'))

        file2_path = os.path.join(base_path, source_files[1].get('file'))
        file2_start_line = int(source_files[1].get('startline'))
        file2_end_line = int(source_files[1].get('endline'))

        if not os.path.exists(file1_path):
            print(f"File not found: {file1_path}")
            continue

        if not os.path.exists(file2_path):
            print(f"File not found: {file2_path}")
            continue

        if 90 <= similarity <= 100:


            file1_lines = read_non_comment_lines(file1_path, file1_start_line, file1_end_line)
            file2_lines = read_non_comment_lines(file2_path, file2_start_line, file2_end_line)
            line_count = file1_end_line - file1_start_line
            line_count_2 = file2_end_line - file2_start_line + 1

            if has_class_dependency(file1_lines) or has_class_dependency(file2_lines):
                print(f"Function in {file1_path} or {file2_path} is unrefactorable due to class dependency.")
            else:
                # Orijinal fonksiyon adını belirle
                function_name = None
                function_2_name = None

                for line in file1_lines:
                    stripped_line = line.strip()
                    if stripped_line.startswith("async def "):
                        stripped_line = stripped_line.replace("async ", "", 1)
                    if stripped_line.startswith("def "):
                        function_name = stripped_line.split(")")[0].strip().replace("def ", "")

                        break
                for line in file2_lines:
                    stripped_line = line.strip()
                    if stripped_line.startswith("async def "):
                        stripped_line = stripped_line.replace("async ", "", 1)
                    if stripped_line.startswith("def "):
                        function_2_name = stripped_line.split(":")[0].strip().replace("def ", "") + ":"

                        break

                differences = sync_compare_files_ignore_comments(file1_lines, file2_lines)
                refactored_code, function_call_code, first_clone = refactor_and_generate_function(differences, function_name, function_2_name, line_count, line_count_2, store_first=True)


                replace_lines_in_file(file1_path, file1_start_line, file1_end_line, refactored_code)
                print(f"Refactored code written to {file1_path}")

                    # Farklı dosyadaysa import ifadesini ekle
                if file1_path != file2_path:
                    stripped_line = function_name.strip()
                    function_new_name = stripped_line.replace("def ", "").split("(")[0].strip()
                    module_name = convert_path_to_module(file1_path, base_path)
                    import_statement = f'from {module_name} import {function_new_name}'
                    add_import_to_file(import_statement, file2_path)
                    print(f'Import statement "{import_statement}" added to {file2_path}')


                replace_lines_in_file(file2_path, file2_start_line, file2_end_line, function_call_code)
                print(f"Function call written to {file2_path}")




                if ismultipair > 2: #Multikontrol
                    while multi_clone < ismultipair :
                        multifile_path = os.path.join(base_path, source_files[multi_clone].get('file'))
                        multifile_start_line = int(source_files[multi_clone].get('startline'))
                        multifile_end_line = int(source_files[multi_clone].get('endline'))
                        filen_lines = read_non_comment_lines(file1_path, file1_start_line, file1_end_line)

                        multi_array_path.append(multifile_path)
                        multi_array_start.append(multifile_start_line)
                        multi_array_end.append(multifile_end_line)
                        line_count_multi = multifile_end_line - multifile_start_line + 1

                        if not os.path.exists(multifile_path):
                            print(f"File not found: {multifile_path}")
                            continue

                        multifile_lines = read_non_comment_lines(multifile_path, multifile_start_line, multifile_end_line)
                        #multifile_lines = multifile_lines[0].strip()
                        if has_class_dependency(multifile_lines):
                            print(f"Function in {multifile_path} is unrefactorable due to class dependency.")
                        else:

                            function_name = None
                            multifunction_name = None

                            for line in file1_lines:
                                stripped_line = line.strip()
                                if stripped_line.startswith("async def "):
                                    stripped_line = stripped_line.replace("async ", "", 1)
                                if stripped_line.startswith("def "):
                                    function_name = stripped_line.split(")")[0].strip().replace("def ", "")

                                    break
                            for line in multifile_lines:
                                stripped_line = line.strip()
                                if stripped_line.startswith("def "):
                                    multifunction_name = stripped_line.split(":")[0].strip().replace("def ", "") + ":"
                                    break
                            new_differences = sync_compare_files_ignore_comments(filen_lines, multifile_lines)
                            new_refactored_code, new_function_call_code , new_first_clone = refactor_and_generate_function(new_differences,
                                                                                                 function_name, multifunction_name, line_count, line_count_multi, store_first=False)

                            replace_lines_in_file(file1_path, file1_start_line, file1_end_line, new_refactored_code)
                            print(f"Refactored code written to {file1_path}")

                            # Farklı dosyadaysa import ifadesini ekle
                            if file1_path != multifile_path:
                                stripped_line =  function_name.strip()
                                function_new_name = stripped_line.replace("def ", "").split("(")[0].strip()
                                module_name = convert_path_to_module(file1_path, base_path)
                                import_statement = f'from {module_name} import {function_new_name}'
                                add_import_to_file(import_statement, multifile_path)
                                print(f'Import statement "{import_statement}" added to {multifile_path}')


                            replace_lines_in_file(multifile_path, multifile_start_line, multifile_end_line,
                                                      new_function_call_code)
                            print(f"Function call written to {multifile_path}")
                        multi_clone+=1

        elif 80 <= similarity <= 89:
            single = 0
            multi = 1
            functions = []
            function1_code = read_non_comment_lines(file1_path, file1_start_line, file1_end_line)
            function2_code = read_non_comment_lines(file2_path, file2_start_line, file2_end_line)

            functions.append((function1_code, function2_code))
            refactored_funcs, refactored_func1, refactored_func2, ext_function_name = refactor_functions_80(
                function1_code, function2_code, file1_path, file2_path, single)

            if refactored_funcs != None:

                if has_class_dependency_80(refactored_funcs):
                    print(f"Function in {file1_path} or {file2_path} is unrefactorable due to class dependency.")
                else:
                    replace_lines_in_file(file1_path, file1_start_line, file1_end_line, refactored_func1)
                    print(f"Refactored code written to {file1_path}")
                    lines = refactored_func1.strip().split('\n')
                    num_lines_eighty = len(lines) - 1

                    function_length = num_lines_eighty - (file1_end_line - file1_start_line)

                    if file1_path != file2_path:
                        stripped_line = ext_function_name.strip()
                        function_new_name = stripped_line.replace("def ", "").split("(")[0].strip()
                        module_name = convert_path_to_module(file1_path, base_path)
                        import_statement = f'from {module_name} import {function_new_name}'
                        add_import_to_file(import_statement, file2_path)
                        print(f'Import statement "{import_statement}" added to {file2_path}')
                        replace_lines_in_file(file2_path, file2_start_line, file2_end_line, refactored_func2)
                        print(f"Function call written to {file2_path}")
                    else:
                        replace_lines_in_file(file2_path, (file2_start_line + function_length),
                                              (file2_end_line + function_length), refactored_func2)
                        print(f"Function call written to {file2_path}")

                    if ismultipair > 2:  # Multikontrol
                        while multi_clone < ismultipair:
                            functions_multi_code = []
                            multifile_path = os.path.join(base_path, source_files[multi_clone].get('file'))
                            multifile_start_line = int(source_files[multi_clone].get('startline'))
                            multifile_end_line = int(source_files[multi_clone].get('endline'))


                            if not os.path.exists(multifile_path):
                                print(f"File not found: {multifile_path}")
                                continue
                            if file1_path != multifile_path or signal_eighty == 1:
                                functions_multi_code = extract_code_from_file(multifile_path, multifile_start_line,
                                                                              multifile_end_line)
                            else:
                                functions_multi_code = extract_code_from_file(multifile_path,
                                                                              (multifile_start_line + function_length),
                                                                              (multifile_end_line + function_length))

                            multi_refactored_funcs, multi_refactored_func1, multi_refactored_func2, ext_function_name = refactor_functions_80(
                                refactored_func1, functions_multi_code, file1_path, multifile_path, multi)
                            if file1_path != multifile_path:

                                stripped_line = ext_function_name.strip()
                                function_new_name = stripped_line.replace("def ", "").split("(")[0].strip()
                                module_name = convert_path_to_module(file1_path, base_path)
                                import_statement = f'from {module_name} import {function_new_name}'
                                add_import_to_file(import_statement, multifile_path)
                                print(f'Import statement "{import_statement}" added to {multifile_path}')
                                replace_lines_in_file(multifile_path, multifile_start_line, multifile_end_line,
                                                      multi_refactored_func2)
                                print(f"Function call written to {multifile_path}")
                            elif signal_eighty == 1:
                                replace_lines_in_file(multifile_path, multifile_start_line, multifile_end_line,
                                                      multi_refactored_func2)
                                print(f"Function call written to {multifile_path}")
                            else:
                                replace_lines_in_file(multifile_path, (multifile_start_line + function_length),
                                                      (multifile_end_line + function_length),
                                                      multi_refactored_func2)
                                print(f"Function call written to {multifile_path}")
                            multi_clone += 1

            else:
                print(f'# of equal lines are less then 8')


def main():
    args = parse_args()
    parse_xml_and_compare(args.xml_path)

if __name__ == "__main__":
    main()