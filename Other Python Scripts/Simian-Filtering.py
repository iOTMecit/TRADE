import xml.etree.ElementTree as ET


def process_and_filter_simian_output(input_file_path, output_file_path):
    tree = ET.parse(input_file_path)
    root = tree.getroot()


    clone_groups = []
    for clone_set in root.findall(".//set"):
        blocks = []
        for block in clone_set.findall("block"):
            source_file = block.get("sourceFile")
            start_line = int(block.get("startLineNumber"))
            end_line = int(block.get("endLineNumber"))
            blocks.append((source_file, start_line, end_line))
        clone_groups.append((clone_set, blocks))


    clone_groups.reverse()


    filtered_clone_groups = []
    for i, (clone_set, blocks) in enumerate(clone_groups):
        should_add = True
        for j, (_, other_blocks) in enumerate(clone_groups):
            if j <= i:
                continue  

            for file_path, start, end in blocks:
                for other_file_path, other_start, other_end in other_blocks:

                    if file_path == other_file_path and start <= other_start <= end and start <= other_end <= end:
                        should_add = False
                        break
                if not should_add:
                    break
            if not should_add:
                break


        if should_add:
            filtered_clone_groups.append(clone_set)


    new_root = ET.Element("simian", attrib=root.attrib)
    for clone_set in filtered_clone_groups:  # Orijinal sıralamada yazdır
        new_root.append(clone_set)


    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_file_path, encoding="utf-8", xml_declaration=True)


input_file = '/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/Deleteds/Vestel/Vestel_Simian_Before.xml'
output_file = '/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/Deleteds/Vestel/Vestel_Simian_filtered.xml'

process_and_filter_simian_output(input_file, output_file)

