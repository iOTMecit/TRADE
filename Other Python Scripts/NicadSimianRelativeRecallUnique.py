import xml.etree.ElementTree as ET
from collections import defaultdict
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

def parse_simian_classes(file_path):
    clone_classes = []
    tree = ET.parse(file_path)
    root = tree.getroot()
    for clone_set in root.findall(".//set"):
        blocks = [
            (
                os.path.basename(block.attrib["sourceFile"]),
                int(block.attrib["startLineNumber"]),
                int(block.attrib["endLineNumber"]),
            )
            for block in clone_set.findall("block")
        ]
        clone_classes.append(blocks)
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

def count_unique_clone_classes(nicad_classes, simian_classes):
    unique_classes = []
    for nicad_class in nicad_classes:
        unique_classes.append(nicad_class)
    for simian_class in simian_classes:
        if not any(are_clone_classes_similar(simian_class, unique_class) for unique_class in unique_classes):
            unique_classes.append(simian_class)
    return len(unique_classes)

# Load clone classes from both files
nicad_classes = parse_nicad_classes("/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/Deleteds/Vestel/VestelCode_Nicad.xml")
simian_classes = parse_simian_classes("/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/Deleteds/Vestel/Vestel_Simian_filtered.xml")

# Count unique clone classes
total_unique_classes = count_unique_clone_classes(nicad_classes, simian_classes)
print(f"Total unique clone classes: {total_unique_classes}")

