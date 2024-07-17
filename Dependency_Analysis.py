from lxml import etree as ET
import os
import re
import subprocess
import json
import ast


def parse_nicad_xml(xml_file):
    if not os.path.exists(xml_file):
        print(f"XML file not found: {xml_file}")
        return []

    clones = []
    try:
        parser = ET.XMLParser(recover=True)
        tree = ET.parse(xml_file, parser=parser)
        root = tree.getroot()

        for class_tag in root.findall('class'):
            similarity = class_tag.get('similarity')
            if similarity == "100":
                clone_pair = []
                for source in class_tag.findall('source'):
                    file_path = source.get('file')
                    start_line = int(source.get('startline'))
                    end_line = int(source.get('endline'))
                    clone_pair.append((file_path, start_line, end_line))
                clones.append(clone_pair)
    except ET.XMLSyntaxError as e:
        print(f"Error parsing XML file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return clones


def extract_function_name(base_path, file_path, start_line):
    full_file_path = os.path.join(base_path, file_path)
    if not os.path.exists(full_file_path):
        print(f"File not found: {full_file_path}")
        return None

    try:
        with open(full_file_path, 'r') as file:
            lines = file.readlines()
            for i in range(start_line - 1, len(lines)):
                if lines[i].strip().startswith('def '):
                    function_name = re.findall(r'def (\w+)\(', lines[i])
                    if function_name:
                        return function_name[0]
    except Exception as e:
        print(f"Error reading file {full_file_path}: {e}")

    return None


def normalize_indentation(code):
    lines = code.split('\n')
    min_indent = min((len(line) - len(line.lstrip(' '))) for line in lines if line.strip())
    normalized_code = '\n'.join(line[min_indent:] for line in lines)
    return normalized_code


def fix_print_statements(code):
    fixed_code = re.sub(r"print\s+'(.*?)'", r"print('\1')", code)
    fixed_code = re.sub(r'print\s+"(.*?)"', r'print("\1")', fixed_code)
    fixed_code = re.sub(r'print\s+(.*?)(\s*\n|\s*$)', r'print(\1)\2', fixed_code)
    return fixed_code


def is_class_dependency(node, class_names):
    # Check if the node is a class definition, a method of a class, or an attribute of a known class
    if isinstance(node, ast.ClassDef):
        return True, node.name
    elif isinstance(node, ast.FunctionDef):
        for arg in node.args.args:
            if arg.arg == 'self':
                return True, f"Method {node.name} with 'self'"
    elif isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id in class_names:
        return True, f"{node.value.id}.{node.attr}"
    return False, ""


def analyze_class_dependencies(code):
    try:
        normalized_code = normalize_indentation(code)
        fixed_code = fix_print_statements(normalized_code)
        tree = ast.parse(fixed_code)

        class_names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_names.add(node.name)

        for node in ast.walk(tree):
            has_dep, dep = is_class_dependency(node, class_names)
            if has_dep:
                return True, f"Class dependency found in code: {dep}"

        return False, ""
    except SyntaxError as e:
        return True, f"Syntax error in code analysis for code:\n{code}\nNormalized code:\n{fixed_code}\nError: {e}"


def analyze_file_dependencies_with_pydeps(base_path, project_path, function_name):
    output_path = os.path.join(base_path, 'dependency_graph.json')

    try:
        result = subprocess.run(
            ['pydeps', '--noshow', '--max-bacon=2', '--output', output_path, '--output-format=json', project_path],
            capture_output=True, text=True)
        if result.returncode != 0:
            return False, f"Error running pydeps: {result.stderr}"

        with open(output_path, 'r') as f:
            dependencies = json.load(f)

        for module, details in dependencies.items():
            for dep in details.get('imports', []):
                if function_name in dep:
                    return True, f"Dependency found in pydeps output: {dep}"
    except Exception as e:
        return True, f"Error analyzing dependencies: {e}"

    return False, ""


def analyze_dependencies(clone, base_path, project_path):
    for file_path, start_line, end_line in clone:
        try:
            full_file_path = os.path.join(base_path, file_path)
            with open(full_file_path, 'r') as file:
                lines = file.readlines()
                code = ''.join(lines[start_line - 1:end_line])

                # Check class dependencies in the code snippet
                has_class_deps, class_reason = analyze_class_dependencies(code)
                if has_class_deps:
                    return True, f"Class dependency issue: {class_reason}"

                # Extract function name and check for external dependencies
                function_name = extract_function_name(base_path, file_path, start_line)
                if function_name:
                    has_external_deps, external_reason = analyze_file_dependencies_with_pydeps(base_path, project_path,
                                                                                               function_name)
                    if has_external_deps:
                        return True, f"External dependency issue: {external_reason}"
        except Exception as e:
            return True, f"Error reading file {file_path}: {e}"
    return False, ""


def main():
    xml_file = '/home/vestel/Desktop/Otomatik/SadeceTestToga_functions-blind-clones-0.30-classes-withsource.xml'
    base_path = '/home/vestel/Desktop/Otomatik'
    project_path = os.path.join(base_path, 'systems/SadeceTestToga')

    clones = parse_nicad_xml(xml_file)

    for clone_pair in clones:
        has_deps, reason = analyze_dependencies(clone_pair, base_path, project_path)
        if not has_deps:
            print(f"Clone pair {clone_pair} is refactorable.")
        else:
            print(f"Clone pair {clone_pair} is unrefactorable. Reason: {reason}")


if __name__ == "__main__":
    main()
