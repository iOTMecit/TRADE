import os
import time
import xml.etree.ElementTree as ET
import re
import ast


CONTEXT_SIZE = 2  # Number of lines before/after to check
stored_differences = {}
global_param_deff= []
param_index = 1
function_counter = 1
old_line_count_80 = 0
new_line_count_80 = 0
exact_count = 0
near_count = 0
similar_count = 0

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
    if isinstance(function_code_blocks[0], str):  # Single block (list of lines)
        function_code_blocks = [function_code_blocks]  # Wrap it in a list

    for block in function_code_blocks:
        new_block = block[:]  # Copy to preserve original
        while len(new_block) >= 5:
            has_dependency = False
            for line in new_block:
                stripped_line = line.strip()
                if stripped_line.startswith('def ') and ('self' in stripped_line or 'cls' in stripped_line):
                    has_dependency = True
                    break
                if 'self.' in stripped_line or 'cls.' in stripped_line:
                    has_dependency = True
                    break
            if not has_dependency:
                return new_block  # Return modified block if no dependency
            new_block.pop()  # Remove last line
    return []  # Return empty list if dependency exists

def wrap_code_in_function(lines):

    indented_lines = ["    " + line for line in lines]
    return "def temp_function():\n" + "\n".join(indented_lines)


def extract_variable_dependencies(lines, assigned_variables=None):
    dependencies = set()
    code_block = wrap_code_in_function(lines)

    try:
        tree = ast.parse(code_block)

    except SyntaxError as e:
        return []

    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            dependencies.add(node.id)

    if assigned_variables:
        dependencies -= assigned_variables

    return sorted(dependencies)

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


def refactor_and_generate_function(differences, function_name, function_2_name, line_count_primer, line_count_seconder, import_function = None, store_first=False):
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
    # Eğer function_new_name varsa replacement_code başına ekle
    if import_function:
        function_name = f"{import_function}.{function_name}"

    param_assignments_str = ', '.join([f"{k}='{v}'" for k, v in param_assignments.items()])
    function_call = f"def {function_2_name}\n\t{function_name}, {param_assignments_str})"
    empty_rows_seconder = line_count_seconder - len(function_call.split('\n'))
    added_empty_rows_seconder = ['\n'] * empty_rows_seconder
    added_empty_rows_seconder_str = ''.join(added_empty_rows_seconder)
    function_call = function_call + added_empty_rows_seconder_str

    return refactored_code, function_call, param_function_code


def replace_lines_in_file(file_path, start_line, end_line, replacement_code):


    replacement_lines = replacement_code.splitlines(keepends=True)  # Preserve blank lines and line endings
    replacement_line_count = len(replacement_lines)
    original_line_count = end_line - start_line
    size_difference = original_line_count - replacement_line_count

    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for i, line in enumerate(lines):
            if i + 1 == start_line:
                file.write(replacement_code + '\n')
                if size_difference > 0:
                    file.writelines(['\n'] * size_difference)
            if not (start_line <= i + 1 <= end_line):
                file.write(line)


def add_import_to_file(import_statement, target_file):

    with open(target_file, 'r') as file:
        content = file.read()

    # Check if the import statement is already present
    if import_statement not in content:

        new_content = import_statement + '\n' + content

        with open(target_file, 'w') as file:
            file.write(new_content)
def append_extracted_function_to_file(file_path, function_code):

    with open(file_path, 'a') as file:
        file.write('\n')
        file.write(function_code)
        file.write('\n')


def convert_path_to_module(file_path, base_directory):
    """Converts a file path to a Python module naming convention and separates the last part as import name."""
    # Get the relative path
    relative_path = os.path.relpath(file_path, base_directory)
    # Replace path separators with dots for module naming
    module_path = relative_path.replace(os.path.sep, '.')
    # Remove the .py extension
    full_module_name = os.path.splitext(module_path)[0]

    # Split to get the module name and import name
    *module_parts, import_name = full_module_name.rsplit('.', 1)
    module_name = '.'.join(module_parts)  # Up to 'hardware'

    return module_name, import_name

def code_length_difference(code_line, start_point , end_point):
    """Kaydırma yapmmak için."""
    refactored_code_length = len(code_line) + 1
    code_length = end_point - start_point
    difference = (code_length - refactored_code_length) - 1

    return code_length, refactored_code_length, difference

def extract_assigned_variables(lines):
    variables = set()
    # Updated pattern to capture variables in a comma-separated list on the left side of an assignment
    variable_pattern = re.compile(r'\b(\w+)\b(?:\s*,\s*\b(\w+)\b)*\s*=')

    for line in lines:
        # Find all matches for the pattern, which should return tuples of strings
        matches = variable_pattern.findall(line)
        # Flatten tuples and add each variable to the set
        for match in matches:
            variables.update(var for var in match if var)

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

    # Iterate over each character in all lines
    for line in lines:
        for char in line:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if stack and stack[-1] == closing_brackets[char]:
                    stack.pop()
                else:
                    print(f"Unmatched closing bracket found in line: {line.strip()}")
                    return True

    if stack:
        print("Unmatched opening brackets remain in stack.")
    return bool(stack)


def clone_results():
    print("100% refactored clone count:", exact_count)
    print("Between 90% - 100% refactored clone count:", near_count)
    print("Between 80% - 90% refactored clone count:", similar_count)


def find_common_lines_80(func1_lines, func2_lines, type , min_length=5):
    global common_blocks, function_counter
    length1, length2 = len(func1_lines), len(func2_lines)
    equal_counter = 0
    i = 0
    if type == 0:
        common_blocks = []
        i = 1
        while i < length1:
            j = 1
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

                    while has_unmatched_closing_bracket(temp_common):
                        # Eğer temp_common uzunluğu min_length'ten küçükse döngüden çık
                        if len(temp_common) < min_length:
                            print(
                                f"Aborting refactor, temp_common length ({len(temp_common)}) is below min_length ({min_length}).")
                            i = start_i
                            break

                        # Son satırı kaldır
                        temp_common = temp_common[:-1]

                    # Kapanış parantez sorunu yoksa refactoring işlemi devam eder
                    if not has_unmatched_closing_bracket(temp_common):
                        function_name = f"extracted_function_{function_counter}"
                        function_counter += 1
                        common_blocks.append((function_name, temp_common))

                        # temp_common'un uzunluğu kadar i ve j güncellenir
                        j = start_j + len(temp_common)
                        i = start_i + len(temp_common)
                        start_i = i
                    else:
                        print("Aborting refactor due to unmatched closing brackets.")

                else:
                    j += 1
                    i = start_i

            i += 1
    else:
        if func1_lines and func1_lines[0].strip().startswith("def"):
            func1_lines = func1_lines[1:]

        if len(func1_lines) > 1 and func1_lines[0].strip().startswith("global"):
            func1_lines = func1_lines[1:]

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


def refactor_functions_80(func1, func2, path1, path2, import_name, type):
    func1_lines = func1
    func2_lines = func2
    global old_line_count_80, new_line_count_80, previous_assigned_variable, previous_variable_names

    common_blocks = find_common_lines_80(func1_lines, func2_lines, type)

    def is_indent_valid(lines, next_line):
        # İlk satırın girintisi
        first_indent = len(lines[0]) - len(lines[0].lstrip())
        # Sonraki satırın girintisi
        next_indent = len(next_line) - len(next_line.lstrip())
        # Girinti kontrolü
        return next_indent <= first_indent

    def get_next_non_empty_line(lines, last_common_line):
        """
        Find the next non-empty line after the last common line.
        """
        if last_common_line in lines:
            next_index = lines.index(last_common_line) + 1  # Find the index of last_common_line
        else:
            # If last_common_line is not in lines, return None
            return None, None

        # Skip empty lines
        while next_index < len(lines) and lines[next_index].strip() == "":
            next_index += 1

        if next_index < len(lines):
            return lines[next_index], next_index
        return None, None

    if type == 0:
        if common_blocks:
            refactored_functions = []
            func1_refactored, func2_refactored = '\n'.join(func1), '\n'.join(func2)  # List to string conversion
            all_refactored = []
            for i, (function_name, lines) in enumerate(common_blocks):

                if lines[0].strip():  # Check if the first line is non-empty
                    first_common_line = lines[0]
                elif len(lines) > 1 and lines[1].strip():  # Check if the second line is non-empty
                    first_common_line = lines[1]
                base_indent = len(first_common_line) - len(first_common_line.lstrip())

                # Find the next non-empty line for indentation validation
                next_line, next_index = get_next_non_empty_line(func1_lines, lines[-1])

                # While common block has at least 5 lines, perform the validation
                while len(lines) >= 5:
                    common_first_indent = len(lines[0]) - len(lines[0].lstrip())  # Indent of first line in common block
                    common_last_indent = len(lines[-1]) - len(lines[-1].lstrip())  # Indent of last line in common block
                    next_line_indent = len(next_line) - len(next_line.lstrip()) if next_line else None

                    if next_line:  # Ensure there's a valid next line
                        if common_last_indent > next_line_indent:
                            # Common last line's indentation is greater -> Remove last line
                            lines.pop()  # Remove the last line
                            next_line, next_index = get_next_non_empty_line(func1_lines, lines[-1] if lines else None)

                        elif common_first_indent < next_line_indent:
                            # Common first line's indentation is smaller -> Remove first line
                            lines.pop(0)  # Remove the first line
                            next_line, next_index = get_next_non_empty_line(func1_lines, lines[-1] if lines else None)
                        else:
                            # If neither condition applies, break the loop
                            break
                    else:
                        # If no valid next line is found, break the loop
                        break

                # If the common block is too small, skip refactoring
                if len(lines) < 5:
                    continue

                # Add the lines of the common block to the refactored code
                lines = has_class_dependency_80(lines)
                if not lines:
                    print(f"Function in {path1} or {path2} is unrefactorable due to class dependency.")

                assigned_variables = extract_assigned_variables(lines)
                variable_names = ", ".join(extract_variable_dependencies(lines, assigned_variables))
                previous_assigned_variable = assigned_variables
                previous_variable_names = variable_names

                # Refactored code block
                refactored_code = []
                refactored_function_call = []
                refactored_code.append(add_with_relative_indent(f"def {function_name}({variable_names}):",0))
                refactored_line_count = 1
                refactored_function_call = ""
                # Add nonlocal declaration if variables are found
                if assigned_variables:
                    nonlocal_declaration = "global " + ", ".join(assigned_variables)
                    refactored_code.append(add_with_relative_indent(nonlocal_declaration, 4))
                    refactored_function_call = add_with_relative_indent(nonlocal_declaration, base_indent) + "\n"
                    refactored_line_count = 2

                refactored_code += [
                    add_with_relative_indent(line, 0) for line in lines if
                    not (line.strip().startswith("return") and line == lines[-1])
                ]

                # Save refactored code as a new function in the list
                refactored_functions.append(refactored_code)

                if path1 != path2:
                    function_name = f"{import_name}.{function_name}"

                # Refactored function call for func2 with the same base indentation as the common block
                refactored_function_call += add_with_relative_indent(f"{function_name}({variable_names})",
                                                                     base_indent)

                # Calculate the difference in line count between the original and refactored code
                original_line_count = len(lines)

                # Add the difference in blank lines after the function call in func1 and func2

                if refactored_line_count < original_line_count:
                    blank_lines_to_add = original_line_count - refactored_line_count
                    refactored_function_call += '\n' * blank_lines_to_add

                # Convert back to strings before performing replacements
                common_block_text = "\n".join(lines)
                all_refactored += refactored_code

                old_line_count_80 = len(func1)

                # Perform replacements on string versions
                func1_refactored = func1_refactored.replace(common_block_text, refactored_function_call)

                func2_refactored = func2_refactored.replace(common_block_text, refactored_function_call)

            refactored_code_text = '\n'.join(all_refactored)
            return refactored_functions, func1_refactored, func2_refactored, refactored_code_text
        else:
            return None, '\n'.join(func1), '\n'.join(func2),None
    else:

        if common_blocks:
            refactored_functions = []
            func1_refactored, multi_refactored = func1, func2  # Convert list to string

            for i, (function_name, lines) in enumerate(common_blocks):

                first_common_line = lines[0]
                base_indent = len(first_common_line) - len(first_common_line.lstrip())
                refactored_line_count = 1

                refactored_function_call = ""

                if previous_assigned_variable:
                    nonlocal_declaration = "global " + ", ".join(previous_assigned_variable)
                    refactored_function_call = add_with_relative_indent(nonlocal_declaration, base_indent) + "\n"
                    refactored_line_count = 2

                if path1 != path2:
                    function_name = f"{import_name}.{function_name}"

                # Refactored function call for func2 with the same base indentation as the common block
                refactored_function_call += add_with_relative_indent(f"{function_name}({previous_variable_names})",
                                                                     base_indent)

                # Calculate the difference in line count between the original and refactored code
                original_line_count = len(lines)

                # Add the difference in blank lines after the function call in func2
                if refactored_line_count < original_line_count:
                    blank_lines_to_add = original_line_count - refactored_line_count
                    refactored_function_call += "\n" * blank_lines_to_add

                # Replace the common block in func2 with the function call
                common_block_text = "\n".join(lines)

                if common_block_text in multi_refactored:
                    multi_refactored = multi_refactored.replace(common_block_text, refactored_function_call)

                    return func1, func1, multi_refactored, True

                else:
                    return func1, func1, multi_refactored, False


        else:
            return None, '\n'.join(func1), '\n'.join(func2), False


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
        global global_param_deff, exact_count, near_count, similar_count
        import_name = None
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
                    # Farklı dosyadaysa import ifadesini ekle
                if file1_path != file2_path:
                    module_name, import_name = convert_path_to_module(file1_path, base_path)
                    import_statement = f'from {module_name} import {import_name}'
                    add_import_to_file(import_statement, file2_path)
                    print(f'Import statement "{import_statement}" added to {file2_path}')

                differences = sync_compare_files_ignore_comments(file1_lines, file2_lines)
                refactored_code, function_call_code, first_clone = refactor_and_generate_function(differences, function_name, function_2_name, line_count, line_count_2, import_name, store_first=True)


                replace_lines_in_file(file1_path, file1_start_line, file1_end_line, refactored_code)
                print(f"Refactored code written to {file1_path}")



                replace_lines_in_file(file2_path, file2_start_line, file2_end_line, function_call_code)
                print(f"Function call written to {file2_path}")

                if similarity == 100 :
                    exact_count += 1
                else :
                    near_count += 1


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

                            # Farklı dosyadaysa import ifadesini ekle
                            if file1_path != multifile_path:
                                module_name, import_name = convert_path_to_module(file1_path, base_path)
                                import_statement = f'from {module_name} import {import_name}'
                                add_import_to_file(import_statement, multifile_path)
                                print(f'Import statement "{import_statement}" added to {multifile_path}')

                            new_differences = sync_compare_files_ignore_comments(filen_lines, multifile_lines)
                            new_refactored_code, new_function_call_code , new_first_clone = refactor_and_generate_function(new_differences,
                                                                                                 function_name, multifunction_name, line_count, line_count_multi, import_name, store_first=False)

                            replace_lines_in_file(file1_path, file1_start_line, file1_end_line, new_refactored_code)
                            print(f"Refactored code written to {file1_path}")

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
            module_name, import_name = convert_path_to_module(file1_path, base_path)
            refactored_funcs, refactored_func1, refactored_func2, extracted_func = refactor_functions_80(
                function1_code, function2_code, file1_path, file2_path, import_name, single)

            if refactored_funcs:

                modified_block = has_class_dependency_80(refactored_funcs)
                if not modified_block:
                    continue
                else:
                    replace_lines_in_file(file1_path, file1_start_line, file1_end_line, refactored_func1)
                    print(f"Refactored code written to {file1_path}")
                    append_extracted_function_to_file(file1_path,extracted_func)
                    print(f"Extracted Function written to {file1_path}")

                    lines = refactored_func1.strip().split('\n')


                    if file1_path != file2_path:

                        import_statement = f'from {module_name} import {import_name}'
                        add_import_to_file(import_statement, file2_path)
                        print(f'Import statement "{import_statement}" added to {file2_path}')

                    replace_lines_in_file(file2_path, file2_start_line, file2_end_line, refactored_func2)
                    print(f"Function call written to {file2_path}")

                    similar_count += 1


                    if ismultipair > 2:  # Multikontrol
                        while multi_clone < ismultipair:
                            functions_multi_code = []

                            multifile_path = os.path.join(base_path, source_files[multi_clone].get('file'))
                            multifile_start_line = int(source_files[multi_clone].get('startline'))
                            multifile_end_line = int(source_files[multi_clone].get('endline'))


                            if not os.path.exists(multifile_path):
                                print(f"File not found: {multifile_path}")
                                continue
                            functions_multi_code = read_non_comment_lines(multifile_path, multifile_start_line,
                                                                              multifile_end_line)
                            functions_multi_code = '\n'.join(functions_multi_code)

                            module_name, import_name = convert_path_to_module(file1_path, base_path)
                            multi_refactored_funcs, multi_refactored_func1, multi_refactored_func2, extracted_func = refactor_functions_80(
                                refactored_func1, functions_multi_code, file1_path, multifile_path, import_name, multi)

                            if extracted_func == True:

                                if file1_path != multifile_path:

                                    import_statement = f'from {module_name} import {import_name}'
                                    add_import_to_file(import_statement, multifile_path)
                                    print(f'Import statement "{import_statement}" added to {multifile_path}')

                                replace_lines_in_file(multifile_path, multifile_start_line, multifile_end_line,
                                                          multi_refactored_func2)
                                print(f"Function call written to {multifile_path}")


                            else:
                                print("The Pair does not have the same code segment ")
                            multi_clone += 1

            else:
                print(f'# of equal lines are less then 5')


def main():
    args = parse_args()
    parse_xml_and_compare(args.xml_path)
    clone_results()

if __name__ == "__main__":
    main()
