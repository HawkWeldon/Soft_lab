#!/run/current-system/sw/bin/bash

pspm()
{
    pname="$1"
    pid=$(pgrep -x "$pname")

    if [ -n "$pid" ]
    then 
        echo "running"
        echo "pid = $1"
        cpu=$(ps -p "$pid" -o %cpu=)
        mem=$(ps -p "$pid" -o %mem=)
        echo "cpu usage is $cpu"
        echo "mem usage is $mem"

    else
        echo "not running"
    fi
}

echo "-----enter-process-----"
read process
pspm "$process" > Q8.txt