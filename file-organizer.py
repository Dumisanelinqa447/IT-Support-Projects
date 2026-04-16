#Python
# File Organizer Script
# This script automatically organizes files into folders (Images, Documents)
# Helps improve file management and efficiency
# Demonstrates basic Python automation skills

import os
import shutil

path = "C:/Users/YourName/Downloads"
if not os.path.exists(path + "/Images"):
    os.makedirs(path + "/Images")

if not os.path.exists(path + "/Documents"):
    os.makedirs(path + "/Documents")
files = os.listdir(path)

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(path + "/" + file, path + "/Images/" + file)
    elif file.endswith(".pdf") or file.endswith(".docx"):
        shutil.move(path + "/" + file, path + "/Documents/" + file)
