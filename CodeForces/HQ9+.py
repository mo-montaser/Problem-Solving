# https://codeforces.com/problemset/problem/133/A

p = input()
flag = 0

for i in p:
    if(i == "H" or i == "Q" or i == "9"):
        flag = 1
        break
    else:
        continue

if(flag == 1):
    print("YES")
else:
    print("NO")
