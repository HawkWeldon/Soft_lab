#!/run/current-system/sw/bin/bash

cd ~

count=0

while read -r folder
do
    folder0=$(echo "$folder" | awk '{print $9}')

    if [ -d "$folder0" ]
    then
        echo "$folder0"
        count=$((count + 1))
    fi

    if [ "$count" -eq 10 ]
    then
        break
    fi

done < <(ls -lt)