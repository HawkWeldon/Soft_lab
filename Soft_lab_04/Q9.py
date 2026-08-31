import subprocess
import sys

if len(sys.argv) < 2:
    print("Give a process")
    sys.exit(1)

process_name = sys.argv[1]

result = subprocess.run(["pgrep", "-x", process_name], capture_output=True, text=True)

if result.returncode != 0:
    print(f"Process {process_name} is not running.")
    sys.exit(0)

pids = result.stdout.strip().splitlines()

print(f"Process {process_name} is running.")

for pid in pids:
    ps_result = subprocess.run(["ps","-p",pid,"-o","pid,%cpu,%mem"], capture_output=True, text=True)
    print(ps_result.stdout)