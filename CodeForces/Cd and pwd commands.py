# https://codeforces.com/problemset/problem/158/C


n = int(input())
commands = []
for i in range(n):
    c = input()
    if(c[:2] == "cd"):
        commands = commands + c[3:].split("/")
    else:
        commands.append(c)

path = []
for command in commands:
    # current path
    if(len(path) == 0):
        curren_path = "/"
    else:
        curren_path = "".join(path) + "/"

    if(command == "pwd"):
        print(curren_path)
    else:
        # cd ..
        if(command == ".."):
            if(len(path) != 0):
                path.pop()
        # cd folder
        else:
            if(command == ""):
                path = []
            else:
                path.append("/" + command)
