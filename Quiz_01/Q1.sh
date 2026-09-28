#!/run/current-system/sw/bin/bash
project_summary()
{
    dir="$1"
    echo "_______Analysis_Start_______"
    echo ""

    if [ ! -d "$dir" ]
    then
        echo "dir doesn't exist"
        echo ""

    else
        cd $dir
        echo "Disk usage"
        du -hs
        echo ""

        echo "Total number of files"
        ls | wc -l
        echo ""

        echo "Files ordered by make time"
        ls -t -l
        echo ""
        cd .. 
    fi

    echo "_______Analysis_finish______"

}

read dir
project_summary "$dir"