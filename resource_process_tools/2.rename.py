import json
import os
import re

def rename_ipynb_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # 获取首行标题信息
    first_cell = notebook['cells'][0]
    if first_cell['cell_type'] == 'markdown':
        first_line = first_cell['source'][0].strip()
        if first_line.startswith('#'):
            new_title = first_line.lstrip('#').strip()

            # 提取原文件名中的 Lesson_N 部分
            original_file_name = os.path.basename(file_path)
            lesson_match = re.search(r'Lesson_\d+', original_file_name)
            if lesson_match:
                lesson_part = lesson_match.group(0)
                new_file_name = f"{lesson_part}_{new_title}.ipynb"
            else:
                new_file_name = f"{new_title}.ipynb"

            # 重命名文件
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
            os.rename(file_path, new_file_path)
            print(f"File renamed to: {new_file_name}")
        else:
            print("First line is not a title.")
    else:
        print("First cell is not a markdown cell.")

def rename_all_ipynb_files_in_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                rename_ipynb_file(file_path)

# 使用示例
directory_path = './'
rename_all_ipynb_files_in_directory(directory_path)