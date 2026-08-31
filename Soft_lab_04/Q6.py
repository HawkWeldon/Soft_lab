import os
import getpass
import platform
import shutil
from datetime import datetime

print("----------------------SYS----------------------")

print("Date and time       :",datetime.now())
print("Logged-in Usrs      :",getpass.getuser())
print("Hostname            :",platform.node())
print("Working dir         :",os.getcwd())

dsk = shutil.disk_usage("/")
available_dsk = dsk.free / (1024**3)
print(f"Available Dsk space : {available_dsk:2f} GB")

mem = os.sysconf("SC_AVPHYS_PAGES")*os.sysconf("SC_PAGE_SIZE")
available_mem = mem / (1024**3)
print(f"Available Mem       : {available_mem:2f} GB")

with open("/proc/uptime", "r") as f:
    uptime = float(f.readline().split()[0])
days = int(uptime // 86400)
hrs = int((uptime % 86400) // 3600)
mins = int((uptime % 3600) // 60)

print(f"System Uptime       : {days} days, {hrs} hrs, {mins} mins")
print("----------------------SYS----------------------")