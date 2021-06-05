# https://codeforces.com/problemset/problem/791/A

a, b = map(int, input().split())
counter = 0

while(b >= a):
    a = a * 3
    b = b * 2
    counter += 1

print(counter)
