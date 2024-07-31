# 将Function-Calling-and-Data-Extraction-with-LLMs目录下, 根据 Lesson_N_xxx.ipynb与LN(其中N值得是课程序号)的匹配关系,将目录名称改为对应ipynb的名称,同时将Lesson_N_xxx.ipynb移动到LN目录内
import os
import shutil
import re

def rename_directories_and_move_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            ipynb_files = [f for f in os.listdir(dir_path) if f.endswith('.ipynb') and re.match(r'Lesson_\d+_', f)]

            if ipynb_files:
                ipynb_file = ipynb_files[0]
                new_dir_name = os.path.splitext(ipynb_file)[0]
                new_dir_path = os.path.join(root, new_dir_name)

                # Rename the directory
                os.rename(dir_path, new_dir_path)

                # Move the ipynb file into the renamed directory
                shutil.move(os.path.join(new_dir_path, ipynb_file), os.path.join(new_dir_path, ipynb_file))
                print(f"Renamed directory {dir_name} to {new_dir_name} and moved {ipynb_file} into it.")

# 使用示例
base_dir = './'
rename_directories_and_move_files(base_dir)