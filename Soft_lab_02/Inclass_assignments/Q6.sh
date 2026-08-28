#!/run/current-system/sw/bin/bash

SIR()
{
    echo "Date + time"
    date
    echo ""

    echo "User"
    whoami
    echo ""

    echo "Host"
    hostname
    echo ""

    echo "current dir"
    pwd
    echo ""

    echo "Available disk space"
    df -h /
    echo ""

    echo "Available memory"
    free -h
    echo ""

    echo "Uptime"
    uptime
    echo ""
}

SIR > Q6.txt