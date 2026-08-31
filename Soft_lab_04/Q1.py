from pathlib import Path

dir = "project_dir"
dir = "./" + dir

if Path(dir).is_dir():
    files = [path for path in Path(dir).rglob("*") if path.is_file()]

    print("No of files:", len(files))

    total_size = sum(file.stat().st_size for file in files)
    print("Total disk usage:", total_size, "bytes")

    files.sort(key = lambda file: file.stat().st_mtime, reverse= True)
    print("\n Files sorter by mod time:")
    for file in files: print(file)
else:
    print("no a dir")