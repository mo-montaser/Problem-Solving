# https://codeforces.com/problemset/problem/344/A

n = int(input())
magnets = []
for i in range(n):
    magnets.append(input())

counter = 1
for i in range(n - 1):
    if(magnets[i][1] == magnets[i + 1][0]):
        counter += 1

print(counter)
