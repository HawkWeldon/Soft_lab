#!/run/current-system/sw/bin/bash

ULR()
{
    arg="$1"
    
    echo "All logged in users and their login time"
    who
    echo ""

    echo "Number of logged in users"
    who | wc -l
    echo ""

    if who | grep -q "$arg"; 
    then
        echo "$arg is logged in"
    else
        echo "$arg is not logged in"
    fi
    echo ""

    echo "last 10 users to log in"
    last -n 10 | awk '{print $1}' | head -n -1
    echo ""

    echo "No of unique users to log in"
    last | awk '{print $1}' | sort -u | wc -l
    echo ""

    echo "The most recent log in"
    last -n 1 | awk '{print $1}' | head -n -1
    echo ""
}

echo "-------Enter user to search-------"
read arg
ULR "$arg" > Q7.txt