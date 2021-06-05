# https://codeforces.com/problemset/problem/443/A

string = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
counter = 0
for i in alpha:
    if i in string:
        counter += 1

print(counter)
