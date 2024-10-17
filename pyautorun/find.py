from textPlay.colors import *
from pyautorun.constants import *

def findLine(config, line):

    found_line = False
    headerFound = False
    header = None
    try:
        with open(config, "r") as f:
            lines = f.readlines()
            for i, l in enumerate(lines):
                if l.strip().startswith("[py.") and l.strip().endswith("]"):
                    headerFound = True
                    header = l[4:-2]
                if l.strip().startswith(line):
                    found_line = True
                    print(f"Found '{BLUE}{l.strip().replace('\n', '')}{RESET}' @ {YELLOW}line {i+1}{RESET} in {CYAN}{header}{RESET}")
            if not found_line:
                print(f"{RED}Line not found{RESET} @ {BLUE}{config}{RESET}")
            elif not headerFound:
                print(f"{RED}Header not found{RESET} @ {BLUE}{config}{RESET}")
            elif not headerFound and not found_line:
                print(f"{RED}Line and header not found{RESET} @ {BLUE}{config}{RESET}")

    except FileNotFoundError:
        FileNotFound()