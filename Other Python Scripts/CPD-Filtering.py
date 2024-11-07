import re

def process_and_filter_cpd_output(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    clone_groups = []  
    i = 0
    while i < len(lines):
        line = lines[i]
        found_match = re.search(r'Found a (\d+) line', line)

        if found_match:
            total_lines = int(found_match.group(1))
            clone_pairs = [line]  


            i += 1
            current_group = [] 
            while i < len(lines):
                starting_line = lines[i]
                starting_match = re.search(r'(Starting at line (\d+) of (.+))', starting_line)

                if starting_match:
                    start_line_info = starting_match.group(1)
                    start_line = int(starting_match.group(2))
                    clone_file_path = starting_match.group(3).strip()
                    end_line = start_line + total_lines - 1
                    new_line = f"{start_line_info} & Finished at line {end_line}\n"
                    clone_pairs.append(new_line)
                    current_group.append((clone_file_path, start_line, end_line))
                else:
                    break
                i += 1


            clone_groups.append((clone_pairs, current_group))
        else:
            i += 1


    filtered_clones = []
    for index, (clone_text, current_group) in enumerate(clone_groups):
        should_add = True
        for other_index, (_, other_group) in enumerate(clone_groups):
            if other_index <= index:
                continue 

            for clone_file_path, start, end in current_group:
                for other_file_path, other_start, other_end in other_group:

                    if clone_file_path == other_file_path and start <= other_start <= end and start <= other_end <= end:
                        should_add = False
                        break
                if not should_add:
                    break
            if not should_add:
                break


        if should_add:
            filtered_clones.extend(clone_text)


    with open(file_path, 'w') as file:
        file.writelines(filtered_clones)


process_and_filter_cpd_output('/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/Deleteds/Vestel/Vestel_CPD_Before.xml')

