from textPlay.colors import *
import os

def addtoScript(config, header, script):
    if "=" not in script:
        print(f"SyntaxError: No '=' in script name \nUsage: {MAGENTA}pyauto add -c <config_file> -h <header_name> -s '<script_name>=<script_to_run>'{RESET}")
        exit()
    else:
        with open(config, "a") as f:
            f.write(f"[py.{header}]\n{script}\n")
        print(f"{GREEN}Script added{RESET} @ {BLUE}{config}{RESET} \nUse: {MAGENTA}pyauto run{RESET}")
        print("To run the script")