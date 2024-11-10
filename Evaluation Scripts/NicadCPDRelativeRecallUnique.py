import xml.etree.ElementTree as ET
import os


def parse_nicad_classes(file_path):
    clone_classes = []
    tree = ET.parse(file_path)
    root = tree.getroot()
    for clone_class in root.findall(".//class"):
        sources = [
            (os.path.basename(src.attrib["file"]), int(src.attrib["startline"]), int(src.attrib["endline"]))
            for src in clone_class.findall("source")
        ]
        clone_classes.append(sources)
    return clone_classes


def parse_cpd_classes(file_path):
    clone_classes = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if "Found a" in lines[i] and "line" in lines[i]:
            line_count = int(lines[i].split("Found a ")[1].split(" line")[0])
            clone_sources = []
            j = i + 1
            while j < len(lines) and "Starting at line" in lines[j]:
                start_line = int(lines[j].split("Starting at line ")[1].split(" of ")[0])
                end_line = start_line + line_count - 1
                file_path = os.path.basename(lines[j].split(" of ")[1].split(" &")[0].strip())
                clone_sources.append((file_path, start_line, end_line))
                j += 1
            clone_classes.append(clone_sources)
    return clone_classes


def are_sources_similar(src1, src2):
    file1, start1, end1 = src1
    file2, start2, end2 = src2
    return file1 == file2 and abs(start1 - start2) <= 5 and abs(end1 - end2) <= 5


def are_clone_classes_similar(class1, class2):
    # Check if two clone classes are similar based on file names and line ranges
    return all(
        any(are_sources_similar(src1, src2) for src2 in class2)
        for src1 in class1
    ) and all(
        any(are_sources_similar(src2, src1) for src1 in class1)
        for src2 in class2
    )


def count_unique_clone_classes(nicad_classes, cpd_classes):
    unique_classes = []
    for nicad_class in nicad_classes:
        unique_classes.append(nicad_class)
    for cpd_class in cpd_classes:
        if not any(are_clone_classes_similar(cpd_class, unique_class) for unique_class in unique_classes):
            unique_classes.append(cpd_class)
    return len(unique_classes)


# Load clone classes from both files
nicad_classes = parse_nicad_classes("/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/Deleteds/HomeAssistant/Home-deleted-Nicad.xml")
cpd_classes = parse_cpd_classes("/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/Deleteds/HomeAssistant/filtered-Home-deleted-cpd.xml")

# Count unique clone classes
total_unique_classes = count_unique_clone_classes(nicad_classes, cpd_classes)
print(f"Total unique clone classes: {total_unique_classes}")

