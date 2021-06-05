# https://codeforces.com/problemset/problem/766/A

a = input()
b = input()

if a == b:
    print(-1)
elif len(a) > len(b) or len(a) < len(b):
    print(max(len(a), len(b)))
else:
    print(len(a))
