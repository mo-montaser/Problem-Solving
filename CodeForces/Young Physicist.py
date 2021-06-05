# https://codeforces.com/problemset/problem/69/A

n = int(input())
coordinates = []
for i in range(n):
    coordinates.append(input().split())
x, y, z = 0, 0, 0

for i in range(n):
    x += int(coordinates[i][0])
    y += int(coordinates[i][1])
    z += int(coordinates[i][2])

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
