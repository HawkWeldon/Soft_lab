#!/run/current-system/sw/bin/bash
file="student.csv"
if [ ! -e "$file" ]
then 
    echo "File doesn't exist"
else 
    echo "File does exist"
    echo "Total number of lines"
    wc -l < "$file"
    echo "Total number of students in CSE"
    grep "Computer Science" "$file" | wc -l
    echo "Total number of students in EE"
    grep "Electrical Engineering" "$file" | wc -l
fi