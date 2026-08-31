import os
import getpass
import platform
import shutil
from datetime import datetime

with open("Q6.txt", "w") as file:

    file.write("----------------------SYS----------------------\n")

    file.write(f"Date and time       :{datetime.now()}\n")
    file.write(f"Logged-in Usrs      :{getpass.getuser()}\n")
    file.write(f"Hostname            :{platform.node()}\n")
    file.write(f"Working dir         :{os.getcwd()}\n")

    dsk = shutil.disk_usage("/")
    available_dsk = dsk.free / (1024**3)
    file.write(f"Available Dsk space : {available_dsk:2f} GB\n")

    mem = os.sysconf("SC_AVPHYS_PAGES")*os.sysconf("SC_PAGE_SIZE")
    available_mem = mem / (1024**3)
    file.write(f"Available Mem       : {available_mem:2f} GB\n")

    with open("/proc/uptime", "r") as f:
        uptime = float(f.readline().split()[0])
    days = int(uptime // 86400)
    hrs = int((uptime % 86400) // 3600)
    mins = int((uptime % 3600) // 60)

    file.write(f"System Uptime       : {days} days, {hrs} hrs, {mins} mins\n")
    file.write("----------------------SYS----------------------\n")