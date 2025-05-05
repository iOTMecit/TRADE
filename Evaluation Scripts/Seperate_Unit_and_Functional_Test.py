import os
import shutil

# Define paths for Kivy test files based on the common Kivy test directory structure
kivy_test_dir = '/home/vestel/Downloads/Open Source Projects/DataSet/Kivy/Refactored Test Suite/Full Code/tests'
unit_tests = []
functional_tests = []

# Define directories for unit and functional tests
unit_dir = os.path.join(kivy_test_dir, "unit")
functional_dir = os.path.join(kivy_test_dir, "functional")

# Create directories if they do not exist
os.makedirs(unit_dir, exist_ok=True)
os.makedirs(functional_dir, exist_ok=True)

# Function to rename the file if a file with the same name exists
def get_unique_filename(directory, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

# Walk through the directory to classify files into unit or functional tests based on contents
for root, dirs, files in os.walk(kivy_test_dir):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            # Open each file and read its content to classify as unit or functional based on typical markers
            with open(file_path, 'r') as f:
                content = f.read()
                # Determine the destination directory and get a unique filename if necessary
                if any(keyword in content for keyword in ["mock", "MagicMock", "unittest", "GraphicUnitTest", "UnitKivyApp"]):
                    dest_dir = unit_dir
                else:
                    dest_dir = functional_dir

                # Get a unique filename and move the file
                unique_filename = get_unique_filename(dest_dir, file)
                shutil.move(file_path, os.path.join(dest_dir, unique_filename))
                (unit_tests if dest_dir == unit_dir else functional_tests).append(unique_filename)

# Print results
print(f"Unit tests moved to {unit_dir}:")
for test in unit_tests:
    print(test)

print(f"\nFunctional tests moved to {functional_dir}:")
for test in functional_tests:
    print(test)
