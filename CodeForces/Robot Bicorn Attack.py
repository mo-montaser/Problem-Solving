# https://codeforces.com/problemset/problem/175/A

s = input()
n = len(s)
max_points = -1

for i in range(1, n - 1):
    for j in range(i + 1, n):
        a = s[:i]
        b = s[i:j]
        c = s[j:]

        if(int(a) <= 10 ** 6 and int(b) <= 10 ** 6 and int(c) <= 10 ** 6):
            if((a[0] == "0" and len(a) > 1) or (b[0] == "0" and len(b) > 1) or (c[0] == "0" and len(c) > 1)):
                continue
            else:
                points = int(a) + int(b) + int(c)
                if(max_points < points):
                    max_points = points

print(max_points)
