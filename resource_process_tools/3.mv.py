import os
import shutil
import glob

# Define the source directory
source_dir = './'

# Find all files matching the pattern 'Lesson_LX_*.ipynb'
files = glob.glob(os.path.join(source_dir, 'Lesson_*.ipynb'))

#%%
# Loop through each file found
for file_path in files:
    # Extract the base name of the file (without the extension)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Create a new directory with the base name
    new_dir = os.path.join(source_dir, base_name)
    os.makedirs(new_dir, exist_ok=True)

    # Move the file into the newly created directory
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))

print("Files have been moved successfully.")