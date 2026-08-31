import os

home = os.path.expanduser("~")

dirs = []

for root, dir, files in os.walk(home):
    relative = os.path.relpath(root,start=home)
    if relative == ".":
        depth = 0
    else:
        depth = len(relative.split(os.sep))

    if depth != 1:
        continue

    total_size = 0
    for dirpath, subdirs, filenames in os.walk(root):
        for file in files:
            path = os.path.join(dirpath, file)
            try: total_size += os.path.getsize(path)
            except (PermissionError, OSError): pass
    dirs.append((total_size, root))

dirs.sort(reverse=True)

print("Top 10 dirs by size:\n")

for size, dir in dirs[:10]:
    size_hr = size

    units = ["B", "KB", "MB", "GB"]
    for unit in units:
        if size_hr < 1024: break
        size_hr /= 1024

    print(f"{size_hr:.2f} {unit} \t {dir}")