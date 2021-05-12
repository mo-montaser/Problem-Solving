# https://codeforces.com/contest/474/problem/B

def lower_bound(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] >= value:
            right = mid - 1
        else:
            left = mid + 1
    return left


n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = input().split()

for i in range(1, n):
    a[i] = a[i] + a[i - 1]

for qi in q:
    print(lower_bound(a, int(qi)) + 1)
