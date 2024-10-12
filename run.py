import json
import os
from textPlay.colors import *
import time

def checkHeader(line, index)-> bool:          
    if line[-1] == "]\n" or line[-1] == "]":
        return True

    else:
        print(f"SyntaxError: No closing bracket @ line {index} \n{line} \n{'~'*(len(line))}^")
        exit()

# MAIN
error = "Error: "
cmd = []

header_check = False
cmd_line = False
comment = False
token = False
sec_header = False

check_line = []

config_loc = "./settings.json" # TODO : Change to "~/.pyautorun/settings.json"

print(f"\n\t{MAGENTA}PyAuto Run{RESET}\n")

try:
    with open(config_loc, "r") as jf:
        jdata = json.load(jf)
except FileNotFoundError:
    print(f"{RED}Config settings not found{RESET} \nUse: {MAGENTA}pyauto init{RESET}")
    exit()

if not jdata.get("user"):
    print("Username not found \nWriting to settings.json")
    user = input("Username: ")
    with open("settings.json", "r+") as jf:
        jdata["user"] = user
        json.dump(jdata, jf, indent=5)


if not jdata.get("config_file"):
    print(f"{YELLOW}Config file not found{RESET} \nWriting to settings.json")
    print("Config file: '.pyscripts'")
    with open("settings.json", "r+") as jf:
        jdata["config_file"] = ".pyscripts"
        json.dump(jdata, jf, indent=5)


config_file = jdata.get("config_file")
print(f"Config file: {config_file}")

try:
    with open(config_file, "r") as f:
        lines = f.readlines()
        lines = [x for x in lines if x != "" or x != "\n"]

except FileNotFoundError:
    print(f"{RED}Config file not found{RESET} \nUse: {MAGENTA}pyauto reset config_file -c {config_file}{RESET}")
    print("To change config file name in setings.json")
    exit()

if not lines[0].startswith(f"# Line Of Configuration (LOC) user = {jdata.get('user')}"):
    print(f"LOC not found \nWriting to {config_file}")
    user = jdata.get("user")
    loc = f"# Line Of Configuration (LOC) user = {user}\n"
    with open(config_file, "w") as f:
        f.writelines([loc]+lines)


run_cmd = input("Header Name: ")
print()

if "." in run_cmd:
    cmdtoken = run_cmd.split(".")[1]
    head_cmd = f"[py.{run_cmd.split(".")[0]}]"
    run_cmd = run_cmd.split(".")[0]
    token = True

    print(f"Header: {head_cmd}")
    print(f"Command token: {cmdtoken}")

    print()

for  index, line in enumerate(lines):
    index += 1
    line = line.replace("\n", "")

    if line.startswith("[py."):
        checkHeader(line, index)
    
    if line.startswith("[") and not line[1:].startswith("py."):
        print(f"Unexpected header found @ line {index}: {line}")
        exit()
    
    check_line.append(line)

    if line.startswith("[py.") and line[4:-1]==run_cmd and not header_check:
        header_check = checkHeader(line, index)
        print(f"Header found @ line {index}: {line}")
        cmd.append(line)

    elif line.startswith("#"):
        comment = True
    
    elif line.startswith("[py.") and header_check:
        sec_header = True

    elif "=" in line and header_check and not sec_header:
        cmd_line = True
        

        if token and line.split("=")[0].strip() == cmdtoken.strip():
            print("Token value:", line.split("=")[1].strip())
            cmd.append(line)

        else:
            cmd.append(line)

    
if not header_check and not token:
    print(f"{error}Header not found:", run_cmd)
elif not cmd_line and header_check:
    print(f"{error}Command not found")
elif not cmd_line and not header_check and not comment:
    print(f"{error}Syntax Error @ line {index}")


cmdstorun = []
for c in cmd[1:]:
    for i, value in enumerate(c):
        if value == "=" and not token:
            cmdstorun.append(c[i+1:].strip())
        
        elif token and value == "=" and c.split("=")[0].strip() == cmdtoken.strip():
            cmdstorun.append(c[i+1:].strip())


print(f"\nNumber of commands executing: {len(cmdstorun) if len(cmdstorun) >= 1 else 0}")

print("\nCommands:")

if len(cmdstorun) > 0:
    for cmds in cmdstorun:
        print(cmds)

    print("\nExecuting Commands...")

    for cmds in cmdstorun:
        print(f"\nExecuting: {MAGENTA}{cmds}{RESET}\n")
        os.system(cmds)

else:
    print("No commands executing")
                



            

           


            
    
