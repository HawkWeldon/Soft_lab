#!/run/current-system/sw/bin/bash
echo "Number of Files:"
ls -a | wc -w
echo "Total disc usage:"
du -hs
echo "Detailed file listing:"
ls -rtl | tail -n +2