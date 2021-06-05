# https://codeforces.com/problemset/problem/231/A

n = int(input())
counter = 0
for i in range(n):
    if input().count("1") >= 2:
        counter += 1

print(counter)
