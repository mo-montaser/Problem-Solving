# https://codeforces.com/problemset/problem/266/A

n = int(input())
string = input()
counter = 0

for i in range(1, n):
    if(string[i] == string[i - 1]):
        counter += 1

print(counter)
