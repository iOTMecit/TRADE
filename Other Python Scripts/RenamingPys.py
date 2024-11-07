import os
import shutil


def collect_and_rename_py_files(source_dir, target_dir):
    os.makedirs(target_dir, exist_ok=True)

    counter = 1

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.py'):
                source_path = os.path.join(root, file)

                new_file_name = f"{counter}.py"
                target_path = os.path.join(target_dir, new_file_name)

                shutil.copy2(source_path, target_path)

                counter += 1

    print(f"Tüm .py dosyaları {target_dir} klasörüne numaralandırılarak kopyalandı.")


source_dir = "/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/Toga/"  # Projenin ana dizini
target_dir = "/home/vestel/Desktop/Tez/CloneDetection/6917-NiCad-6.2/NiCad-6.22-0.20/systems/C"  # Tüm .py dosyalarının toplanacağı hedef klasör

collect_and_rename_py_files(source_dir, target_dir)

