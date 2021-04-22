# https://codeforces.com/problemset/problem/14/A

user_input = input().split()
n = int(user_input[0])
m = int(user_input[1])
recatangle = []
for i in range(n):
    recatangle.append(input())

start_m = []
end_m = []

for i in range(len(recatangle)):
    if "*" in recatangle[i]:
        start_n = i
        break

for i in reversed(range(len(recatangle))):
    if "*" in recatangle[i]:
        end_n = i
        break

for i in recatangle:
    if "*" in i:
        start_m.append(i.index("*"))
        end_m.append(i.rindex("*"))

for i in range(start_n, end_n + 1):
    print(recatangle[i][min(start_m):max(end_m) + 1])
