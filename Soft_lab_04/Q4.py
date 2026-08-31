import os

dir="./project_dir"

file_count = {}

for root, dirs, files in os.walk(dir):
    for file in files:
        if file in file_count:
            file_count[file] += 1
        else:
            file_count[file] = 1

for file, count in file_count.items():
    if count > 1:
        print(file)