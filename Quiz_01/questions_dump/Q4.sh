#!/run/current-system/sw/bin/bash

find . -type f -printf "%f\n" | uniq -d | sort