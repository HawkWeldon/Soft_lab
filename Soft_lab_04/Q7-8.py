import subprocess
import sys

if len(sys.argv) < 2:
    print("give a usr")
    sys.exit(1)

given_usr = sys.argv[1]

who = subprocess.run(["who"], capture_output=True, text=True).stdout
last = subprocess.run(["last"], capture_output=True, text=True).stdout

who_lines = who.strip().splitlines()
logged_in_count = len(who_lines)

current_users = []

for line in who_lines:
    usr_name = line.split()[0]
    if usr_name not in current_users:
        current_users.append(usr_name)

usr_logged_in = given_usr in current_users

last_lines = []

for line in last.splitlines():
    if line.strip() and not line.startswith("wtmp"):
        last_lines.append(line)

last_10 = last_lines[:10]

unique_users = set()

for line in last_lines:
    parts = line.split()

    if parts:
        usr_name = parts[0]

        if usr_name not in ["reboot", "shutdown", "wtmp"]:
            unique_users.add(usr_name)

with open("Q7-8.txt", "w") as file:
    file.write("========== LOGIN REPORT ==========\n")

    file.write("Currently Logged-in Users:\n")

    for line in who_lines:
        parts = line.split()

        username = parts[0]
        login_time = " ".join(parts[2:5])

        file.write(f"User: {username}\tLogin Time: {login_time}\n")

    file.write(f"\nNumber of logged-in users: {logged_in_count}\n")

    file.write(f"\nIs '{given_usr}' currently logged in? "f"{'Yes' if usr_logged_in else 'No'}\n")

    file.write("\nLast 10 User Logins:\n")

    for line in last_10:
        file.write(line + "\n")

    file.write(f"\nNumber of unique users who logged in:"f"{len(unique_users)}\n")

    file.write("\nMost Recent Login:\n")

    if last_10:
        file.write(last_10[0] + "\n")
    else:
        file.write("No login history found.\n")

    file.write("==================================")