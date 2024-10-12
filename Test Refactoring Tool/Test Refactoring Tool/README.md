# TRADE

This project is a Python application designed to automatically refactor clones in python test code. Follow the steps below to download, install and run the project.

## Installation

### Requirements

- Python 3.6 or higher
- `pip` (Python package manager)
- Git

### Step 1: Download the TRADE

Download TRADE to your local machine

### Step 2: Add your code to "systems" folder

Put the python project to refactor into “Test Refactoring Tool/systems”.

### Step 3: Install the TRADE

To run TRADE from the terminal, navigate to the main directory where you downloaded TRADE and install it with the following command:
```shell	
	pip install .
```
### Step 4: Set the BASE_PATH Environment Variable	

The project requires the BASE_PATH environment variable to be set. This variable should point to the root directory of the project:
```shell
	export BASE_PATH=$(pwd)  # On Windows: set BASE_PATH=%cd%
```
Replace $(pwd) with the path where you downloaded TRADE. For example
```shell
	export BASE_PATH=/path/to/where/you/downloaded/Test\ Refactoring\ Tool
```
### Step 5: Run the Project

You can now run the project directly from the terminal:
```shell
	TRADE --xml_path XML_PATH 
```
Replace XML_PATH with the actual path to the XML file you want to process. For example:
```shell
	TRADE --xml_path /path/to/your/file.xml
```
## Usage
The project uses the BASE_PATH environment variable to dynamically handle file paths. Make sure to set this variable to the correct directory path before running the project.The project uses also an XML file that contains clone detection output data. The XML file should specify source code clones, along with details such as file paths, line numbers, and similarity metrics. You can specify the path to this XML file using the `--xml_path` argument.


## Contributing
If you would like to contribute, please open an issue or submit a pull request.	

