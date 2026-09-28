#!/run/current-system/sw/bin/bash

ULR()
{
    usr="$1"

    echo "All users logged in"
    who | head -n 1
    echo ""

    echo "login time for each"
    who | awk '{print $3 " " $4}'
    echo ""

    echo "Number logged in"
    who | wc -l
    echo ""

    echo "Is $usr logged in ?"
    if [ $(who | grep "$usr" | wc -l) -gt 0 ]
    then 
        echo "yes"
    else
        echo "no"
    fi
    echo ""

    echo "last 10 users logged in"
    last | head -n 10 | awk '{print $1}'
    echo ""

    echo "no of unique logged in users"
    last | awk '{print $1}' |sort -u | wc -l
    echo ""

    echo "last login"
    last -n 1 | head -n 1 | awk '{print $1}'
    echo ""
}

echo "-----User-----"
read usr
ULR "$usr" > Q7.txt