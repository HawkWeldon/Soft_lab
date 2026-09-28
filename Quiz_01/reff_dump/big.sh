#!/run/current-system/sw/bin/bash
dir="/home/hawk"
cd "$dir"
du -sh */ | sort -hr | head -n 10