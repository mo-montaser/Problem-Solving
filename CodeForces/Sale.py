# https://codeforces.com/problemset/problem/34/B

n, m = input().split()
n = int(n)
m = int(m)

a = input().split()
a = list(map(int, a))

max_sum = 0
a.sort()
check_max_sum = 0

for i in range(m):
    check_max_sum -= a[i]
    if(check_max_sum > max_sum):
        max_sum = check_max_sum

print(max_sum)
