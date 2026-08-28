#!/run/current-system/sw/bin/bash

info_printer()
{
    dir=$1
    if [ -d "$dir" ];
    then
        echo "Number of files int $dir"
        ls "$dir" | wc -l
        
        echo "Disk space used"
        usage=$(du -sb "$dir" | cut -f1)
        echo "$usage"
        
        if [ "$usage" -gt 1000000000 ];
        then
            echo "$dir is large"
        elif [ "$usage" -gt 100000000 ] && [ "$usage" -lt 1000000000 ];
        then 
            echo "$dir is medium"
        else
            echo "$dir is small"
        fi
    else
        echo "$dir does not exist"
    fi
}

read input

for val in $input
do 
    info_printer "$val"
    echo -e "\n"
done