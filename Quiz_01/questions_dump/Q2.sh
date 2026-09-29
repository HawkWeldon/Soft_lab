#!/run/current-system/sw/bin/bash
analysis()
{
    csv="$1"
    echo "_______Analysis_Start_______"
    echo ""

    if [ ! -f "$csv" ]
    then
        echo "file doesn't exist"
        echo ""
    else
        echo "Total number of line"
        cat "$csv" | wc -l
        echo ""

        echo "Total number of EE students"
        cat "$csv" | grep "Electrical Engineering" | wc -l
        echo ""

        echo "Total number of CSE students"
        cat "$csv" | grep "Computer Science" | wc -l
        echo ""
    fi

    echo "_______Analysis_finish______"
}

analysis "student.csv"