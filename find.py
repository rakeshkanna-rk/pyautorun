from textPlay.colors import *
from constants import *

def findLine(config, line):

    found_line = False
    try:
        with open(config, "r") as f:
            lines = f.readlines()
            for i, l in enumerate(lines):
                if l.strip().startswith(line):
                    found_line = True
                    print(f"Found '{BLUE}{line}{RESET}' @ {YELLOW}line {i+1}{RESET} in {CYAN}{config}{RESET}")
            if not found_line:
                print(f"{RED}Line not found{RESET} @ {BLUE}{config}{RESET}")

    except FileNotFoundError:
        FileNotFound()