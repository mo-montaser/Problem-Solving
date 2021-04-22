# https://codeforces.com/problemset/problem/298/A

n = input()
steps = input()
r = steps.count("R")
l = steps.count("L")

if(l == 0):
    start = steps.index("R") + 1
    end = steps.rindex("R") + 2
elif(r == 0):
    start = steps.rindex("L") + 1
    end = steps.index("L")
else:
    if(l >= r):
        start = steps.rindex("L") + 1
        end = steps.rindex("R") + 2
    else:
        start = steps.index("R") + 1
        end = steps.index("L") + 1


print(start, end)
