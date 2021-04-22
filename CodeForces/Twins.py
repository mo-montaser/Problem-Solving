# https://codeforces.com/problemset/problem/160/A

n = int(input())
a = list(map(int, input().split()))

coins_sum = sum(a)
coins = 0
a.sort(reverse=True)

for i in range(n):
    coins += a[i]
    if(coins > coins_sum // 2):
        print(i + 1)
        break
