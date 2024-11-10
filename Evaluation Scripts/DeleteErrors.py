import os


def convert_path(log_path):
    return log_path.replace('_', '/')


def delete_files_from_log(log_file_path, project_root):
    deleted_files = set()  

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if 'TXL0192E' in line or 'TXL0127E' in line:
                start_index = line.find("systems_")
                end_index = line.find("-pyindent", start_index)

                if start_index == -1 or end_index == -1:
                    continue  

                log_path = line[start_index:end_index].strip()

                project_relative_path = convert_path(log_path)
                project_file_path = os.path.join(project_root, project_relative_path)

                if not os.path.isfile(project_file_path):
                    if log_path.endswith('.py'):
                        path_before_py = log_path.rsplit('_', 1)
                        if len(path_before_py) == 2:
                            alternative_log_path = path_before_py[0].replace('_', '/') + '_' + path_before_py[1]
                            alternative_path = os.path.join(project_root, alternative_log_path)
                            print(f"Alternative path check: {alternative_path}")
                            if os.path.isfile(alternative_path):
                                project_file_path = alternative_path

                if os.path.isfile(project_file_path) and project_file_path not in deleted_files:
                    os.remove(project_file_path)
                    deleted_files.add(project_file_path)  
                    print(f"{project_file_path} deleted.")
                elif project_file_path in deleted_files:
                    print(f"{project_file_path} already deleted.")
                else:
                    print(f"{project_file_path} cannot found or already deleted.")


log_file_path = '/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/C.log'  
project_root = '/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/'  
delete_files_from_log(log_file_path, project_root)

