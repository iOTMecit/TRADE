import re

def parse_simian_text(file_path):
    total_clone_pairs = 0
    total_clone_count = 0
    clone_group_count = 0  # New variable to count clone groups

    # Regular expression to match the start of a clone group, <set lineCount=...>
    clone_group_pattern = re.compile(r'<set lineCount="\d+"')

    # Regular expression to match <block sourceFile="..."> entries
    file_pattern = re.compile(r'<block sourceFile="([^"]+)"')

    # Counter for files in each clone group
    clone_group_files = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # If a new clone group is found
            if clone_group_pattern.search(line):
                clone_group_count += 1  # Increment the clone group count

                # If there were files in the previous group, calculate clone pairs and count clones
                if len(clone_group_files) > 1:
                    total_clone_pairs += calculate_clone_pairs(len(clone_group_files))
                total_clone_count += len(clone_group_files)  # Add all files (clones) from the group

                # Reset the list for the new clone group
                clone_group_files = []

            # If a file is part of the clone group, add it to the list
            match = file_pattern.search(line)
            if match:
                clone_group_files.append(match.group(1))

        # Handle the last group
        if len(clone_group_files) > 1:
            total_clone_pairs += calculate_clone_pairs(len(clone_group_files))
        total_clone_count += len(clone_group_files)  # Count files in the last group

    return total_clone_pairs, total_clone_count, clone_group_count


def calculate_clone_pairs(n):
    """Calculate the clone pair count using the formula n(n-1)/2"""
    return n * (n - 1) // 2


# Path to the CPD output text file
file_path = ('/home/vestel/Desktop/Tez/CloneDetection/simian-academic/simian-4.0.0/HomeAssistant.xml')

# Calculate the total clone pair count, clone count, and clone group count
total_pairs, total_clones, total_groups = parse_simian_text(file_path)
print(f"Total Clone Pairs: {total_pairs}")
print(f"Total Clone Groups: {total_groups}")
print(f"Total Clones: {total_clones}")
