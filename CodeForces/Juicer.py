# https://codeforces.com/problemset/problem/709/A

n, b, d = map(int, input().split())
a = list(map(int, input().split()))
sum_a = 0
counter = 0

for i in range(n):
    if(a[i] <= b):
        sum_a += a[i]
        if(sum_a > d):
            counter += 1
            sum_a = 0

print(counter)
