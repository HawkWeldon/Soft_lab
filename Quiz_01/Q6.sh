#!/run/current-system/sw/bin/bash

SIR()
{
    echo "Date & Time"
    date
    echo ""

    echo "User logged in"
    whoami
    echo ""

    echo "Host"
    hostname
    echo ""

    echo "Current dir"
    pwd
    echo ""

    echo "Available disk space"
    df -h 
    echo ""

    echo "Available memory"
    free
    echo ""

    echo "Uptime"
    uptime
    echo""
}

SIR > Q6.txt