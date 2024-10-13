from textPlay.colors import *
import time
import os

def createConfig(name):
    if not name:
        with open(".pyscripts", "w") as f:
            f.write(f"# Line Of Configuration (LOC) file = .pyscripts [{time.ctime()}]\n")
    else:
        with open(name, "w") as f:
            f.write(f"# Line Of Configuration (LOC) file = {name} [{time.ctime()}]\n")

    print(f"{GREEN}Config file created{RESET} @ {BLUE}{os.getcwd()}{RESET} \nUse: {MAGENTA}pyauto run{RESET}")
    print("To run the script")