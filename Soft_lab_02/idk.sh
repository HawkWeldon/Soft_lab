#!/run/current-system/sw/bin/bash
dir="$1"
#for variables we need to put no spaces
echo "Directory: $dir"
echo "Number of files"
ls "$dir" | wc -l
echo "Disc usage"
du -sh "$dir"
echo "Detailed file listing"
ls -rtl "$1" | tail -n +2