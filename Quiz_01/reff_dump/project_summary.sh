#!/run/current-system/sw/bin/bash
dir="project_dir"
if [ ! -d "$dir" ]
then
    echo "dir doesn't exist"
else
    cd "./$dir"
    echo "Number of Files:"
    ls -a | wc -w
    echo "Total disc usage:"
    du -hs
    echo "Display by time modified"
    ls -lt
    echo "Analysis complete"
fi