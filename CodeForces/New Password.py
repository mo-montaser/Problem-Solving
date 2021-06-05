# https://codeforces.com/problemset/problem/770/A

n, k = map(int, input().split())
password = ""
letters = "abcdefghijklmnopqrstuvwxyz"
j = 0

for i in range(n):
    password += letters[j]
    j += 1
    if(j == k):
        j = 0

print(password)
