
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


with open(".pyscripts", "r") as f:
    lines = f.readlines()
    lines = [x for x in lines if x != "" or x != "\n"]

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

else:
    print("No commands executing")
                
            
# print()
# print(cmd)
# print()
# for i in check_line: print(i)



            

           


            
    
