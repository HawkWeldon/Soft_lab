#!/run/current-system/sw/bin/bash

pspm()
{
    pname="$1"
    pid=$(pgrep -x "$pname")
    if [ -n "$pid" ];
    then
        echo "$pname is running"
        echo "$pid is it's pid"
        echo ""
        cpu=$(ps -p "$pid" -o %cpu=)
        mem=$(ps -p "$pid" -o %mem=)

        echo "CPU usage is $cpu%"
        echo "Memory usage is $mem%"
    else
        echo "$pname is not running"
    fi 
}

echo "-------Enter process to search-------"
read pname
pspm "$pname" > Q8-9.txt