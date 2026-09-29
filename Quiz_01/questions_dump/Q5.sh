#!/run/current-system/sw/bin/bash

Health_Report()
{
    item="$1"
    echo "_______Analysis_Start_______"
    echo ""

    if [ ! -d "$item" ]
    then 
        echo "$item doesn't exist"
    else
        echo "No of files"
        find . -maxdepth 1 -type f | wc -l
        echo ""

        echo "Disk usage"
        du -hs | awk '{print $1}'
        echo ""

        usage=$(du -bs | awk '{print $1}')
        if [ "$usage" -gt 1000000000 ]
        then 
            echo "Size = Large"
        elif [ "$usage" -gt 1000000 ]
        then
            echo "Size = Medium"
        else
            echo "Size = Small"
        fi
        echo ""
    fi
    echo "_______Analysis_finish______"
}

read list

for item in $list 
do
    Health_Report "$item"
    echo ""
done