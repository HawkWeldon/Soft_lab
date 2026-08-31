from pathlib import Path
import csv 

file = Path("student.csv")

if file.is_file():
    with open(file, "r", newline= "") as f:
        reader = csv.DictReader(f)
        students = list(reader)

    print("Total number of lines:", len(students))

    cse_count = sum(1 for student in students if student["Department"] == "Computer Science")
    ee_count = sum(1 for student in students if student["Department"] == "Electrical Engineering")

    print("CSE students:", cse_count)
    print("EE students:", ee_count)

    print("Analysis Completed")
else:
    print("file doesn't exist")