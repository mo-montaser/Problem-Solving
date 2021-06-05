# https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
players = list(map(int, input().split()))
counter = 0

for i in range(n):
    if players[k - 1] <= players[i] and players[i] > 0:
        counter += 1

print(counter)
