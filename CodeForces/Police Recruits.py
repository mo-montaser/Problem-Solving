# https://codeforces.com/problemset/problem/427/A

n = int(input())
events = list(map(int, input().split()))
untreated_crimes = 0
officers = 0

for i in range(n):
    if(events[i] > 0):
        officers += events[i]
    elif(officers >= 1):
        officers += events[i]
    else:
        untreated_crimes += 1

print(untreated_crimes)
