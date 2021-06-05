# https://codeforces.com/problemset/problem/520/A

n = int(input())
string = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
flag = "YES"

if(n < 26):
    flag = "NO"
else:
    string = string.lower()
    for i in alpha:
        if i not in string:
            flag = "NO"
            break

print(flag)
