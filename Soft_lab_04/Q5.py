import os 

dirs = input("Enter dir names: ").split()

for dir in dirs:

    if not os.path.isdir(dir):
        print(f"{dir}: doesn not exist")
        continue

    file_count = 0
    total_size = 0

    for root, dirz, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            try: 
                total_size += os.path.getsize(path)
                file_count += 1
            except (PermissionError, OSError): pass

    size_mb = total_size / (1024 * 1024)

    print("Dir:",dir)
    print("No of files:", file_count)
    print(f"Disk usage: {size_mb:2f} MB")

    if size_mb < 100:
        print("Sml\n")
    elif size_mb <= 1024:
        print("Mid\n")
    else:
        print("Lrg\n")