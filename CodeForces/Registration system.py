# https://codeforces.com/problemset/problem/4/C


n = int(input())
names = []
for i in range(n):
    names.append(input())

database = {}
dups = {}

for name in names:
    if(name not in database):
        database[name] = ""
        print("OK")
    else:
        if(name not in dups):
            dups[name] = 1
            print(name + str(dups[name]))
        else:
            dups[name] += 1
            print(name + str(dups[name]))
